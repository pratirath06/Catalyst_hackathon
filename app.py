import streamlit as st
from src.components.sidebar import render_sidebar
from src.models.conversation import get_conversation_chain

# Page config
st.set_page_config(page_title="EduMentor AI", layout="wide")

# Main app layout
st.title("EduMentor AI")
st.write("Welcome! I'm your offline educational mentor. Ask me anything!")

def main():
    # Initialize single chat session in session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = get_conversation_chain()
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = None
    if "game_state" not in st.session_state:
        st.session_state.game_state = {"active": False, "type": None, "content": None, "user_answer": ""}

    # Render sidebar and get feature outputs
    notes_content, quiz_content, game_content = render_sidebar()

    # Handle feature outputs (no clearing here; done in sidebar)
    if notes_content:
        st.session_state.messages.append({"role": "assistant", "content": notes_content})
        st.download_button("Download Notes", notes_content, file_name="study_notes.txt")
    if quiz_content:
        st.session_state.quiz_questions = quiz_content
        st.session_state.messages.append({"role": "assistant", "content": quiz_content})
    if game_content:
        st.session_state.game_state = game_content
        st.session_state.messages.append({"role": "assistant", "content": game_content["content"]})

    # Chat area
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Get user input
    from src.components.voice_input import get_voice_input
    user_input = get_voice_input()

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.conversation.invoke({"input": user_input})
                st.markdown(response['text'])
        st.session_state.messages.append({"role": "assistant", "content": response['text']})

    # Quiz display
    if st.session_state.quiz_questions:
        st.subheader("Quiz Time!")
        st.write(st.session_state.quiz_questions)
        answer = st.text_area("Your Answers (one per line):")
        if st.button("Submit Quiz Answers"):
            prompt = f"Check these answers for the quiz:\n\nQuiz:\n{st.session_state.quiz_questions}\n\nAnswers:\n{answer}"
            result = st.session_state.conversation.invoke({"input": prompt})['text']
            st.write("Results:", result)
            st.session_state.messages.append({"role": "assistant", "content": f"Quiz Results:\n{result}"})
            st.session_state.quiz_questions = None

    # Game display
    if st.session_state.game_state["active"]:
        st.subheader(f"Game: {st.session_state.game_state['type']}")
        st.write(st.session_state.game_state["content"])
        game_answer = st.text_input("Your Answer:")
        if st.button("Submit Game Answer"):
            prompt = f"Check this answer for the game:\n\n{st.session_state.game_state['content']}\n\nAnswer: {game_answer}"
            result = st.session_state.conversation.invoke({"input": prompt})['text']
            st.write("Result:", result)
            st.session_state.messages.append({"role": "assistant", "content": f"Game Result: {result}"})
            st.session_state.game_state["active"] = False

    # Footer
    st.markdown(
        """
        <style>
        .footer {position: fixed; right: 0; bottom: 0; margin-right: 1rem; margin-bottom: 1rem; z-index: 1000; text-align: right;}
        </style>
        <div class="footer">Developed by <a href="https://pratirath06.github.io/" target="_blank">Pratirath Gupta</a></div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()