# Import all the 'Instrument' components we've mastered
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Load the secret API key
load_dotenv()

def run_milestone_pipeline():
    print(" --- STARTING RETRIEVAL MILESTONE PIPELINE ---")

    # 2. Setup Models
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0) # Temp 0 for facts
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # 3. Phase: Data Liquidation (From Module 6)
    loader = PyPDFLoader("docs/textbook.pdf") # Point to your PDF
    docs = loader.load() # Load the pages
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100) # Set the 'Chop'
    chunks = splitter.split_documents(docs) # Liquidation complete
    print(f" PDF Liquidated into {len(chunks)} chunks.")

    # 4. Phase: The Memory Bank (The Database)
    vector_db = FAISS.from_documents(chunks, embeddings) # Store vectors in RAM
    retriever = vector_db.as_retriever(search_kwargs={"k": 3}) # Top 3 relevant chunks
    print(" Vector Database & Retriever Online.")

    # 5. Phase: The Logic (The RAG Prompt)
    template = """You are a professional assistant. Answer based ONLY on the context.
    If the answer isn't there, say you don't know. 
    Context: {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    # 6. THE ORCHESTRATION: The Pipe Symphony
    # We create a function to format our retrieved docs for the prompt
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Building the chain
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    # 7. EXECUTION: The Final Test
    user_query = "What is the most important takeaway from this document?"
    print(f"\n User Question: {user_query}")
    
    # Run the chain
    answer = rag_chain.invoke(user_query)
    
    # 8. THE CITED RESULT
    print(f"\n AI Answer:\n{answer}")
    
    # Manual Source Audit for the milestone
    sources = retriever.invoke(user_query)
    print("\n Verified Sources:")
    for doc in sources:
        print(f"- Page {doc.metadata['page'] + 1}: {doc.metadata['source']}")

try:
    run_milestone_pipeline()
except Exception as e:
    print(f" Pipeline Failure: {e}")
