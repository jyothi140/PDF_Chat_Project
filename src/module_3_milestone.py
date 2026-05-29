# Import all necessary tools for math, environment, and AI
import os
import google.generativeai as genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

def run_embedding_milestone():
    # 1. Initialize the environment and security
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api_key)

    print(" --- MODULE 3: EMBEDDING MILESTONE --- 🚀")

    # 2. Define a small 'Mock PDF Dataset'
    knowledge_base = [
        "The mitochondria is the powerhouse of the cell.",
        "The speed of light is approximately 299,792 kilometers per second.",
        "VS Code is a popular source-code editor made by Microsoft.",
        "RAG stands for Retrieval-Augmented Generation."
    ]

    # 3. User Query (Semantic - uses different words)
    user_query = "What is the primary energy source for cellular activity?"

    try:
        # 4. Convert the entire knowledge base into 768D vectors
        print(" Generating knowledge base embeddings...")
        kb_embeddings = [
            genai.embed_content(model="models/text-embedding-004", content=text)['embedding']
            for text in knowledge_base
        ]

        # 5. Convert the user's query into a vector
        print(" Embedding user query...")
        query_vec = genai.embed_content(model="models/text-embedding-004", content=user_query)['embedding']

        # 6. Calculate semantic similarity scores using scikit-learn
        # We wrap query_vec in [] to make it a 2D array for sklearn
        scores = cosine_similarity([query_vec], kb_embeddings)[0]

        # 7. Find the best match
        best_idx = np.argmax(scores)
        top_score = scores[best_idx]

        # 8. Final Verification Report
        print("\n--- MILESTONE REPORT ---")
        print(f"Top Match: {knowledge_base[best_idx]}")
        print(f"Confidence: {top_score:.4f}")

        # A score > 0.6 usually indicates a solid semantic match
        if top_score > 0.6:
            print("\n VERIFIED: Semantic search is accurate and responsive.")
        else:
            print("\n WARNING: Low similarity score. Check model configuration.")

    except Exception as e:
        print(f" MILESTONE FAILED: {e}")

# Execute the final check
if __name__ == "__main__":
    run_embedding_milestone()
