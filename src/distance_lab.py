# Import os and dotenv for our API key
import os
import google.generativeai as genai
import numpy as np # Import NumPy for the distance calculation
from dotenv import load_dotenv

# 1. Setup our AI connection
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Define a helper function for Euclidean Distance
def calculate_euclidean(v1, v2):
    # This uses the 'L2 Norm' of the difference between vectors
    # Mathematically: sqrt(sum((v1 - v2)^2))
    return np.linalg.norm(np.array(v1) - np.array(v2))

# 3. Two sentences that are almost identical
text_a = "The dog is in the park."
text_b = "The canine is at the park."

try:
    # 4. Generate the embeddings (768 numbers each)
    vec_a = genai.embed_content(model="models/text-embedding-004", content=text_a)['embedding']
    vec_b = genai.embed_content(model="models/text-embedding-004", content=text_b)['embedding']

    # 5. Calculate the distance
    dist = calculate_euclidean(vec_a, vec_b)

    print("---  Measuring Space (Euclidean Distance) ---")
    print(f"Sentence A: {text_a}")
    print(f"Sentence B: {text_b}")
    print(f"Straight-Line Distance: {dist:.4f}")
    
    # 6. Interpret the result
    if dist < 0.6: # Generally, for this model, < 0.6 is very close
        print(" RESULT: These points are very close in space!")
    else:
        print(" RESULT: These points are far apart.")

except Exception as e:
    print(f" ERROR: {e}")