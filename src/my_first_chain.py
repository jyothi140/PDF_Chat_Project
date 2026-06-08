# Import os and dotenv for secret API key handling
import os
from dotenv import load_dotenv
# Import the components for our 'Assembly Line'
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load the 'Secret Vault' (.env)
load_dotenv()

# 2. Station A: Initialize the LLM (The Brewer)
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Station B: Create the Prompt Template (The Grinder)
# We use a placeholder {topic} to make the chain reusable
prompt = ChatPromptTemplate.from_template("Tell me a fun fact about {topic}")

# 4. Station C: Initialize the Output Parser (The Filter)
parser = StrOutputParser()

# 5. THE SYMPHONY: Connect all stations using the Pipe operator (|)
# Data flows from: User Input -> Prompt -> Model -> Parser -> Result
chain = prompt | model | parser

print("---  Running My First LangChain ---")

try:
    # 6. Run the entire chain with a single command
    # We pass the variable 'topic' inside a dictionary
    result = chain.invoke({"topic": "Space Travel"})
    
    # 7. Print the final, cleaned-up response
    print(f"Result: {result}")

except Exception as e:
    # 8. Catch errors like missing API keys or internet issues
    print(f" ERROR: {e}")