# Import the splitter tool from the LangChain text splitters library
from langchain_text_splitters import CharacterTextSplitter

# 1. A sample sentence that we want to keep together
raw_text = "The secret ingredient to a great RAG system is a healthy amount of overlap."

print("---  The Overlap Safety Net ---")

# 2. Initialize the Splitter with Overlap
# chunk_size=30: Make the chunks small so we can see the cut
# chunk_overlap=15: Repeat 15 characters from the end of Chunk 1 at the start of Chunk 2
splitter = CharacterTextSplitter(
    separator="", 
    chunk_size=30, 
    chunk_overlap=15
)

# 3. Perform the split
chunks = splitter.split_text(raw_text)

# 4. Print the chunks to see the 'Shared' text
for i, chunk in enumerate(chunks):
    # repr() helps us see the exact string including spaces
    print(f"Chunk {i+1}: {repr(chunk)}")

print("\n OBSERVATION: Look at the end of Chunk 1 and the start of Chunk 2.")
print("The 'Baton' (text) was passed successfully!")
