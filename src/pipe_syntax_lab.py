# Import the 'Runnable' interface - the secret behind the pipe
from langchain_core.runnables import RunnableLambda

# 1. Station 1: The 'Input Cleaner' (A simple function)
def clean_text(input_data):
    # This simulates a prompt template preparing text
    return input_data.strip().upper()

# 2. Station 2: The 'AI Brain' (A simple simulation)
def mock_ai(clean_input):
    # This simulates the LLM receiving text and responding
    return f"AI RESPONSE TO: {clean_input}"

# 3. We wrap our functions in 'RunnableLambda' so they can use the Pipe
# The Pipe (|) ONLY works with objects that follow LangChain's 'Runnable' rules
station_1 = RunnableLambda(clean_text)
station_2 = RunnableLambda(mock_ai)
station_3 =  RunnableLambda(add_completed)
# 4. THE MAGIC: We create the Chain using the Pipe operator
# This tells LangChain: "Take the output of 1 and shove it into 2"
my_first_chain = station_1 | station_2| station_3

print("---  Testing the Pipe (|) Syntax ---")

# 5. We 'invoke' the chain (turn on the conveyor belt)
# We send in messy text to see if the chain cleans and processes it
result = my_first_chain.invoke("   hello world   ")

print(f"Final Output: {result}")
# Expect: "AI RESPONSE TO: HELLO WORLD"
