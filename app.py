import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="AI Memory Lab", layout="wide")
st.title(" Chat with Memory")

# 2. INITIALIZE THE NOTEBOOK: Check if 'messages' exists in our memory
# If not, create an empty list to store our chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. DISPLAY OLD MESSAGES: Every time the script reruns, 
# we loop through our 'Notebook' and draw the bubbles again
for message in st.session_state.messages:
    with st.chat_message(message["role"]): # Look up if it was 'user' or 'assistant'
        st.markdown(message["content"])    # Show what was said

# 4. THE INPUT: Wait for the user to type something
if prompt := st.chat_input("Ask me anything..."):
    
    # 5. WRITE TO NOTEBOOK: Add the user's message to our list
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # 6. SHOW CURRENT MESSAGE: Display the user's bubble immediately
    with st.chat_message("user"):
        st.markdown(prompt)

    # 7. GENERATE RESPONSE: (Simulating AI logic for now)
    response = f"I remembered you said: {prompt}"
    
    # 8. SHOW ASSISTANT BUBBLE: Display the AI's response
    with st.chat_message("assistant"):
        st.markdown(response)
        
    # 9. WRITE RESPONSE TO NOTEBOOK: Save the AI's reply to memory
    st.session_state.messages.append({"role": "assistant", "content": response})
