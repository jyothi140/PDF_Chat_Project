# Import the standard environment and LangChain tools
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load your secret API key
load_dotenv()

# 2. Initialize the AI Brain (The Conductor)
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Create a template with TWO variables: {subject} and {tone}
# Note: You can add as many as you want!
template = """
You are a helpful assistant. 
Explain the following subject: {subject}
Use a {tone} tone.
Keep the explanation under 3 sentences.
"""

# 4. Turn the string into a LangChain Prompt Template
prompt_template = ChatPromptTemplate.from_template(template)

# 5. Build the Chain (Prompt -> Model -> Parser)
# The pipe (|) connects the fl
parser = StrOutputParser()
chain = prompt_template | model | parser
print("---  The Mad-Libs Challenge: Multiple Inputs ---")

try:
    # 6. THE KEY STEP: Pass a dictionary with BOTH variables
    # The keys in the dictionary MUST match the names inside the {}
    user_inputs = {
        "subject": "Black Holes",
        "tone": "funny and pirate-like"
    }
    
    # 7. Invoke the chain with the dictionary
    result = chain.invoke(user_inputs)
    
    print(f"AI Response:\n{result}")

except Exception as e:
    print(f" ERROR: {e}")