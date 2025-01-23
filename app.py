import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
llm=ChatGroq(model="llama-3.1-8b-instant")

from flask import Flask,render_template,jsonify,request
from src.helper import load_pdf_file,text_split,download_hugging_face_embeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from src.prompt import *

app=Flask(__name__)

extracted_data=load_pdf_file(data="Data/")
text_chunks=text_split(extracted_data)
embeddings=download_hugging_face_embeddings()
vectorstore=FAISS.from_documents(documents=text_chunks, embedding=embeddings)
retriever=vectorstore.as_retriever()

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",template),
        ("user","{input}")
    ]
)
document_chain=create_stuff_documents_chain(llm,prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)
    response=retrieval_chain.invoke({"input": msg})
    print("Response : ",response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)