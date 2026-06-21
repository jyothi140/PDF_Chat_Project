# Import the streamlit library
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PDF Architect", layout="wide")

# 2. THE SIDEBAR: Everything inside this 'with' block goes to the left panel
with st.sidebar:
    # Add a title to the sidebar
    st.title(" Control Center")
    
    # Add an informational 'Info' box for user instructions
    st.info("Step 1: Upload your PDF\nStep 2: Ask a question")
    
    # Add a divider for clean visual separation
    st.divider()
    
    # Add a status indicator (we will make this dynamic later!)
    st.markdown("### 🚦 System Status")
    st.success("PDF Engine: Ready")
    
    # Add a version number at the bottom of the sidebar
    st.caption("v1.0.4 - Phase 2 Internship")

# 3. THE MAIN AREA: This stays in the center of the screen
st.title(" Chat with your PDF")

# Create a placeholder for where the chat will eventually go
st.write("The main area is now clean and ready for your conversation.")

# 4. Use a Column layout in the main area for a 'Featured' look
col1, col2 = st.columns([3, 1]) # Create two columns: one wide, one narrow

with col1:
    st.subheader("Recent Activity")
    st.write("No questions asked yet.")

with col2:
    # This acts like a mini-sidebar on the right side
    st.button("Clear Chat History")
