# Import the OS and Dotenv for our API Key
import os
from dotenv import load_dotenv
# Import our PDF Loader and Smart Splitter from Module 6
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Import FAISS and Google Embeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 1. Load your secret API Key
load_dotenv()

# 2. Setup the 'Librarian's Tools' (Embeddings)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

print("---  Similarity Search Health Check ---")

try:
    # 3. Load and Split your PDF (The 'Liquidation' from Module 6)
    loader = PyPDFLoader("docs/handshake_sample.pdf")
    pages = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)

    # 4. Create a temporary 'Memory Bank' (Vector Store) in RAM
    # This turns your PDF chunks into searchable math vectors
    vector_db = FAISS.from_documents(chunks, embeddings)

    # 5. THE TEST: Define a query based on your PDF content
    query = "What is the main subject of this document?"

    # 6. Perform a raw Similarity Search
    # k=2 means 'Fetch the top 2 closest matches'
    results = vector_db.similarity_search(query, k=2)

    print(f" Query: {query}")
    print(f" Found {len(results)} relevant chunks in the PDF.\n")

    # 7. Print the results to verify the 'Forklift' found the right data
    for i, res in enumerate(results):
        print(f" MATCH {i+1} (Page {res.metadata['page'] + 1}):")
        print(f"{res.page_content[:200]}...") # Print first 200 characters
        print("-" * 30)

except Exception as e:
    print(f" TEST FAILED: {e}")
