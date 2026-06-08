# Import os and dotenv for security
import os
from dotenv import load_dotenv
# Import our Gemini model
from langchain_google_genai import ChatGoogleGenerativeAI
# Import the specialized 'Unwrapper' (Output Parser)
from langchain_core.output_parsers import StrOutputParser

# 1. Load your API key
load_dotenv()

# 2. Initialize the AI Brain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Initialize the Output Parser Guard
# This object is a 'Runnable' that knows how to extract text
parser = StrOutputParser()

print("---  The Output Parser Guard Lab ---")

try:
    # 4. First, let's see the 'Raw' response WITHOUT the guard
    # We invoke the LLM directly
    raw_response = llm.invoke("Say 'Hello' in one word.")
    print(f"\n RAW DATA (The Bag): {raw_response}")
    print(f"Type of Raw: {type(raw_response)}")

    # 5. Now, let's use the 'Guard' to unwrap it
    # We can pass the raw response directly into the parser
    clean_text = parser.invoke(raw_response)
    print(f"\n CLEAN TEXT (The Burger): '{clean_text}'")
    print(f"Type of Clean: {type(clean_text)}")

    # 6. Preview of Topic 7: Chaining them together with a Pipe (|)
    # chain = llm | parser
    # result = chain.invoke("Say 'Hello'")

except Exception as e:
    print(f" ERROR: {e}")
