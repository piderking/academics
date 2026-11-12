"""
Academic Flashcard & Quiz Generator for Study Portal
Queries Railway Qdrant for course concepts, leverages Gemini Flash to synthesize
pedagogical flashcards and quizzes, and appends them to decks.json.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / ".academic_engine"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from config import GEMINI_API_KEY, VISION_MODEL
from vector_store import AcademicVectorStore
from multimodal_enricher import MultimodalEnricher
from google import genai
from google.genai import types

DECK_FILE = Path(__file__).resolve().parent / "decks.json"


def load_decks() -> Dict[str, Any]:
    if DECK_FILE.exists():
        with open(DECK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"decks": []}


def save_decks(data: Dict[str, Any]):
    with open(DECK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def generate_deck_from_qdrant(course: str, topic: str, deck_id: str = None, deck_title: str = None):
    store = AcademicVectorStore()
    enricher = MultimodalEnricher()
    client = genai.Client(api_key=GEMINI_API_KEY)

    print(f"[*] Querying Railway Qdrant for [{course}] '{topic}'...", flush=True)
    query_vec = enricher.embed_text(f"{course} {topic}")
    qdrant_results = store.search(query_vec, course=course if course != "ALL" else None, limit=6)

    if not qdrant_results:
        print(f"[!] No direct matches found in Qdrant for {course} - {topic}. Expanding search...", flush=True)
        qdrant_results = store.search(query_vec, limit=6)

    context_snippets = []
    source_files = set()
    for r in qdrant_results:
        source_files.add(r.get("filename", "Course Material"))
        pg = r.get("page_number")
        loc = f"Page {pg}" if pg else "Doc"
        desc = r.get("gemini_description")
        prev = r.get("content_preview", "")
        if desc:
            context_snippets.append(f"[{r.get('filename')} {loc} DIAGRAM]: {desc}")
        elif prev:
            context_snippets.append(f"[{r.get('filename')} {loc} TEXT]: {prev}")

    context_str = "\n\n".join(context_snippets)

    system_prompt = (
        "You are an expert academic curriculum designer and Socratic tutor. "
        "Your task is to generate high-yield, pedagogical flashcards and multiple-choice quiz questions "
        "grounded directly in the student's actual course materials retrieved from their vector store.\n\n"
        "Guidelines:\n"
        "1. Active recall: Focus on core definitions, biological/mathematical mechanisms, diagnostic chemical tests, and microscopy details.\n"
        "2. Flashcards must include:\n"
        "   - front: Clear, challenging diagnostic question or visual prompt.\n"
        "   - hint: Socratic stepping stone hint that guides without spoiling.\n"
        "   - back: Accurate, comprehensive explanation highlighting key terms in markdown bold (**term**).\n"
        "   - citation: Page/slide reference from the context.\n"
        "   - tags: 2-3 short keyword tags.\n"
        "3. Quizzes must include:\n"
        "   - question: Practical lab/exam scenario question.\n"
        "   - options: Exactly 4 distinct plausible options.\n"
        "   - correctIndex: 0-3 index of the correct option.\n"
        "   - explanation: Clear rationale explaining why the answer is correct and why other distractors are wrong.\n"
        "   - socraticHint: Guiding diagnostic hint.\n"
        "   - citation: Slide/page reference.\n\n"
        "Return ONLY a valid JSON object with keys 'title', 'description', 'flashcards', 'quizzes'."
    )

    user_prompt = (
        f"Course: {course}\n"
        f"Topic: {topic}\n"
        f"Primary Sources: {', '.join(source_files)}\n\n"
        f"Course Material Context Chunks:\n{context_str}\n\n"
        "Generate 6-8 comprehensive flashcards and 3-5 multiple-choice quiz questions formatted as JSON."
    )

    print("[*] Generating pedagogical flashcards & quiz via Gemini...", flush=True)
    response = client.models.generate_content(
        model=VISION_MODEL,
        contents=[user_prompt],
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type="application/json",
            temperature=0.2
        )
    )

    deck_content = json.loads(response.text)
    
    deck_obj = {
        "id": deck_id or f"{course.lower().replace(' ', '-').replace('(', '').replace(')', '')}-{topic.lower()[:15].replace(' ', '-')}",
        "course": course,
        "title": deck_title or deck_content.get("title", f"{course}: {topic}"),
        "description": deck_content.get("description", f"Study deck for {topic}"),
        "source": ", ".join(source_files) or "Course Material",
        "flashcards": deck_content.get("flashcards", []),
        "quizzes": deck_content.get("quizzes", [])
    }

    # Ensure all items have unique IDs
    for idx, c in enumerate(deck_obj["flashcards"]):
        if "id" not in c:
            c["id"] = f"{deck_obj['id']}-c{idx+1}"
    for idx, q in enumerate(deck_obj["quizzes"]):
        if "id" not in q:
            q["id"] = f"{deck_obj['id']}-q{idx+1}"

    data = load_decks()
    existing_idx = next((i for i, d in enumerate(data["decks"]) if d["id"] == deck_obj["id"]), -1)
    if existing_idx >= 0:
        data["decks"][existing_idx] = deck_obj
        print(f"[OK] Updated existing deck '{deck_obj['title']}' with {len(deck_obj['flashcards'])} cards and {len(deck_obj['quizzes'])} quizzes.")
    else:
        data["decks"].append(deck_obj)
        print(f"[OK] Created new deck '{deck_obj['title']}' with {len(deck_obj['flashcards'])} cards and {len(deck_obj['quizzes'])} quizzes.")

    save_decks(data)
    print(f"[OK] Saved to {DECK_FILE}")
    return deck_obj


def main():
    parser = argparse.ArgumentParser(description="Academic Flashcard & Quiz Generator")
    parser.add_argument("--course", type=str, required=True, help="Course code (e.g. BOT-1121, MATH-1151, STAT-1510, AI 300)")
    parser.add_argument("--topic", type=str, required=True, help="Topic or lab name (e.g. 'Lab 3 Plant Cells and Tissues')")
    parser.add_argument("--id", type=str, default=None, help="Optional custom deck ID")
    parser.add_argument("--title", type=str, default=None, help="Optional deck title")
    args = parser.parse_args()

    generate_deck_from_qdrant(course=args.course, topic=args.topic, deck_id=args.id, deck_title=args.title)


if __name__ == "__main__":
    main()
