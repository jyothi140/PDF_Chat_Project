# Import the specialized template tool from LangChain
from langchain_core.prompts import ChatPromptTemplate

# 1. Create the 'Mad-Libs' style template
# We use curly braces {} to mark the 'blank spaces'
template = "You are a professional tutor. Explain the concept of {topic} in exactly two sentences."

# 2. Initialize the Prompt Template object
# This tells LangChain to prepare the 'Topic' variable for later
prompt_template = ChatPromptTemplate.from_template(template)

print("--- The Prompt Template Lab ---")

# 3. Simulate a user wanting to learn about 'Photosynthesis'
# We use .format_messages to fill in the blanks
formatted_prompt = prompt_template.format_messages(topic="Photosynthesis")

# 4. Print the result to see how LangChain filled the blanks
# In a real chain, this output would 'pipe' directly into the AI
print(f"Final Prompt to AI:\n{formatted_prompt[0].content}")

# 5. Let's try it again with a different topic to show it's dynamic
second_prompt = prompt_template.format_messages(topic="Quantum Physics")
print(f"\nSecond Dynamic Prompt:\n{second_prompt[0].content}")

print("\nSUCCESS: The template is dynamically filling the blanks!")
