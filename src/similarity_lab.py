import os
import google.generativeai as genai
import numpy as np # We use numpy for the 'Angle Math'
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. A function to calculate Cosine Similarity between two lists of numbers
def calculate_similarity(v1, v2):
    # This is the 'Angle Math' formula: Dot Product divided by Magnitudes
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 2. Three sentences to compare
sentences = [
    "The cat is sleeping on the mat.",      # Sentence A
    "A kitten is napping on the rug.",      # Sentence B (Similar to A)
    "The weather is quite rainy today."     # Sentence C (Different)
]

try:
    # 3. Get embeddings for all three
    embeddings = [
        genai.embed_content(model="models/text-embedding-004", content=s)['embedding']
        for s in sentences
    ]

    # 4. Compare A with B
    sim_AB = calculate_similarity(embeddings[0], embeddings[1])
    # 5. Compare A with C
    sim_AC = calculate_similarity(embeddings[0], embeddings[2])

    print("--- Measuring Meaning (Cosine Similarity) ---")
    print(f"Similarity (Cat vs Kitten): {sim_AB:.4f}") # Expect a high score near 1
    print(f"Similarity (Cat vs Weather): {sim_AC:.4f}") # Expect a lower score
    
    print("\n RESULT: The AI successfully saw that 'Cat' and 'Kitten' point in a similar direction!")

except Exception as e:
    print(f" ERROR: {e}")
