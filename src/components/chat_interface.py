import streamlit as st

def render_chat_interface(conversation, messages):
    # Display chat history for the current chat
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    from src.components.voice_input import get_voice_input
    user_input = get_voice_input()

    if user_input:
        # Add user message to current chat history
        messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = conversation.invoke({"input": user_input})
                st.markdown(response['text'])

        # Add bot response to current chat history
        messages.append({"role": "assistant", "content": response['text']})