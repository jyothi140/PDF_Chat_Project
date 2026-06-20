# Import os and load_dotenv to use our API Key
import os
from dotenv import load_dotenv
# Import the Gemini Chat model from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load the environment variables from .env
load_dotenv()

# 2. Initialize the Gemini Model (The 'Brain')
# We need this to access the model's specific tokenizer
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Create a test string with simple and complex words
sample_text = "Learning AI is fantastic! Photosynthesis is complex."

print(f"---  Token vs. Character Audit ---")
print(f"Text: '{sample_text}'")

try:
    # 4. Count the Characters (The 'Human' way)
    char_count = len(sample_text)
    
    # 5. Count the Tokens (The 'AI' way)
    # This sends the text to the Gemini local tokenizer to get an exact count
    token_count = llm.get_num_tokens(sample_text)

    # 6. Display the comparison
    print(f" Character Count: {char_count}")
    print(f" Token Count: {token_count}")
    print(f" Ratio: ~{char_count/token_count:.2f} characters per token")

except Exception as e:
    # 7. Catch errors if the API key is missing or model fails
    print(f" ERROR: Could not count tokens. {e}")
