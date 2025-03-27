import streamlit as st

def get_voice_input():
    st.subheader("Input Options")
    text_input = st.chat_input("Type your question here...")
    return text_input