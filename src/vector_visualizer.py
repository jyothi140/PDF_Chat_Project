# Import os for API keys and genai for embeddings
import os
import google.generativeai as genai
import numpy as np
# Import PCA from scikit-learn (The 'Squasher')
from sklearn.decomposition import PCA
from dotenv import load_dotenv

# 1. Load the secret API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Sentences from two different "worlds" (Tech vs. Nature)
data = [
    "The software update fixed the bug.",
    "Python is great for coding.",
    "The forest is full of green trees.",
    "Flowers bloom in the spring."
]

print("---  The Vector Visualizer ---")

try:
    # 3. Create high-dimensional embeddings (768D)
    embeddings = [
        genai.embed_content(model="models/text-embedding-004", content=text)['embedding']
        for text in data
    ]

    # 4. Initialize PCA to squash 768 dimensions down to 2
    pca = PCA(n_components=2)
    
    # 5. Perform the "Squash" (Fit and Transform)
    # We convert the list to a NumPy array first
    reduced_vectors = pca.fit_transform(np.array(embeddings))

    # 6. Print the results as simple X, Y coordinates
    for i, text in enumerate(data):
        x = reduced_vectors[i][0]
        y = reduced_vectors[i][1]
        print(f"Sentence: {text[:30]}...")
        print(f"   -> 2D Coordinates: X={x:.2f}, Y={y:.2f}\n")

    print(" SUCCESS: 768D squashed to 2D. Similar sentences will have similar X/Y values!")

except Exception as e:
    print(f" ERROR: {e}")
