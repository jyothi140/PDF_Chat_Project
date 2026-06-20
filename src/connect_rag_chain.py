# Import necessary tools for our environment and AI
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Load your API key from the secret .env file
load_dotenv()

# 2. Setup the Brain (LLM) and the Translator (Embeddings)
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 3. Create a mini-database (Simulating our PDF content)
vector_db = FAISS.from_texts(
    ["The solar system has eight planets.", "Jupiter is the largest planet."],
    embeddings
)
# Turn the database into a 'Retriever' (The Librarian)
retriever = vector_db.as_retriever()

# 4. Create the RAG Prompt (The Instructions)
template = """Answer the question based ONLY on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 5. THE PIPE SYMPHONY: Connecting the pieces
# RunnablePassthrough() helps pass the user's question to the prompt and retriever simultaneously
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)

print("--- ⛓️ RAG Chain: System Online ---")

try:
    # 6. Run the entire chain with one single question
    question = "How many planets are in the solar system?"
    response = rag_chain.invoke(question)
    
    # 7. Print the final result
    print(f"User: {question}")
    print(f"AI: {response}")

except Exception as e:
    # 8. Catch any errors in the pipeline
    print(f" Chain Error: {e}")

