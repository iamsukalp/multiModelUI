import streamlit as st
from Util.textExtractor import DocumentTextExtractor

extractor = DocumentTextExtractor()


def download_file(combined_text, filename):
    st.download_button(
        label="Download file",
        data=combined_text,
        file_name=filename,
        mime="text/plain",
    )


def extractionTab():
    textContainer = st.container(border=True, height=450)

    uplaodSection, extractBtn = st.columns(
        [0.9, 0.1], gap="large", vertical_alignment="center"
    )

    with uplaodSection:
        uploaded_files = st.file_uploader(
            "",
            type=["pdf", "png", "jpeg", "pptx"],
            accept_multiple_files=True,
            key="vision",
        )

    with extractBtn:
        st.write("\n")
        st.write("\n")
        if st.button("Extract Text"):
            if uploaded_files:
                if (len(uploaded_files)) == 1:
                    filename = f"{uploaded_files[0].name}.txt"
                else:
                    filename = "combined_extracted_text.txt"
                combined_text = extractor.extract_text_from_multiple_files(
                    uploaded_files
                )
                print(combined_text)
                with textContainer:
                    st.code(combined_text)
                download_file(combined_text, filename)
            else:
                print(f"length: {len(uploaded_files)}")
                st.write("No file imported")
