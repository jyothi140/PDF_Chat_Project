# Import the 'os' module to check our secret environment variables
import os
# Import the specialized 'Gemini' connector from our new toolkit
from langchain_google_genai import ChatGoogleGenerativeAI
# Import the 'load_dotenv' tool we set up in Module 2
from dotenv import load_dotenv

# 1. Tell the code to go into the 'vault' (.env) and load the keys
load_dotenv()

# 2. Grab the API key to make sure it exists
api_key = os.getenv("GOOGLE_API_KEY")

print("---  LangChain Toolkit Audit ---")

try:
    # 3. Initialize the 'Conductor' object (ChatGoogleGenerativeAI)
    # This proves the 'langchain-google-genai' library is working
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    
    # 4. Success message if the object was created without crashing
    print(" SUCCESS: LangChain-Google-Genai toolkit is active.")
    print(f" Model Assigned: {llm.model}")
    
    if api_key:
        print("Environment: API Key detected and ready for orchestration.")
    else:
        print("Warning: API Key missing from .env - Toolkit is installed but 'offline'.")

except Exception as e:
    # 5. Catch any errors if the library wasn't installed correctly
    print(f" ERROR: Toolkit check failed. {e}")
