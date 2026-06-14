# AI Multilingual Document Summarizer

## Description

AI Multilingual Document Summarizer is a web-based application that generates concise summaries from long text documents and PDF files using Deep Learning and Natural Language Processing (NLP) techniques. The system supports automatic language detection, keyword extraction, and abstractive text summarization through Transformer-based models.

The project is designed to reduce the time required to read lengthy documents by automatically extracting the most important information and presenting it in a concise form.

## Features

* Text Summarization
* PDF Document Summarization
* Deep Learning-based Abstractive Summarization
* Automatic Language Detection
* Multilingual Document Support
* Keyword Extraction
* PDF Text Extraction
* Download Summary Option
* Interactive Streamlit Interface

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

## Project Architecture

Input Document
↓
PDF/Text Extraction
↓
Language Detection
↓
Text Chunking
↓
Transformer-based Summarization
↓
Keyword Extraction
↓
Summary Generation
↓
Streamlit User Interface

## Skills Demonstrated

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

* Large PDF Support
* Chapter-wise Summarization
* AI-powered Insights Generation
* Research Paper Analysis
* Question Answering from Documents
* PDF Chatbot
* Named Entity Recognition (NER)
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
