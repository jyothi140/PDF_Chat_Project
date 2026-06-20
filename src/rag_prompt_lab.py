# Import the specialized Prompt Template from LangChain
from langchain_core.prompts import ChatPromptTemplate

# 1. Define the System Instruction (The 'Legal Contract')
# We use {context} and {question} as placeholders for our data
system_instructions = """
You are a helpful assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If the answer is not in the context, say 'I am sorry, but the PDF does not contain that information.' 
Do not make up an answer.

Context:
{context}
"""

# 2. Define the User Question format
user_input = "{question}"

print("---  RAG Prompt Engineering Lab ---")

try:
    # 3. Create the 'ChatPromptTemplate'
    # This combines the 'System' rules and the 'User' task
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_instructions),
        ("human", user_input),
    ])

    # 4. SIMULATION: Let's see what the prompt looks like when filled
    # Imagine these variables were pulled from your PDF and User
    sample_context = "The company's mission is to accelerate the world's transition to sustainable energy."
    sample_question = "What is the company's mission?"

    # 5. Format the prompt (Fill in the blanks)
    final_prompt = prompt_template.format(
        context=sample_context, 
        question=sample_question
    )

    # 6. Print the result to see what the AI 'hears'
    print("\n[AI'S SECRET INSTRUCTIONS]:")
    print(final_prompt)
    print("\n PROMPT READY: Your AI now has a strict boundary!")

except Exception as e:
    print(f" ERROR: Prompt creation failed. {e}")