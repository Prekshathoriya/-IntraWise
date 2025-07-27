# read text from all PDFs in data folder
import os
from PyPDF2 import PdfReader

def load_pdfs(folder_path="data"):
    all_text = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            reader = PdfReader(os.path.join(folder_path, file_name))
            for page in reader.pages:
                all_text += page.extract_text() + "\n"
    return all_text
