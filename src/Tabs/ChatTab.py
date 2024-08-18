import streamlit as st
from components.messageComponent import messageComponent
from Util.resetButtonComponent import reset_conversation
from Util.imageHandler import add_image_to_messages
from components.audioButtonComponent import audionButtonComponent
import time


@st.dialog("Dictate")
def audioRecorder():

    with st.container(height=250):
        audionButtonComponent()


def chatTab():

    user_prompt = None
    image_prompt = None
    audio_prompt = None
    chat_container = st.container(border=True, height=450)
    input_field, attachBtn, cameraBtn, audioBtn, clearBtn = st.columns(
        [0.6, 0.04, 0.04, 0.03, 0.03]
    )

    with attachBtn:
        with st.popover("🔗"):
            st.file_uploader(
                "Upload an image",
                type=["png", "jpg", "jpeg"],
                accept_multiple_files=False,
                key="uploaded_img",
                on_change=add_image_to_messages,
            )
            image_prompt = "image"

    with cameraBtn:
        with st.popover("📷"):
            activate_camera = st.checkbox("Activate camera")
            if activate_camera:
                st.camera_input(
                    "Take a picture",
                    key="camera_img",
                    on_change=add_image_to_messages,
                )
                image_prompt = "image"

    with audioBtn:
        if st.button("🎙️", help="Record audio"):
            audioRecorder()

    with clearBtn:
        st.button("🧹", help="Clear conversation", on_click=reset_conversation)

    with input_field:
        user_prompt = st.chat_input("Hi! Ask me anything...")

    if "audio_prompt" in st.session_state:
        audio_prompt = st.session_state.audio_prompt
        print(audio_prompt)

    if user_prompt or audio_prompt or image_prompt:
        with chat_container:
            messageComponent(user_prompt or audio_prompt)
