# Import the streamlit library to control the web browser interface
import streamlit as st

# 1. SET PAGE CONFIG: This must be the very first Streamlit command in your script!
# 'page_title' sets the name on the browser tab.
# 'page_icon' sets the little emoji or image on the tab.
# 'layout' set to "wide" uses the full width of the screen.
st.set_page_config(
    page_title="PDF Chat Architect",
    page_icon="",
    layout="wide"
)

# 2. APP HEADER: Create a big, bold title at the top of the page
st.title(" PDF Chat Architect")

# 3. SUBHEADER: Add a smaller line of text to explain the app's purpose
st.subheader("Your Intelligent PDF Retrieval Assistant")

# 4. DIVIDER: Draw a horizontal line to separate the header from the content
st.divider()

# 5. SIDEBAR: Add a status message to the left-hand panel
# This keeps the main screen clean for the actual chat later
st.sidebar.success("Foundation Pipeline: Online")

# 6. STATUS MESSAGE: A simple text block to confirm the app is running
st.write("The foundation is set. Ready to integrate the RAG engine.")

