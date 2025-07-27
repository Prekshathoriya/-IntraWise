# retrieve info and answer using a local HuggingFace model (no Ollama)
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

CHROMA_PATH = "chroma_db"

def load_qa():
    # embeddings must match ingestion
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    # Load a small local model (free, CPU)
    model_name = "google/flan-t5-base"  # light model that works on CPU
    pipe = pipeline("text2text-generation", model=model_name)
    llm = HuggingFacePipeline(pipeline=pipe)

    # prompt
    prompt = PromptTemplate(
        template="Answer using only this context:\n{context}\n\nQuestion: {question}\nAnswer:",
        input_variables=["context", "question"]
    )

    # create RetrievalQA
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )
    return qa

def get_answer(query):
    qa = load_qa()
    return qa.run(query)
