from pypdf import PdfReader

def extract_pdf_text(filepath: str) -> str:
    """
    Extract text from a PDF file.
    """
    reader = PdfReader(filepath)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text
