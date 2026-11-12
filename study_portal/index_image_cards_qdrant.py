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

client = genai.Client(api_key=api_key)

with open('G:/My Drive/Academics/study_portal/midterm2_deck.json', 'r', encoding='utf-8') as f:
    deck = json.load(f)

# Focus on cards with images (24 cards total now)
cards_with_img = [c for c in deck['flashcards'] if c.get('image')]
print(f"Cards with images: {len(cards_with_img)}")

batch_size = 25
points = []

for i in range(0, len(cards_with_img), batch_size):
    batch = cards_with_img[i:i + batch_size]
    texts = [f"Botany Flashcard: {c['front']}\nAnswer: {c['back']}\nImage Description: {c.get('imageDescription','')}\nHint: {c.get('hint','')}" for c in batch]
    
    embed_resp = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts
    )
    
    for idx, c in enumerate(batch):
        vec = embed_resp.embeddings[idx].values
        point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"bot1121_midterm2_img_{c['id']}"))
        points.append({
            "id": point_id,
            "vector": vec,
            "payload": {
                "course": "BOT-1121",
                "filename": "midterm2_deck.json",
                "relative_path": "study_portal/midterm2_deck.json",
                "modality": "image_diagram",
                "content_preview": f"Image Card: {c['front']} | Image: {c['image']}",
                "gemini_description": c.get('imageDescription', '')
            }
        })

print(f"Upserting {len(points)} image-anchored points to Railway Qdrant...")
url = f"{qdrant_url}/collections/academic_materials/points?wait=true"
headers = {"Content-Type": "application/json", "api-key": qdrant_key}
res = requests.put(url, headers=headers, json={"points": points}, timeout=45)
print("Qdrant upsert status:", res.status_code, res.json())
