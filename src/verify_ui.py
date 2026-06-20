# Import the streamlit library we just installed
import streamlit as st

# 1. Print a message to the internal terminal
print("---  UI Toolkit Verification ---")

# 2. Check the version of Streamlit
# This confirms the 'bricks' are in the box and ready to use
try:
    version = st.__version__
    print(f" Streamlit version {version} is successfully installed!")
    print(" You are ready to run: 'streamlit hello'")
except Exception as e:
    # 3. If something went wrong, show the error
    print(f" Installation Error: {e}")
