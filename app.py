import streamlit as st
from PyPDF2 import PdfReader

from summarizer import summarize_text
from language_detector import detect_language
from keyword_extractor import extract_keywords
from translator import translate_to_english, translate_from_english
from chunker import chunk_text

st.set_page_config(page_title="Document Summarization Tool", page_icon="📄")
st.title("📄 Document Summarization Tool")
st.write("Upload a PDF or enter text to generate an AI-powered summary.")

option = st.radio("Choose Input Type", ["Text", "PDF"])
text = ""

# Input
if option == "Text":
    text = st.text_area("Enter Text", height=250)
else:
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file is not None:
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"

# Validate input
if text.strip():
    # Language detection
    language = detect_language(text)
    st.write(f"Detected Language: {language}")
else:
    language = "unknown"

# Optional: translate input to English for summarization
translate_to_en = st.checkbox("Translate input to English for summarization", value=(language != "en"))
original_language = language

if st.button("Generate Summary"):
    if text.strip() == "":
        st.warning("Please provide text or upload a PDF.")
    else:
        with st.spinner("Preparing text..."):
            working_text = text

            # If needed, translate to English for the model
            if translate_to_en:
                working_text = translate_to_english(text)

            # Chunking
            chunks = chunk_text(working_text)

            # Summarize per chunk
            st.subheader("Chunk-wise Summaries")
            combined_summary_parts = []
            for idx, chunk in enumerate(chunks, start=1):
                if not chunk.strip():
                    continue
                with st.spinner(f"Summarizing chunk {idx}/{len(chunks)}"):
                    chunk_summary = summarize_text(chunk)
                combined_summary_parts.append(chunk_summary)
                st.markdown(f"**Chunk {idx}/{len(chunks)} Summary:**")
                st.write(chunk_summary)

            final_summary = " ".join(combined_summary_parts)

            # Optional: post-process final summary if too long
            # (summarizer.py already handles length, but you can trim here)
            st.subheader("Final Summary")
            st.write(final_summary)

            # Translate back to original language if requested
            if translate_to_en and original_language != "en":
                final_summary_in_orig = translate_from_english(final_summary, target_lang=original_language)
            else:
                final_summary_in_orig = final_summary

            st.subheader("Summary (in original language)")
            st.write(final_summary_in_orig)

            # Keywords (on the English or original text depending on your preference)
            st.subheader("Keywords")
            # If you translated, extract keywords on the English text for consistency
            keywords_source = working_text
            keywords = extract_keywords(keywords_source)
            for keyword in keywords:
                st.write("•", keyword)

            # Download button (provide final summary in original language)
            st.download_button(label="Download Summary",
                               data=final_summary_in_orig,
                               file_name="summary.txt",
                               mime="text/plain")
# import streamlit as st
# from PyPDF2 import PdfReader
# from summarizer import summarize_text

# st.set_page_config(page_title="Document Summarization Tool", page_icon="📄")
# st.title("📄 Document Summarization Tool")
# st.write("Upload a PDF or enter text to generate a summary.")
# option = st.radio("Choose Input Type", ["Text", "PDF"])
# text = ""

# # Text Input
# if option == "Text":
#     text = st.text_area("Enter Text", height=250)
    
# # PDF Upload
# else:
#     uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
#     if uploaded_file is not None:
#         pdf_reader = PdfReader(uploaded_file)
#         for page in pdf_reader.pages:
#             extracted = page.extract_text()
#             if extracted:
#                 text += extracted + "\n"
# from language_detector import detect_language
# language = detect_language(text)
# st.write("Detected Language:", language)
# if st.button("Generate Summary"):
#     if text.strip() == "":
#         st.warning("Please provide text or upload a PDF.")
#     else:
#         with st.spinner("Generating Summary..."):
#             summary = summarize_text(text)
#         st.subheader("Summary")
#         st.write(summary)
#         st.download_button(label="Download Summary", data=summary, file_name="summary.txt", mime="text/plain")
# if st.button("Generate Chapter Summary"):

