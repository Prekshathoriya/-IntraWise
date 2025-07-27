# make embeddings and store in chroma database
import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from utils.pdf_loader import load_pdfs
from utils.text_splitter import split_text

# where to store the chroma db
CHROMA_PATH = "chroma_db"

def build_vector_db():
    # 1. load all text from PDFs
    text = load_pdfs("data")
    if not text.strip():
        print("No PDF text found.")
        return None

    # 2. split text into chunks
    chunks = split_text(text)

    # 3. make embeddings using HuggingFace (free)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # 4. create vector store (Chroma)
    db = Chroma.from_texts(chunks, embedding=embeddings, persist_directory=CHROMA_PATH)

    # 5. save database
    db.persist()
    print(f"Vector DB saved to {CHROMA_PATH} with {len(chunks)} chunks.")
    return db
