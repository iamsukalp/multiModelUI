import streamlit as st
from Tabs.ChatTab import chatTab
from Tabs.ExtractionTab import extractionTab
from Tabs.TranslatorTab import translatorTab


# Set page configuration - this must be the first Streamlit command
st.set_page_config(
    layout="wide",
    page_title="Sage",
    page_icon=":speech_balloon:",
    initial_sidebar_state="collapsed",
)

st.logo(
    "src/logo.png",
)

tab1, tab2, tab3 = st.tabs(["Chat", "Vision", "Translator"])

with tab1:
    chatTab()

with tab2:
    extractionTab()

with tab3:
    translatorTab()
