# Import 'os' to read the API key and 'genai' to talk to Google
import os
import google.generativeai as genai
# Import 'load_dotenv' to open our secret vault
from dotenv import load_dotenv

# 1. Load the secrets from your .env file
load_dotenv()

# 2. Grab the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")

# 3. Configure the AI library to use your secret key
genai.configure(api_key=api_key)

# 4. Initialize the 'Gemini' model (the brain)
# We use 'gemini-1.5-flash' because it is fast and efficient
model = genai.GenerativeModel('gemini-1.5-flash')

print("--- Sending First API Call ---")

try:
    # 5. Send a simple 'Hello' message to the AI
    response = model.generate_content("Hello AI! I am building a Chat with PDF app. Say hi back!")
    
    # 6. Print the text that the AI sent back
    print(f"AI Response: {response.text}")
    print("\nSUCCESS: Your connection to the LLM is LIVE!")

except Exception as e:
    # 7. If something goes wrong, print the error clearly
    print(f"ERROR: Connection failed. {e}")

