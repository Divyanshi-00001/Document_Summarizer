# from transformers import pipeline

# # Load BART model
# summarizer = pipeline(
#     "summarization",
#     model="facebook/bart-large-cnn"
# )

# def summarize_text(text):
#     if len(text) < 50:
#         return "Text is too short to summarize."

#     summary = summarizer(
#         text,
#         max_length=130,
#         min_length=30,
#         do_sample=False
#     )

#     return summary[0]['summary_text']

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def summarize_text(text):

    if not text.strip():
        return "Please enter some text."

    if len(text.split()) < 10:
        return text

    stop_words = set(stopwords.words("english"))

    words = word_tokenize(text.lower())

    freq = defaultdict(int)

    for word in words:
        if word.isalnum() and word not in stop_words:
            freq[word] += 1

    sentences = sent_tokenize(text)

    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    ranked = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )

    summary = " ".join(ranked[:5])

    return summary