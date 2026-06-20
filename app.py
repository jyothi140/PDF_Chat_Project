# Import streamlit to build the interface
import streamlit as st
# Import random to demonstrate how the script 'reruns'
import random

# 1. Page configuration (Always at the top!)
st.set_page_config(page_title="Magic Rerun Lab", page_icon="🪄")

# 2. Add a Title
st.title(" The Magic Execution Lab")

# 3. This number will change EVERY time the script reruns
# It proves Streamlit runs from top-to-bottom on every interaction
lucky_number = random.randint(1, 100)
st.write(f" Your 'Lucky Number' for this rerun is: **{lucky_number}**")

# 4. Create a button to trigger a rerun
if st.button("Trigger a Rerun"):
    # When you click this, the whole script starts over from line 1
    st.write("The button was clicked! Streamlit is rerunning...")

# 5. Add a text input to trigger a rerun
# Every time you type and hit 'Enter', the script reruns
user_text = st.text_input("Type something and hit Enter:")
if user_text:
    st.write(f"You typed: {user_text}")

# 6. Debug message to show where we are
st.info(" Tip: Look at the top right of the browser for the 'Always rerun' option!")

