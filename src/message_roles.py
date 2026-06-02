# Import the secure vault tools
import os
from dotenv import load_dotenv
# Import the specialized message roles from LangChain
from langchain_core.messages import SystemMessage, HumanMessage
# Import our Google Gemini connection
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load your API key from the .env file
load_dotenv()

# 2. Initialize the Gemini brain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 3. Create the Director's Briefing (System Message)
# This establishes the Persona and the Rules
system_instruction = SystemMessage(
    content="You are a simplified science teacher. Explain everything like I am 10 years old."
)

# 4. Create the User's Question (Human Message)
# This is the actual task or question
user_input = HumanMessage(
    content="What is a Large Language Model?"
)

# 5. Bundle them into a list (The conversation history)
# LangChain chat models expect a list of messages
messages = [system_instruction, user_input]

print("---  Persona Test: Science Teacher ---")

try:
    # 6. Send the whole 'Script' to the AI
    # This proves the AI follows the 'System' role while answering the 'Human'
    response = llm.invoke(messages)
    
    # 7. Print the AI's response (which is an AIMessage object)
    print(f"Teacher AI says:\n{response.content}")

except Exception as e:
    print(f" ERROR: {e}")