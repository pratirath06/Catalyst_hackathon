import streamlit as st

def render_sidebar():
    notes_content = None
    quiz_content = None
    game_content = None

    with st.sidebar:
        st.header("EduMentor AI", divider="gray")
        
        # Educational Level Dropdown
        education_options = [
            "Class 1-5 (Primary)",
            "Class 6-8 (Middle School)",
            "Class 9-10 (Secondary)",
            "Class 11-12 (Higher Secondary)",
            "Undergraduate",
            "Postgraduate",
            "Doctorate"
        ]
        educational_level = st.selectbox(
            "Select your educational level:",
            options=education_options
        #    index=education_options.index(st.session_state.educational_level) if st.session_state.educational_level in education_options else 1
        )

        # Study Notes
        st.subheader("Tools", divider="gray")
        notes_topic = st.text_input("Enter a topic for study notes:")
        if st.button("Generate Notes") and notes_topic:
            st.session_state.messages = []  # Clear chat first
            prompt = f"Provide concise study notes on {notes_topic} (max 200 words)."
            notes_content = st.session_state.conversation.invoke({"input": prompt})['text']
            

        # Quiz Generator
        quiz_topic = st.text_input("Enter a topic for a quiz:")
        if st.button("Generate Quiz") and quiz_topic:
            st.session_state.messages = []  # Clear chat first
            prompt = f"Generate a 5-question short-answer quiz on {quiz_topic}."
            quiz_content = st.session_state.conversation.invoke({"input": prompt})['text']
            

        # Educational Games
        game_type = st.selectbox("Play a Game:", ["None", "Guess the Word", "Math Challenge"])
        if st.button("Start Game") and game_type != "None":
            st.session_state.messages = []  # Clear chat first
            if game_type == "Guess the Word":
                prompt = "Provide a word guessing game: give a hint and expect a one-word answer."
            elif game_type == "Math Challenge":
                prompt = "Provide a simple math problem with a numerical answer."
            game_content = {
                "active": True,
                "type": game_type,
                "content": st.session_state.conversation.invoke({"input": prompt})['text'],
                "user_answer": ""
            }
              # Force UI update after clearing

        # Resources
        #st.divider()
        #st.subheader("Resources")
        #st.write("📚 [Learning Materials](https://example.com)")
        #st.write("📝 [Practice Tests](https://example.com)")
        #st.write("📊 [Study Planner](https://example.com)")

        st.divider()
        st.write("Developed by Team Catalyst")

    return notes_content, quiz_content, game_content