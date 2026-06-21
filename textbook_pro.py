# ... (Previous imports and setup from Module 8)

# Find the section in your code where the AI generates a response:
if prompt := st.chat_input("Ask a question about the textbook..."):
    # Store and show User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # --- WE WANT TO STOP HERE ---
    # To set a breakpoint, click the margin (gutter) to the left of the line number below.
    # A small red dot should appear.
    
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | rag_prompt | llm | StrOutputParser()
    )

    # Generate Response
    with st.chat_message("assistant"):
        response = chain.invoke(prompt) # The code will pause BEFORE this line finishes
        st.markdown(response) # You can inspect 'response' here
        st.session_state.messages.append({"role": "assistant", "content": response})

