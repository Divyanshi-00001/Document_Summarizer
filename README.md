# Document Summarization Tool

## Description

A web-based application that summarizes long text documents and PDF files using the NLTK because it is lightweight, easier to understand, and demonstrates core NLP concepts such as tokenization, stop-word removal, and sentence ranking.

## Features

- Text Summarization
- PDF Summarization
- NLP preprocessing
- Extractive summaries
- Download Summary
- Streamlit Interface

## Technologies Used

- Python
- Streamlit
- NLTK
- PyPDF2

## How It Works

1. User uploads a PDF or enters text
2. Text is extracted using PyPDF2
3. NLP preprocessing is performed:
   - Tokenization
   - Stop word removal
   - Stemming / Lemmatization
4. Sentence scoring is done using word frequency
5. Top-ranked sentences are selected as summary
6. Summary is displayed on Streamlit UI

## Run

pip install -r requirements.txt

streamlit run app.py
