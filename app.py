import streamlit as st
from src.components.sidebar import render_sidebar
from src.components.chat_interface import render_chat_interface
from src.components.voice_input import get_voice_input
from src.models.conversation import get_conversation_chain

# Main app layout
st.title("EduMentor AI")
st.write("Welcome! I'm your offline educational mentor. How can I assist you today?")

def main():
    # Initialize chat sessions in session state
    if "chat_sessions" not in st.session_state:
        st.session_state.chat_sessions = {}  # Dictionary: {chat_id: {"conversation": LLMChain, "messages": []}}
    if "current_chat_id" not in st.session_state:
        st.session_state.current_chat_id = None

    # Render sidebar and get selected chat ID
    education_level, selected_chat_id = render_sidebar()

    # Set or create current chat
    if selected_chat_id:
        st.session_state.current_chat_id = selected_chat_id
        if selected_chat_id not in st.session_state.chat_sessions:
            st.session_state.chat_sessions[selected_chat_id] = {
                "conversation": get_conversation_chain(),
                "messages": []
            }
    elif st.session_state.current_chat_id is None and st.session_state.chat_sessions:
        st.session_state.current_chat_id = list(st.session_state.chat_sessions.keys())[0]

    # Render chat interface for current chat
    if st.session_state.current_chat_id:
        current_chat = st.session_state.chat_sessions[st.session_state.current_chat_id]
        render_chat_interface(current_chat["conversation"], current_chat["messages"])

    # Add footer
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            right: 0;
            bottom: 0;
            margin-right: 1rem;
            margin-bottom: 1rem;
            z-index: 1000;
            background-color: transparent;
            text-align: right;
        }
        </style>
        <div class="footer">
            Developed by <a href="https://pratirath06.github.io/" target="_blank">Pratirath Gupta</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()