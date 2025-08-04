import gradio as gr
from app.pdf_reader import pdf_to_images
from app.ocr_engine import image_to_text
from app.summarizer import summarize_text

def process_pdf(file):
    try:
        images = pdf_to_images(file.name)
        text = "\n".join([image_to_text(img) for img in images])
        summary = summarize_text(text)
        return summary
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"❌ Error: {str(e)}"


def launch_gui():
    gr.Interface(
        fn=process_pdf,
        inputs=gr.File(file_types=[".pdf"]),
        outputs="text",
        title="PDF OCR + Summarizer",
        description="Upload a scanned PDF, get a concise summary."
    ).launch()
