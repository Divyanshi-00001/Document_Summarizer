from transformers import AutoTokenizer

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def chunk_text(text, max_tokens=512):
    # Basic tokenization-based chunking
    tokens = tokenizer.encode(text, add_special_tokens=False)
    chunks = [tokens[i:i+max_tokens] for i in range(0, len(tokens), max_tokens)]
    return [tokenizer.decode(chunk, skip_special_tokens=True) for chunk in chunks]

# def chunk_text(text, chunk_size=2000):
#     chunks = []
#     for i in range(0, len(text), chunk_size):
#         chunks.append(text[i:i+chunk_size])
#     return chunks