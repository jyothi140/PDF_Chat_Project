# Import the 'Smart Chef' from the LangChain text splitters library
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Sample text with paragraphs and sentences
# We want the AI to keep these ideas together as much as possible
raw_text = """
The CPU is the heart of the computer. It executes instructions.

Python is a high-level language. It is known for its readability.
This makes it great for Artificial Intelligence projects.
"""

print("---  The Smart Chop: Recursive Splitting ---")

# 2. Initialize the Smart Splitter
# chunk_size=50: A very small size to force it to look for breaks
# chunk_overlap=10: A small safety net
# separators: The list of characters it tries IN ORDER (\n\n, \n, " ", "")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10,
    separators=["\n\n", "\n", " ", ""] 
)

# 3. Perform the 'Smart Chop'
# This returns a list of text chunks
chunks = splitter.split_text(raw_text)

# 4. Print the results to see the hierarchy in action
for i, chunk in enumerate(chunks):
    # We use repr() to see hidden newline characters like \n
    print(f"Chunk {i+1} ({len(chunk)} chars): {repr(chunk)}")

print("\n OBSERVATION: Notice how the sentences usually stay whole!")

