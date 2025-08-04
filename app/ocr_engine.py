import pytesseract

# ✅ Explicitly set the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_text(image):
    return pytesseract.image_to_string(image)
