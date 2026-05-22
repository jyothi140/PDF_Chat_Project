# Import os to get our API key and genai to talk to the embedding model
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load your secret API key from the .env file
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. Define two sentences to compare
text_1 = "I love training AI models."
text_2 = "Machine learning is my favorite hobby."

print("---  Generating Embedding Vectors ---")

try:
    # 3. Use Gemini's embedding model to turn text into numbers
    # 'models/text-embedding-004' is a specialized model just for math
    result_1 = genai.embed_content(model="models/text-embedding-001", content=text_1)
    result_2 = genai.embed_content(model="models/text-embedding-001", content=text_2)

    # 4. Extract the actual list of numbers (the vector)
    vector_1 = result_1['embedding']
    
    # 5. Show the student what a 'coordinate' looks like
    print(f"Sentence: '{text_1}'")
    print(f"Vector Length: {len(vector_1)} numbers")
    print(f"First 5 numbers of the coordinate: {vector_1[:5]}")
    
    print("\nSUCCESS: You have turned human language into computer math!")

except Exception as e:
    print(f" ERROR: {e}")
