from transformers import pipeline, AutoTokenizer

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
summarizer = pipeline("summarization", model=MODEL_NAME, device=0 if __import__("torch").cuda.is_available() else -1)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def summarize_text(text):
    # Token-based chunking
    tokens = tokenizer.encode(text, add_special_tokens=False)
    max_tokens = 512  # fits model input size
    chunks = [tokens[i:i+max_tokens] for i in range(0, len(tokens), max_tokens)]
    summaries = []

    for chunk in chunks:
        decoded_chunk = tokenizer.decode(chunk, skip_special_tokens=True)
        if not decoded_chunk.strip():
            continue
        result = summarizer(
            decoded_chunk,
            max_length=200,
            min_length=60,
            do_sample=False
        )
        summaries.append(result[0]["summary_text"])

    final_summary = " ".join(summaries)

    # If final summary is too long, run one more summarization pass
    if len(final_summary.split()) > 400:
        result = summarizer(
            final_summary,
            max_length=300,
            min_length=100,
            do_sample=False
        )
        final_summary = result[0]["summary_text"]

    return final_summary
# from transformers import pipeline
# from chunker import chunk_text

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(text):
#     chunks = chunk_text(text)
#     summaries = []

#     for chunk in chunks:
#         result = summarizer(
#             chunk,
#             max_length=120,
#             min_length=40,
#             do_sample=False
#         )
#         summaries.append(result[0]["summary_text"])

#     final_summary = " ".join(summaries)

#     while len(final_summary.split()) > 800:
#         result = summarizer(
#             final_summary[:3000],
#             max_length=200,
#             min_length=80,
#             do_sample=False
#         )
#         final_summary = result[0]["summary_text"]

#     return final_summary

# import nltk
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords
# from collections import defaultdict

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# def summarize_text(text):
#     if not text.strip():
#         return "Please enter some text."
#     if len(text.split()) < 10:
#         return text
#     stop_words = set(stopwords.words("english"))
#     words = word_tokenize(text.lower())
#     freq = defaultdict(int)
#     for word in words:
#         if word.isalnum() and word not in stop_words:
#             freq[word] += 1
#     sentences = sent_tokenize(text)
#     sentence_scores = {}
#     for sentence in sentences:
#         for word in word_tokenize(sentence.lower()):
#             if word in freq:
#                 sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]
#     ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
#     summary = " ".join(ranked[:5])
#     return summary

# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="facebook/bart-large-cnn"
# )

# def summarize_text(text):

#     if not text.strip():
#         return "Please enter some text."

#     text = text[:3000]

#     summary = summarizer(
#         text,
#         max_length=120,
#         min_length=40,
#         do_sample=False
#     )

#     return summary[0]["summary_text"]


# from transformers import pipeline

# summarizer = pipeline(
#     "summarization",
#     model="csebuetnlp/mT5_multilingual_XLSum"
# )

# def summarize_text(text):

#     if not text.strip():
#         return "Please enter some text."

#     if len(text.split()) < 30:
#         return text

#     text = text[:3000]

#     summary = summarizer(
#         text,
#         max_length=150,
#         min_length=50,
#         do_sample=False
#     )

#     return summary[0]["summary_text"]

# from transformers import pipeline

# summarizer = pipeline(
#     "text2text-generation",
#     model="google/mt5-small"
# )

# def summarize_text(text):

#     prompt = "summarize: " + text[:2000]

#     result = summarizer(
#         prompt,
#         max_length=150,
#         do_sample=False
#     )

#     return result[0]["generated_text"]

# from transformers import pipeline

# # Load BART model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# def summarize_text(text):
#     if len(text) < 50:
#         return "Text is too short to summarize."
#     summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
#     return summary[0]['summary_text']

