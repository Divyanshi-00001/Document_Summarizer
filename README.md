# AI Multilingual Document Summarizer

## Description

AI Multilingual Document Summarizer is a web-based application that generates concise summaries from long text documents and PDF files using Deep Learning and Natural Language Processing (NLP) techniques. The system supports automatic language detection, keyword extraction, and abstractive text summarization through Transformer-based models.

The project is designed to reduce the time required to read lengthy documents by automatically extracting the most important information and presenting it in a concise form.

## Code snippets

1. app.py (updated)
    Features:
        Text or PDF input
        Language detection
        Optional translation to English for summarization and back to source language
        Adaptive chunking (via chunker.py)
        Per-chunk summaries displayed in UI
        Keywords, download of final summary
        Progress indicators and basic error handling

2. chunker.py 
    Simple token-based chunking that respects a max_tokens budget.
    Uses the same tokenizer as my summarizer to keep compatibility.

3. summarizer.py 
    Designed to summarize per chunk and return a combined summary.

4. keyword_extractor.py 
    Returns top 10 keywords

5. language_detector.py
    Simple language detection with a fallback.

6. translator.py 
    Lightweight translation helpers using deep-translator.
    translate_to_english: auto-detect source, translate to English
    translate_from_english: translate from English to a target language (e.g., "es" for Spanish, "fr" for French, etc.)

7. requirements.txt 
    Include a couple of added libraries and pin versions for reproducibility.

## Technologies Used

### Programming Language

* Python

### Deep Learning & NLP

* Transformers (Hugging Face)
* mT5 / BART Models
* NLTK
* LangDetect

### Libraries

* PyPDF2
* YAKE
* Deep Translator
* SentencePiece
* Torch

### Framework

* Streamlit

## System Workflow

1. User uploads a PDF file or enters text.
2. Text is extracted from PDF using PyPDF2.
3. Language is automatically detected.
4. Long documents are divided into manageable chunks.
5. Transformer-based model generates summaries for each chunk.
6. Chunk summaries are combined into a final summary.
7. Important keywords are extracted using YAKE.
8. Summary and keywords are displayed on the Streamlit interface.
9. User can download the generated summary.

## System architecture diagram (optional)

    A simple ASCII or image diagram showing: UI (Streamlit) -> Input handling -> Language detection -> Translation (optional) -> Chunking -> Summarization -> Keyword extraction -> Export.

## Skills Set Required

* Natural Language Processing (NLP)
* Deep Learning
* Transformer Models
* Text Summarization
* Multilingual AI Systems
* PDF Processing
* Streamlit Application Development
* Python Programming
* Model Integration
* Keyword Extraction

## Future Enhancements

* Research Paper Analysis
* Question Answering from Documents
* PDF Chatbot
* PowerPoint Generation from Documents

## Installation

```bash
pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

## Author

 Divyanshi Agarwal

 B.Tech CSE (AI & Data Science)
 
 Graphic Era Deemed to be University


