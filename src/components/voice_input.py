# voice_input.py code file
import streamlit as st
from streamlit_mic_recorder import speech_to_text

def get_voice_input():
    st.subheader("Input Options")
    col1, col2 = st.columns([3, 1])

    with col1:
        text_input = st.chat_input("Type your question here...")

    with col2:
        voice_text = speech_to_text(
            language='en',
            start_prompt="🎤 Speak",
            stop_prompt="Stop",
            just_once=True,
            key='voice_input'
        )

    return voice_text if voice_text else text_input