# chat_interface.py code file
import streamlit as st

def render_chat_interface(conversation):
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    from src.components.voice_input import get_voice_input
    user_input = get_voice_input()

    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Generate bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = conversation.invoke({"input": user_input})
                st.markdown(response['text'])

        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response['text']})