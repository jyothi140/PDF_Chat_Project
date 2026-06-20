# 1. We'll use a simple list to simulate our 'Retrieved PDF Data'
# In the real app, this comes from your FAISS vector database
retrieved_context = "The capital of France is Paris. It is known for the Eiffel Tower."

# 2. This is the user's actual question
user_query = "What is the capital of France?"

print("---  The RAG Blueprint Lab ---")

# 3. THE RAG PROMPT: This is the 'Secret Sauce'
# We 'Augment' the prompt by injecting the context and the question together
rag_prompt = f"""
You are a helpful assistant. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 

Context: {retrieved_context}

Question: {user_query}

Answer:
"""

# 4. In a real RAG pipeline, we would now 'Pipe' this to the LLM
# For this blueprint, we are going to print the final instruction 
# to see exactly what the LLM 'sees' behind the scenes.
print(" [STEP 1: RETRIEVE] Found relevant context in PDF...")
print(" [STEP 2: AUGMENT] Combining context with user query...")
print("\n--- FINAL PROMPT SENT TO AI ---")
print(rag_prompt)

# 5. This is what 'Generation' looks like
print(" [STEP 3: GENERATE] AI reads the context and provides the fact-based answer.")

