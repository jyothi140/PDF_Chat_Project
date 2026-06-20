# Import the FAISS class to create a temporary database
from langchain_community.vectorstores import FAISS
# Import Google Generative AI Embeddings to turn text into math
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# Import load_dotenv to read our API Key
from dotenv import load_dotenv
import os

# 1. Load the 'Secret Vault' (.env)
load_dotenv()

# 2. Setup our Embeddings model (The 'Translator')
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 3. Create a small list of 'PDF Chunks' to act as our data
texts = [
    "The CPU is the central processing unit of a computer.",
    "Photosynthesis is how plants turn sunlight into energy.",
    "The Great Wall of China is visible from some satellite orbits.",
    "Python is a popular programming language for data science."
]

print("---  Building the Retriever Object ---")

try:
    # 4. Create a temporary FAISS database from our texts
    # This turns the strings into vectors and stores them in RAM
    vector_db = FAISS.from_texts(texts, embeddings)

    # 5. THE MAGIC STEP: Convert the Database into a 'Retriever'
    # search_kwargs={"k": 2} tells the retriever to find the TOP 2 most relevant chunks
    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    # 6. Test the Retriever with a 'Human' question
    question = "How do plants get energy?"
    
    # 7. Ask the Retriever to go fetch the relevant 'hay'
    # This returns a list of LangChain 'Document' objects
    docs = retriever.invoke(question)

    print(f" Question: {question}")
    print(f" Retriever found {len(docs)} relevant documents:")
    
    # 8. Loop through and print what the 'Forklift' brought back
    for i, doc in enumerate(docs):
        print(f" Chunk {i+1}: {doc.page_content}")

except Exception as e:
    # 9. Catch errors like missing API keys
    print(f" ERROR: Retriever failed. {e}")


