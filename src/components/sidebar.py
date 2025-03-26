# sidebar.py code file
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

        if st.button("Clear Chat"):
            st.session_state.messages = []

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

    return education_level