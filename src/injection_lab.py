# Import tools to load our keys and build our chain
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 1. Load the secret API key
load_dotenv()

# 2. Setup our Brain and our 'Meaning-Translator' (Embeddings)
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 3. Create a tiny 'Simulated PDF' database
texts = ["The secret code to the vault is 12345.", "The vault is located in the basement."]
vector_db = FAISS.from_texts(texts, embeddings)
retriever = vector_db.as_retriever()

# 4. Create a specialized RAG prompt
template = """Answer based on this context: {context}
Question: {question}"""
prompt = ChatPromptTemplate.from_template(template)

print("---  Context Injection Lab: Debugging Mode ---")

try:
    # 5. STEP 1: See what the Retriever finds (The 'Photo' we are handing over)
    user_query = "What is the secret code?"
    retrieved_docs = retriever.invoke(user_query)
    
    # Extract just the text from the documents
    context_text = "\n".join([doc.page_content for doc in retrieved_docs])
    
    print(f"\n INJECTED CONTEXT FOUND:")
    print(f"--------------------------------")
    print(context_text)
    print(f"--------------------------------")

    # 6. STEP 2: See the FINAL PROMPT (The 'Full Briefing' for the AI)
    # This combines the instructions, the context, and the question
    final_combined_prompt = prompt.format(context=context_text, question=user_query)
    
    print(f"\n FINAL PROMPT SENT TO AI'S BRAIN:")
    print(final_combined_prompt)

    # 7. STEP 3: Get the actual answer
    response = model.invoke(final_combined_prompt)
    print(f"\n AI ANSWER: {response.content}")

except Exception as e:
    print(f" Lab Error: {e}")
