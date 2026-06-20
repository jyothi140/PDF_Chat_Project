# Import necessary libraries for environment and AI logic
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# 1. Load the secret API key from your .env file
load_dotenv()

# 2. Setup the Embeddings model (The 'Meaning-Translator')
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 3. Create a simulated 'PDF Database' with Metadata (Page Numbers)
# In a real app, this is created by your PDF Loader from Module 6
mock_docs = [
    Document(page_content="The company was founded in 1999.", metadata={"source": "manual.pdf", "page": 1}),
    Document(page_content="Our headquarters are in San Francisco.", metadata={"source": "manual.pdf", "page": 5}),
    Document(page_content="The CEO is Jane Doe.", metadata={"source": "manual.pdf", "page": 12})
]

print("---  Source Attribution Audit ---")

try:
    # 4. Initialize the Vector Store with our mock documents
    vector_db = FAISS.from_documents(mock_docs, embeddings)
    
    # 5. Define a query to find specific information
    query = "Where is the company located?"
    
    # 6. Perform a Similarity Search that returns the full Document object
    # This includes both the text (page_content) and the tags (metadata)
    results = vector_db.similarity_search(query, k=1)

    if results:
        # 7. Extract the answer and the 'Footnote'
        found_text = results[0].page_content
        found_page = results[0].metadata.get("page")
        found_source = results[0].metadata.get("source")

        # 8. Print the 'Verified' response
        print(f" AI Answer: {found_text}")
        print(f" Source: {found_source}")
        print(f" Found on Page: {found_page}")
    else:
        print(" No relevant source found.")

except Exception as e:
    # 9. Catch errors like API connection issues
    print(f" Audit Error: {e}")
