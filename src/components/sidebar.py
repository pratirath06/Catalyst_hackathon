import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("EduMentor AI")
        st.subheader("Settings")

        education_options = [
            "Class 1-5 (Primary)",
            "Class 6-8 (Middle School)",
            "Class 9-10 (Secondary)",
            "Class 11-12 (Higher Secondary)",
            "Undergraduate",
            "Postgraduate",
            "Doctorate"
        ]

        education_level = st.selectbox(
            "Select your education level:",
            education_options,
            index=3
        )

        # Chat session management
        st.subheader("Chat Sessions")
        if st.button("New Chat"):
            new_chat_id = f"Chat {len(st.session_state.chat_sessions) + 1}"
            st.session_state.current_chat_id = new_chat_id

        # Display existing chats
        chat_ids = list(st.session_state.chat_sessions.keys())
        selected_chat_id = st.selectbox(
            "Select a chat:",
            chat_ids if chat_ids else ["No chats yet"],
            index=chat_ids.index(st.session_state.current_chat_id) if st.session_state.current_chat_id in chat_ids else 0
        )

        if st.button("Clear Current Chat") and st.session_state.current_chat_id:
            if st.session_state.current_chat_id in st.session_state.chat_sessions:
                st.session_state.chat_sessions[st.session_state.current_chat_id]["messages"] = []
                st.session_state.chat_sessions[st.session_state.current_chat_id]["conversation"].memory.clear()

        st.divider()
        st.subheader("Resources")
        st.write("📚 [Learning Materials](https://example.com)")
        st.write("📝 [Practice Tests](https://example.com)")
        st.write("📊 [Study Planner](https://example.com)")

        st.divider()
        st.write("Developed by Tidal Techies")

        if st.checkbox("Show Project Structure"):
            st.code("""
            edumentor_ai/
            ├── .streamlit/
            │   └── secrets.toml
            ├── src/
            │   ├── components/
            │   │   ├── sidebar.py
            │   │   ├── voice_input.py
            │   │   └── chat_interface.py
            │   ├── utils/
            │   │   ├── speech_recognition_utils.py
            │   │   └── groq_utils.py
            │   └── models/
            │       └── conversation.py
            ├── logs/
            │   └── application.log
            ├── app.py
            └── requirements.txt
            """)

    return education_level, selected_chat_id