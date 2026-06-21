# Import Streamlit for the UI
import streamlit as st
# Import your RAG components (Ensure you have these from Module 7)
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# 1. Load API Keys from your .env file
load_dotenv()

# 2. Setup Page Config
st.set_page_config(page_title="PDF AI Architect", layout="wide")
st.title("Integrated PDF Chat")

# 3. INITIALIZE MODELS: Create the AI brain and the translator
# We use @st.cache_resource so the AI doesn't reload every time you click a button
@st.cache_resource
def load_llm():
    # Initialize the Gemini model
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    # Initialize the Embedding model
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return model, embeddings

model, embeddings = load_llm()

# 4. SIMULATED DATABASE: (In the final milestone, we'll use your uploaded PDF)
# For this bridge test, we use a fixed 'Brain'
vector_db = FAISS.from_texts(["The project deadline is January 20th."], embeddings)
retriever = vector_db.as_retriever()

# 5. SESSION STATE: The Chat History 'Notebook'
if "messages" not in st.session_state:
    st.session_state.messages = []

# 6. DISPLAY HISTORY: Draw old messages on the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. THE BRIDGE: Connect the Chat Input to the RAG Logic
if prompt := st.chat_input("Ask a question about the PDF..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Trigger the RAG Chain
    with st.chat_message("assistant"):
        # Create the prompt template
        template = "Answer based on context: {context}\nQuestion: {question}"
        prompt_template = ChatPromptTemplate.from_template(template)
        
        # Build the chain (The Bridge)
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | model
            | StrOutputParser()
        )
        
        # Run the chain and display the 'Generated' response
        response = chain.invoke(prompt)
        st.markdown(response)
        
        # Save response to history
        st.session_state.messages.append({"role": "assistant", "content": response})
