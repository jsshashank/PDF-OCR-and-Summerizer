def chunk_text(text, max_len=1024):
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]