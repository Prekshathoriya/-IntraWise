import streamlit as st
import os
from ingest import build_vector_db
from qa_engine import get_answer

# Streamlit page settings
st.set_page_config(page_title="IntraWise", layout="wide")
os.makedirs("data", exist_ok=True)

# Session states to remember chat and processing
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

# Title and description
st.title("🤖 IntraWise – Company FAQ Assistant")
st.write("Upload HR policy PDFs and ask any questions based on them.")

# Sidebar for file upload and processing
st.sidebar.header("Upload & Process")
uploaded_files = st.sidebar.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)

# Save uploaded files
if uploaded_files:
    for file in uploaded_files:
        with open(os.path.join("data", file.name), "wb") as f:
            f.write(file.read())
    st.sidebar.success(f"Uploaded {len(uploaded_files)} file(s)")

# Process button
if st.sidebar.button("⚡ Process Documents"):
    st.sidebar.write("Processing documents, please wait...")
    build_vector_db()
    st.session_state.db_ready = True
    st.sidebar.success("Documents processed successfully! You can now chat.")

# Clear button
if st.sidebar.button("🧹 Clear Uploaded Files"):
    for f in os.listdir("data"):
        os.remove(os.path.join("data", f))
    st.session_state.db_ready = False
    st.session_state.chat_history = []
    st.sidebar.success("All uploaded files removed.")

# Only show chat interface if DB is ready
if st.session_state.db_ready:
    # Chat input
    user_input = st.chat_input("Ask a question about your company policies...")
    if user_input:
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Get answer from QA engine
        answer = get_answer(user_input)

        # Add answer to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

    # Show chat messages
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
else:
    st.info("Upload and process documents first to start chatting.")
