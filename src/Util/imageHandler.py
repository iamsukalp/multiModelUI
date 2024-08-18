import streamlit as st
from PIL import Image
import random
import base64
from io import BytesIO
from components.messageComponent import messageComponent


# Function to convert file to base64
def get_image_base64(image_raw):
    buffered = BytesIO()
    image_raw.save(buffered, format=image_raw.format)
    img_byte = buffered.getvalue()

    return base64.b64encode(img_byte).decode("utf-8")


def file_to_base64(file):
    with open(file, "rb") as f:

        return base64.b64encode(f.read())


def base64_to_image(base64_string):
    base64_string = base64_string.split(",")[1]

    return Image.open(BytesIO(base64.b64decode(base64_string)))


def add_image_to_messages():
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.session_state.uploaded_img or (
        "camera_img" in st.session_state and st.session_state.camera_img
    ):
        img_type = (
            st.session_state.uploaded_img.type
            if st.session_state.uploaded_img
            else "image/jpeg"
        )
        if img_type == "video/mp4":
            # save the video file
            video_id = random.randint(100000, 999999)
            with open(f"video_{video_id}.mp4", "wb") as f:
                f.write(st.session_state.uploaded_img.read())
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "video_file",
                            "video_file": f"video_{video_id}.mp4",
                        }
                    ],
                }
            )
        else:
            raw_img = Image.open(
                st.session_state.uploaded_img or st.session_state.camera_img
            )
            img = get_image_base64(raw_img)
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:{img_type};base64,{img}"},
                        }
                    ],
                }
            )
