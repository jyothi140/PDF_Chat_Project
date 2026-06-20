# Import the tools to build our chain
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Load the secret API key
load_dotenv()

# 2. Setup our Brain and our 'Translator'
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 3. Create a tiny database with VERY limited info
texts = ["The office is open from 9 AM to 5 PM, Monday to Friday."]
vector_db = FAISS.from_texts(texts, embeddings)
retriever = vector_db.as_retriever()

# 4. THE GUARDRAIL PROMPT: The most important part!
# We explicitly tell the AI what to do if the context is missing info.
template = """You are a strict office assistant. 
Use ONLY the following context to answer the question. 
If the answer is NOT in the context, exactly say: 'I am sorry, but that information is not in the office manual.'
Do not use your own knowledge.

Context: {context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 5. Connect the Chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

print("---  Hallucination Guardrail Lab ---")

try:
    # 6. TEST: Ask a question that IS in the context
    print("\nTest 1: Valid Question...")
    print("AI:", chain.invoke("What are the office hours?"))
 # 7. TEST: Ask a question that IS NOT in the context (The Trick)
    print("\nTest 2: Out-of-Context Question...")
    print("AI:", chain.invoke("What is the office address?"))

except Exception as e:
    print(f" Error: {e}")
