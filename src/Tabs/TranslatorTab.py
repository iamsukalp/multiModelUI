import streamlit as st
from Util.translator import translate_text


def translatorTab():

    languages_supported = [
        "Afrikaans",
        "Albanian",
        "Amharic",
        "Arabic",
        "Armenian",
        "Azerbaijani",
        "Basque",
        "Belarusian",
        "Bengali",
        "Bosnian",
        "Bulgarian",
        "Burmese",
        "Catalan",
        "Cebuano",
        "Chichewa",
        "Chinese",
        "Corsican",
        "Croatian",
        "Czech",
        "Danish",
        "Dutch",
        "English",
        "Esperanto",
        "Estonian",
        "Filipino",
        "Finnish",
        "French",
        "Galician",
        "Georgian",
        "German",
        "Greek",
        "Gujarati",
        "Haitian Creole",
        "Hausa",
        "Hawaiian",
        "Hebrew",
        "Hindi",
        "Hmong",
        "Hungarian",
        "Icelandic",
        "Igbo",
        "Indonesian",
        "Irish",
        "Italian",
        "Japanese",
        "Javanese",
        "Kannada",
        "Kazakh",
        "Khmer",
        "Korean",
        "Kurdish",
        "Kyrgyz",
        "Lao",
        "Latin",
        "Latvian",
        "Lithuanian",
        "Luxembourgish",
        "Macedonian",
        "Malagasy",
        "Malay",
        "Malayalam",
        "Maltese",
        "Maori",
        "Marathi",
        "Mongolian",
        "Nepali",
        "Norwegian",
        "Pashto",
        "Persian",
        "Polish",
        "Portuguese",
        "Punjabi",
        "Romanian",
        "Russian",
        "Samoan",
        "Scots Gaelic",
        "Serbian",
        "Sesotho",
        "Shona",
        "Sindhi",
        "Sinhala",
        "Slovak",
        "Slovenian",
        "Somali",
        "Spanish",
        "Sundanese",
        "Swahili",
        "Swedish",
        "Tajik",
        "Tamil",
        "Telugu",
        "Thai",
        "Turkish",
        "Ukrainian",
        "Urdu",
        "Uzbek",
        "Vietnamese",
        "Welsh",
        "Xhosa",
        "Yiddish",
        "Yoruba",
        "Zulu",
    ]

    input, filler, output = st.columns([2, 0.1, 2])
    input_text = None
    output_language = None

    with input:
        inputContainer = st.container(border=True, height=450)
        with inputContainer:
            st.subheader("Input Text")
            input_text = st.text_area(
                height=300,
                label="Input Text",
                label_visibility="hidden",
                placeholder="Input the text to be translated",
            )

    with output:
        outputContainer = st.container(border=True, height=450)
        with outputContainer:
            st.subheader("Translation")

    col1, col2, col3 = st.columns(
        [1.5, 7.5, 1], gap="large", vertical_alignment="center"
    )

    with col1:
        output_language = st.selectbox(
            "Translate to",
            languages_supported,
        )

    with col3:
        st.write("\n")
        if st.button("Translate"):
            if input_text and output_language:
                output_text = translate_text(input_text, output_language)
                with outputContainer:
                    st.code(output_text)
            else:
                with outputContainer:
                    st.code("Check input params")
