import os
from dotenv import load_dotenv
from google import genai

def run_final_milestone():
    print("--- MODULE 2: CONNECTIVITY MILESTONE --- 🚀")

    # Check .env exists
    if not os.path.exists(".env"):
        print("SECURITY ERROR: .env file not found!")
        return

    # Load API key
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("CONFIG ERROR: GOOGLE_API_KEY missing!")
        return

    print(f" SECURITY: Secret key loaded (Starts with: {api_key[:4]}...)")

    try:
        # Configure Gemini client
        client = genai.Client(api_key=api_key)

        print(" Attempting Handshake with Gemini...")

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="Confirm system status: Are you online and ready?"
        )

        print(" CONNECTION: LLM responded successfully!")
        print(f"AI MESSAGE: {response.text}")

        print("\nMILESTONE REACHED: Your AI Command Center is fully operational!")

    except Exception as e:
        print(f"CONNECTION FAILED: {e}")

if __name__ == "__main__":
    run_final_milestone()