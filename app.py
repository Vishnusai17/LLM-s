import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# --- 1. Load PDF Document ---
# Assumes your PDF is in a 'documents' subdirectory
file_path = os.path.join("documents", "/Users/vishnus/Desktop/local-rag-project/documents/Vishnu Resume Ed Media.pdf") 
if not os.path.exists(file_path):
    print("Error: Document not found. Make sure 'my_document.pdf' is in the 'documents' folder.")
    exit()

loader = PyPDFLoader(file_path)
docs = loader.load()

# --- 2. Split Document into Chunks ---
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

# --- 3. Create Embeddings and Store in FAISS Vector Store ---
# This uses a local, open-source embedding model
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)

# --- 4. Initialize Local LLM (Ollama) ---
llm = Ollama(model="llama3:8b")

# --- 5. Define the RAG Chain ---
# Create a retriever from the vector store
retriever = vectorstore.as_retriever()

# Define the prompt template
template = """
You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.

Context: {context} 

Question: {question} 

Helpful Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

# Create the RAG chain using LangChain Expression Language (LCEL)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# --- 6. Ask a Question ---
if __name__ == "__main__":
    print("PDF loaded and indexed. Ask a question about your document.")
    # Example question (replace with your own)
    question = "What is the main topic of the document?"
    print(f"Question: {question}")
    
    # Invoke the chain to get the answer
    answer = rag_chain.invoke(question)
    
    print("\nAnswer:")
    print(answer)