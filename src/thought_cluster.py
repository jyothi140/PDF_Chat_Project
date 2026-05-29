# Import os for keys and genai for our embeddings
import os
import google.generativeai as genai
import numpy as np
# Import the KMeans clustering tool from scikit-learn
from sklearn.cluster import KMeans
from dotenv import load_dotenv

# 1. Setup our secret vault and AI connection
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. A mini 'textbook' with two clear topics: Fruit and Coding
sentences = [
    "Apples are a great source of fiber.",
    "Bananas contain high levels of potassium.",
    "Python is a versatile programming language.",
    "Java is used for building enterprise apps.",
    "Oranges are famous for Vitamin C.",
    "C++ is a powerful language for systems."
]

print("---  Clustering Your Thoughts ---")

try:
    # 3. Convert all 6 sentences into 768-dimensional vectors
    embeddings = [
        genai.embed_content(model="models/text-embedding-004", content=s)['embedding']
        for s in sentences
    ]
    matrix = np.array(embeddings)

    # 4. Tell the AI to find 2 distinct 'piles' (clusters)
    # n_clusters=2 because we know we have Fruit and Code topics
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    
    # 5. The AI 'learns' the patterns and assigns a label (0 or 1) to each sentence
    kmeans.fit(matrix)
    labels = kmeans.labels_

    # 6. Print the results to see if the AI grouped them correctly
    for i, sentence in enumerate(sentences):
        # The AI doesn't know the names 'Fruit' or 'Code', just Group 0 or 1
        print(f"Group {labels[i]} | Sentence: {sentence}")

    print("\n SUCCESS: The AI automatically sorted your textbook into topics!")

except Exception as e:
    print(f" ERROR: {e}")

