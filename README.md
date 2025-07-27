# 🤖 IntraWise – Smart Internal FAQ Assistant

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen)](https://lkvckrdsmencx7xcyxetum.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

**IntraWise** is an AI-powered **internal company FAQ assistant**.  
Upload your HR manuals, policy PDFs, or onboarding guides and instantly **ask natural language questions**.  
The app answers **only from your documents** using Retrieval-Augmented Generation (RAG).

---

## 🚀 Live Demo
🔗 **Try it now:** [https://lkvckrdsmencx7xcyxetum.streamlit.app/](https://lkvckrdsmencx7xcyxetum.streamlit.app/)

---

## ✨ Features

- **Upload PDFs:** HR guides, policy manuals, FAQs  
- **Automatic Processing:** Extracts text, chunks content, and builds a local vector database  
- **AI-Powered Q&A:** Ask questions like “How many leaves can I take in a year?”  
- **Contextual Answers:** Uses **only your documents**, not the internet  
- **Beautiful Streamlit UI:** Clean, interactive chat-style interface  
- **Secure and Local:** All processing happens in-memory on Streamlit  

---

## 🧠 How It Works

1. **Document Ingestion**  
   - Extracts text from uploaded PDFs  
   - Splits into smaller chunks  

2. **Vector Database (RAG)**  
   - Creates embeddings using HuggingFace  
   - Stores in ChromaDB (local)

3. **Question Answering**  
   - Retrieves most relevant chunks  
   - Uses a local HuggingFace model to generate the answer  

---

## 📂 Project Structure

intra_wise/
├── app.py # Streamlit app
├── ingest.py # PDF processing & vector DB
├── qa_engine.py # Retrieval + LLM
├── utils/ # Helpers (pdf_loader, text_splitter, config)
├── chroma_db/ # Auto-created local vector store
├── data/ # Uploaded PDFs
└── requirements.txt


---

## 🛠️ Tech Stack

- **Python** – Streamlit, LangChain, ChromaDB
- **Models:** HuggingFace Embeddings & FLAN-T5  
- **Frontend:** Streamlit (no HTML/CSS/JS needed)

---

## 💡 Example Questions

After uploading your policies, try:

- *"How many leaves can I take in a year?"*
- *"What are the work from home rules?"*
- *"What are office timings?"*

---

## 🏗 Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/Prekshathoriya/-IntraWise.git
   cd -IntraWise
Create a virtual environment:python -m venv venv
source venv/Scripts/activate  # Windows
Install dependencies:pip install -r requirements.txt
Run:streamlit run app.py
