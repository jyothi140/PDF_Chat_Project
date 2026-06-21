import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="PDF Loader", layout="wide")

# 2. THE SIDEBAR: Where the 'Deposit Slot' lives
with st.sidebar:
    st.title(" Document Center")
    
    # 3. THE UPLOADER: This creates the drag-and-drop widget
    # label: The text above the box
    # type: We restrict this to 'pdf' so users don't upload images or music
    uploaded_file = st.file_uploader("Upload a PDF textbook", type="pdf")
    
    # 4. THE SUCCESS HANDSHAKE: Check if a file was actually dropped in
    if uploaded_file is not None:
        # Display a success message with the file name
        st.success(f"Successfully uploaded: {uploaded_file.name}")
        
        # 5. DEBUG INFO: Show the file size (just to prove we have it!)
        file_size = len(uploaded_file.getvalue()) / 1024
        st.info(f"File Size: {file_size:.2f} KB")
    else:
        # Remind the user what to do if the slot is empty
        st.warning("Please upload a PDF to begin.")

# 3. THE MAIN AREA
st.title(" AI Research Assistant")
st.write("Upload a document in the sidebar to start the conversation.")
