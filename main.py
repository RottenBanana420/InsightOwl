"""
Author: Kusai Hajuri
Date: 2024-07-19
Description: This script uses Streamlit to create a web app that processes URLs of news articles, 
             embeds the content using Ollama LLaMA3, stores it in a FAISS index, and answers user 
             queries based on the content.
"""

import os
import pickle
import time
from dotenv import load_dotenv
import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

# Load environment variables
load_dotenv()

# Set environment variables for LangChain tracing and API key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Set up Streamlit interface
st.title("InsightOwl: News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Collect URLs from user input
urls = [st.sidebar.text_input(f"URL {i + 1}") for i in range(3)]

# Button to trigger URL processing
process_url_clicked = st.sidebar.button("Process URLs")

# Path to save the FAISS index
faiss_index_path = "faiss_store.pkl"

# Placeholder for main processing messages
main_placeholder = st.empty()

# Initialize the Ollama LLaMA3 language model
llm = OllamaLLM(model="llama3")

if process_url_clicked:
    # Load data from URLs
    main_placeholder.text("Data Loading... Started... ✅✅✅")
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()

    # Split data into manageable chunks
    main_placeholder.text("Text Splitter... Started... ✅✅✅")
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    split_documents = text_splitter.split_documents(documents)

    # Create embeddings and build FAISS index
    main_placeholder.text("Embedding Vector Started Building... ✅✅✅")
    embeddings = OllamaEmbeddings(model="llama3")
    faiss_index = FAISS.from_documents(split_documents, embeddings)

    # Save the FAISS index to a pickle file
    with open(faiss_index_path, "wb") as f:
        pickle.dump(faiss_index, f)

# Collect user query input
query = main_placeholder.text_input("Question:")

if query:
    if os.path.exists(faiss_index_path):
        # Load the FAISS index from the pickle file
        with open(faiss_index_path, "rb") as f:
            faiss_index = pickle.load(f)

        # Set up the retrieval chain
        retriever = faiss_index.as_retriever()
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=retriever)

        # Get the result by invoking the chain with the user's query
        result = chain({"question": query}, return_only_outputs=True)

        # Display the answer
        st.header("Answer")
        st.write(result["answer"])

        # Display the sources, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            for source in sources.split("\n"):  # Split the sources by newline
                st.write(source)
