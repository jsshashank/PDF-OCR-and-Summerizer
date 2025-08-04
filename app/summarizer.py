from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_chunk_len=1024):
    chunks = [text[i:i+max_chunk_len] for i in range(0, len(text), max_chunk_len)]
    return "\n".join([summarizer(chunk)[0]['summary_text'] for chunk in chunks])
