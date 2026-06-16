# Import the OS module for file paths
import os
# Import the PDF Loader we mastered in Topic 3
from langchain_community.document_loaders import PyPDFLoader
# Import the Smart Splitter we mastered in Topic 7
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Define the path to our target PDF
file_path = os.path.join("docs", "textbook.pdf")

print(f"---  MILESTONE: Starting Data Liquidation Pipeline ---")

try:
    # 2. STEP 1: LOAD (The Handshake)
    # We initialize the loader with our file path
    loader = PyPDFLoader(file_path)
    # We load the pages into a list of document objects
    raw_pages = loader.load()
    print(f" Phase 1: Loaded {len(raw_pages)} raw pages from PDF.")

    # 3. STEP 2: CONFIGURE (The Smart Chef)
    # We set our industrial standards: 500 char size, 50 char overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", " ", ""]
    )

    # 4. STEP 3: LIQUIDATE (The Chop)
    # We pass the raw pages into the splitter to get our final chunks
    # .split_documents is better than .split_text because it keeps our Metadata!
    final_chunks = text_splitter.split_documents(raw_pages)

    # 5. STEP 4: AUDIT (The Result)
    print(f" Phase 2: Chopped PDF into {len(final_chunks)} optimized chunks.")
    
    # 6. Show the first chunk and its 'Evidence Tag' (Metadata)
    print("\n---  SAMPLE CHUNK AUDIT ---")
    print(f" Content: {final_chunks[0].page_content[:100]}...")
    print(f" Metadata: {final_chunks[0].metadata}")

    print("\n MILESTONE COMPLETE: Your data is liquidated and ready for the Vector Bank!")

except Exception as e:
    # 7. Catch-all for any pipeline breaks
    print(f" MILESTONE FAILED: {e}")
