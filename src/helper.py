import os
from dotenv import load_dotenv
load_dotenv()


os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant")

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import  PyPDFLoader,DirectoryLoader
from langchain_text_splitters import  RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS


def load_pdf_file(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    documents=loader.load()
    return documents

def text_split(extracted_data):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=80)
    chunks=text_splitter.split_documents(extracted_data)
    return chunks

def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L3-v2")
    return embeddings
    