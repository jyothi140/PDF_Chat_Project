# Import the OS and Dotenv for security
import os
from dotenv import load_dotenv
# Import the Gemini model from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load your secret API key
load_dotenv()

# 2. Initialize the Gemini brain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Create a long piece of text (Simulating a part of a PDF)
# In AI, we don't count words; we count 'Tokens' (word pieces)
long_text = "The quick brown fox jumps over the lazy dog. " * 50 

print("---  Memory Limit Audit ---")

try:
    # 4. Ask the LLM to calculate the 'Tokens' for this text
    # This is like the Doctor checking if the pages will fit on the desk
    token_count = llm.get_num_tokens(long_text)
    
    # 5. Report the findings
    print(f"Text length: {len(long_text)} characters")
    print(f"Token count: {token_count} tokens")
    
    # 6. Compare to the typical 'Desk Size'
    # Gemini 1.5 Flash has a massive desk (1 million tokens), 
    # but older models like GPT-3.5 only had 4,000!
    if token_count < 1000000:
        print(" STATUS: This chunk fits on the Gemini 'Desk'.")
    else:
        print(" STATUS: Memory Overflow! You must chop this PDF into pieces.")

except Exception as e:
    print(f" ERROR: {e}")