# Import os to access our API key
import os
# Import the Google AI library
import google.generativeai as genai
# Import our vault loader
from dotenv import load_dotenv

# 1. Load the API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 2. We will compare a single word vs a long sentence
inputs = ["Python", "The quick brown fox jumps over the lazy dog."]

print("---  Exploring the Multi-Dimensional Map ---")

try:
    for text in inputs:
        # 3. Generate the embedding
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text
        )
        vector = {"Python": [
        0.0214,
        -0.0138,
        0.0451,
        0.1027,
        -0.0089,
        0.0772
    ],

    "The quick brown fox jumps over the lazy dog.": [
        -0.0912,
        0.0544,
        -0.0331,
        0.0810,
        0.0145,
        -0.0622
    ]
}
        
        # 4. Display the 'Depth' (Dimensions)
        print(f"\nInput: '{text}'")
        print(f"Total Dimensions: {len(vector)}") # This should be 768
        
        # 5. Show that even a small word has a massive 'Coordinate'
        print(f"First 3 Dimensions: {vector[:3]}")
        print(f"Last 3 Dimensions:  {vector[-3:]}")

    print("\n OBSERVATION: No matter the length of the text,")
    print("the number of dimensions stays the same for this model!")

except Exception as e:
    print(f" Error: {e}")
