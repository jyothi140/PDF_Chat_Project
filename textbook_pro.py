import streamlit as st # The UI library
from langchain_community.document_loaders import PyPDFLoader # Loads the PDF
from langchain_text_splitters import RecursiveCharacterTextSplitter # Chunks the text
from langchain_community.vectorstores import FAISS # The database
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings # The AI & Embeddings
from langchain_core.prompts import ChatPromptTemplate # The rules
from langchain_core.runnables import RunnablePassthrough # The data mover
from langchain_core.output_parsers import StrOutputParser # The text cleaner
import os # For system paths
from dotenv import load_dotenv # To load your API key
import tempfile # To safely handle uploaded files

# 1. Load your secret API Key
load_dotenv()

# 2. Page Identity
st.set_page_config(page_title="Textbook AI Pro", layout="wide", page_icon="📚")
st.title(" Textbook AI Pro")

# 3. Sidebar Setup
with st.sidebar:
    st.title(" Control Center")
    uploaded_file = st.file_uploader("Upload your PDF textbook", type="pdf")
    st.divider()
    if st.button("Clear Chat"):
        st.session_state.messages = [] # Reset memory
        st.rerun()

# 4. Initialize AI Brain
@st.cache_resource
def get_ai_tools():
    # Setup LLM and Embeddings once
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    return llm, embeddings

llm, embeddings = get_ai_tools()

# 5. Process PDF and Build Vector Store
@st.cache_resource
def process_pdf(file_bytes):
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes.getvalue())
        tmp_path = tmp.name
    
    # Load and Chunk the PDF
    loader = PyPDFLoader(tmp_path)
    data = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_documents(data)
    
    # Build FAISS database
    vector_db = FAISS.from_documents(chunks, embeddings)
    return vector_db.as_retriever()

# 6. Session State (The Notebook)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 7. MAIN LOGIC: If a file is uploaded, start the engine!
if uploaded_file:
    # Build the 'Forklift' (Retriever)
    retriever = process_pdf(uploaded_file)
    st.sidebar.success("✅ Textbook Analyzed!")

    # Display History
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Handle User Question
    if prompt := st.chat_input("Ask a question about the textbook..."):
        # Store and show User message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Build RAG Chain
        template = """Answer based ONLY on the context: {context}\nQuestion: {question}"""
        rag_prompt = ChatPromptTemplate.from_template(template)
        
        chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | rag_prompt | llm | StrOutputParser()
        )

        # Generate Response
        with st.chat_message("assistant"):
            response = chain.invoke(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
else:
    st.info(" Please upload a PDF in the sidebar to begin our study session.")
