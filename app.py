# app.py file
import streamlit as st
from src.components.sidebar import render_sidebar
from src.components.chat_interface import render_chat_interface
from src.components.voice_input import get_voice_input
from src.models.conversation import get_conversation_chain

# Main app layout
st.title("EduMentor AI")
st.write("Welcome! I'm your educational mentor. How can I assist you today?")

def main():
    # Initialize conversation chain
    conversation = get_conversation_chain()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Render sidebar
    education_level = render_sidebar()

    # Render chat interface
    render_chat_interface(conversation)

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