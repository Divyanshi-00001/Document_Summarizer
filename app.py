import streamlit as st
from PyPDF2 import PdfReader
from summarizer import summarize_text

st.set_page_config(
    page_title="Document Summarization Tool",
    page_icon="📄"
)

st.title("📄 Document Summarization Tool")
st.write("Upload a PDF or enter text to generate a summary.")

option = st.radio(
    "Choose Input Type",
    ["Text", "PDF"]
)

text = ""

# Text Input
if option == "Text":
    text = st.text_area(
        "Enter Text",
        height=250
    )

# PDF Upload
else:
    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

if st.button("Generate Summary"):

    if text.strip() == "":
        st.warning("Please provide text or upload a PDF.")
    else:

        with st.spinner("Generating Summary..."):
            summary = summarize_text(text)

        st.subheader("Summary")
        st.write(summary)

        st.download_button(
            label="Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )
