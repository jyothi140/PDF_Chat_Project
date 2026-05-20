# Import necessary tools for environment and AI
import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

def run_final_milestone():
    print(" --- MODULE 2: CONNECTIVITY MILESTONE --- 🚀")

    # 1. Check if the secret vault (.env) exists
    if not os.path.exists(".env"):
        print(" SECURITY ERROR: .env file not found!")
        return

    # 2. Load secrets and verify the API Key exists
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("CONFIG ERROR: GOOGLE_API_KEY is missing from .env!")
        return
    else:
        print(f"SECURITY: Secret key loaded (Starts with: {api_key[:4]}...)")

    # 3. Configure the AI with a strict 'Low Temperature' (Factual) setting
    genai.configure(api_key=api_key)
    config = {"temperature": 0.1, "max_output_tokens": 50}
    model = genai.GenerativeModel('gemini-1.5-flash', generation_config=config)

    # 4. Perform the 'Live Handshake'
    print(" Attempting Handshake with Gemini...")
    try:
        # We ask a specific question to verify factual response
        response = model.generate_content("Confirm system status: Are you online and ready?")
        print(f" CONNECTION: LLM responded successfully!")
        print(f"AI MESSAGE: {response.text.strip()}")
        print("\n MILESTONE REACHED: Your AI Command Center is fully operational!")
    except Exception as e:
        print(f"CONNECTION FAILED: {e}")

# Run the milestone check
if __name__ == "__main__":
    run_final_milestone()