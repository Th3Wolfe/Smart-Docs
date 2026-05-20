from pypdf import PdfReader
from docx import Document
from pathlib import Path


def extract_text_from_pdf(file_path: str):

    text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_text_from_docx(file_path: str):

    doc = Document(file_path)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_text(file_path: str):

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    else:
        raise ValueError("Formato de arquivo não suportado")