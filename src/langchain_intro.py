# We import the core 'HumanMessage' to see how LangChain structures data
from langchain_core.messages import HumanMessage
# We import a simple tool to check our LangChain version
import langchain

# 1. Start the 'Architect' audit
print("---  LangChain Architecture Audit ---")

# 2. Check which version of the Lego set we are using
# Professional developers always check versions to ensure compatibility
version = langchain.__version__
print(f" Framework Detected: LangChain version {version}")

# 3. Create a 'Message Object' - the basic building block of a chain
# In LangChain, we don't just send strings; we send objects that have 'roles'
test_message = HumanMessage(content="Hello Architect!")

# 4. Verify the object is structured correctly for the 'Symphony'
if test_message.content == "Hello Architect!":
    print(" Objects: LangChain Message blocks are snapping together perfectly.")
    print(f"Message Role: {test_message.type}") # This will show 'human'
else:
    print(" Error: Architecture blocks are misaligned.")

print("\nNote: In the next lesson, we will install the full 'Conductor' toolkit!")
