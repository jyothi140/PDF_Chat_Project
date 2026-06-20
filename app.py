# Import the Streamlit library to build our web interface
import streamlit as st

# 1. Set the page configuration (The text that appears on the browser tab)
st.set_page_config(page_title="PDF Chat Bot", page_icon="")

# 2. Create a Header (The main title on the screen)
st.title(" Chat with your PDF")

# 3. Create a Subheader (A smaller description)
st.subheader("Turn your textbooks into an interactive conversation.")

# 4. Add some simple text to the screen
st.write("Welcome! This app uses RAG technology to answer questions from your documents.")

# 5. Create a Button and tell it what to do when clicked
if st.button("Say Hello to my AI"):
    # This code only runs when the user clicks the button
    st.success("Hello, Future AI Engineer! Your interface is working.")
    
# 6. Add a sidebar for extra settings later
st.sidebar.title("App Settings")
st.sidebar.info("Upload your PDF to get started.")
