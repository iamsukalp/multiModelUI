import streamlit as st


def reset_conversation():
    if "messages" in st.session_state and len(st.session_state.messages) > 0:
        st.session_state.pop("messages", None)
    if "audio_prompt" in st.session_state:
        st.session_state.pop("audio_prompt", None)


def removeImage(index):
    st.session_state.messages.pop(index)
    st.rerun()
