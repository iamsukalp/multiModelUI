import streamlit as st
from audiorecorder import audiorecorder
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def audionButtonComponent():

    if "audio_prompt" not in st.session_state:
        st.session_state.audio_prompt = None

    audio = audiorecorder("", "")

    if len(audio) > 0:
        # To play audio in frontend:
        st.audio(audio.export().read())

        # To save audio to a file, use pydub export method:
        audio.export("audio.wav", format="wav")

        # To get audio properties, use pydub AudioSegment properties:
        st.write(
            f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds"
        )

        audio_file = open("audio.wav", "rb")
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=(audio_file),
        )

        st.session_state.audio_prompt = transcript.text
        st.rerun()
