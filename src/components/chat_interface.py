import streamlit as st

def render_chat_interface(conversation, messages, chat_id):
    # Display chat history for the current chat
    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input with unique key
    from src.components.voice_input import get_voice_input
    user_input = get_voice_input(key=f"input_{chat_id}")

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

        # Update chat title based on first message if this is the first exchange
        if len(messages) == 2:  # First user message + first response
            title_prompt = f"Summarize this conversation in 5 words or less: {user_input}"
            title_response = conversation.invoke({"input": title_prompt})
            st.session_state.chat_sessions[chat_id]["title"] = title_response['text'][:30]
            st.switch_page("pages/chat_session.py")