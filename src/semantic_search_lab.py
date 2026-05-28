import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Configure Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Sample PDF chunks
pdf_data = [
    "The CPU is the brain of the computer.",
    "Python is a high-level programming language.",
    "Photosynthesis is how plants make food from sunlight.",
    "The Great Wall of China is a historic landmark."
]

# User query
query = "Tell me about how greenery produces energy."

print("---  Semantic Search Lab ---")
print(f"User Query: '{query}'")

try:
    # Generate embeddings for PDF data
    pdf_embeddings = [
        client.models.embed_content(
            model="text-embedding-004",
            contents=text
        ).embeddings[0].values
        for text in pdf_data
    ]

    # Generate embedding for query
    query_embedding = client.models.embed_content(
        model="text-embedding-004",
        contents=query
    ).embeddings[0].values

    # Compute cosine similarity
    scores = cosine_similarity([query_embedding], pdf_embeddings)[0]

    # Find best match
    best_match_index = np.argmax(scores)

    print(f"\nTop Match Found: '{pdf_data[best_match_index]}'")
    print(f"Confidence Score: {scores[best_match_index]:.4f}")

except Exception as e:
    print(f" ERROR: {e}")