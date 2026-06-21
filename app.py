import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="PDF Chat Room", layout="wide")

# 2. Sidebar (From our previous lesson)
with st.sidebar:
    st.title(" Documents")
    st.file_uploader("Upload PDF", type="pdf")

# 3. THE MAIN CHAT AREA
st.title("PDF Research Room")

# 4. THE BUBBLES: Creating a 'User' bubble
# Using 'with' tells Streamlit: 'Put everything inside this bubble'
with st.chat_message("user"):
    st.write("Hello! Can you help me find information in my PDF?")

# 5. THE BUBBLES: Creating an 'Assistant' bubble
with st.chat_message("assistant"):
    st.write("Of course! Please upload a file and ask away.")

# 6. THE INPUT: This adds the sticky text box at the bottom
# We use the 'walrus operator' (:=) to check if the user typed something
if user_prompt := st.chat_input("Type your question here..."):
    # 7. ECHO: If the user types, show their message in a new bubble
    with st.chat_message("user"):
        st.write(user_prompt)
    
    # 8. RESPONSE: Show a placeholder 'Assistant' response
    with st.chat_message("assistant"):
        st.write(f"I am processing your question: '{user_prompt}'")
