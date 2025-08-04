# PDF-OCR-and-Summerizer
A python app that scans pdf and give Summary of pdf.
---
## Feautures :
- **Scanning pdf** [multipage support] (using OCR)
- **Auto Text summarization** (using transformers)
- clean GUI (Gradio)
- chunked summary
---
## TEch stack :

| Component       | Library / Tool                       |
|----------------|--------------------------------------|
| PDF → Image     | [`PyMuPDF`](https://pymupdf.readthedocs.io/)     |
| OCR             | [`Tesseract`](https://github.com/tesseract-ocr/tesseract) via `pytesseract` |
| Summarization   | [`transformers`](https://huggingface.co/transformers/) (`facebook/bart-large-cnn`) |
| GUI             | [`gradio`](https://gradio.app/)      |
---

## dependencies :

-pip install -r requirements.txt
