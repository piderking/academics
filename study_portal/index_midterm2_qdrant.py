import json
import os
import requests
from dotenv import load_dotenv
from google import genai
import uuid

load_dotenv('G:/My Drive/Academics/.env')
api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
qdrant_url = os.getenv('QDRANT_URL')
qdrant_key = os.getenv('QDRANT_API_KEY')

if not api_key or not qdrant_url:
    print("Warning: Missing GEMINI_API_KEY or QDRANT_URL in environment. Skipping Qdrant upload.")
    exit(0)

client = genai.Client(api_key=api_key)

with open('G:/My Drive/Academics/study_portal/decks.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

deck = next((d for d in data['decks'] if d['id'] == 'bot-1121-midterm-2'), None)
if not deck:
    print("Error: bot-1121-midterm-2 not found in decks.json")
    exit(1)

cards = deck['flashcards']
quizzes = deck.get('quizzes', [])
print(f"Preparing to index {len(cards)} flashcards and {len(quizzes)} quizzes for BOT-1121 Midterm 2 into Qdrant...")

headers = {
    'api-key': qdrant_key,
    'Content-Type': 'application/json'
}

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")

# 1. Flashcards embedding & upsert
points = []
for c in cards:
    text_to_embed = f"BOT-1121 Botany Midterm 2 Flashcard: {c['front']}\nAnswer: {c['back']}\nTags: {', '.join(c.get('tags', []))}\nCitation: {c.get('citation', '')}"
    try:
        resp = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text_to_embed
        )
        vec = resp.embeddings[0].values
        
        point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"bot-1121-midterm-2-{c['id']}"))
        points.append({
            "id": point_id,
            "vector": vec,
            "payload": {
                "course": "BOT-1121",
                "type": "flashcard",
                "deck_id": "bot-1121-midterm-2",
                "card_id": c['id'],
                "front": c['front'],
                "back": c['back'],
                "hint": c.get('hint'),
                "image": c.get('image'),
                "citation": c.get('citation'),
                "tags": c.get('tags', []),
                "source": deck['source']
            }
        })
    except Exception as e:
        print(f"Error embedding card {c['id']}: {e}")

# 2. Quizzes embedding & upsert
for idx, q in enumerate(quizzes):
    text_to_embed = f"BOT-1121 Botany Midterm 2 Quiz Practical: {q['station']}\nQuestion: {q['question']}\nCorrect Answer: {q['options'][q['correctIndex']]}\nExplanation: {q['explanation']}"
    try:
        resp = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text_to_embed
        )
        vec = resp.embeddings[0].values
        
        point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"bot-1121-midterm-2-quiz-{idx}"))
        points.append({
            "id": point_id,
            "vector": vec,
            "payload": {
                "course": "BOT-1121",
                "type": "quiz",
                "deck_id": "bot-1121-midterm-2",
                "station": q['station'],
                "question": q['question'],
                "options": q['options'],
                "correctIndex": q['correctIndex'],
                "explanation": q['explanation'],
                "image": q.get('image'),
                "citation": q.get('citation'),
                "source": deck['source']
            }
        })
    except Exception as e:
        print(f"Error embedding quiz {q['station']}: {e}")

print(f"Generated {len(points)} total vectors. Upserting to Qdrant collection 'academic_materials'...")

# Batch upsert in chunks of 20
collection_name = 'academic_materials'
for i in range(0, len(points), 20):
    batch = points[i:i+20]
    payload = {"points": batch}
    r = requests.put(f"{qdrant_url}/collections/{collection_name}/points?wait=true", headers=headers, json=payload)
    if r.status_code == 200:
        print(f"  Upserted batch {i//20 + 1}/{(len(points)+19)//20} ({len(batch)} points) - Status: {r.status_code}")
    else:
        print(f"  Upsert batch failed: {r.status_code} - {r.text}")

print("Qdrant synchronization complete!")
