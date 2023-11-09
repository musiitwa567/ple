from dotenv import load_dotenv
import streamlit as st
from langchain import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.llms import GooglePalm
from langchain.vectorstores import Qdrant
from langchain.embeddings import GooglePalmEmbeddings
import qdrant_client
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"]=""
 

def get_vector_store():
    
    client = qdrant_client.QdrantClient(
        os.getenv("QDRANT_HOST"),
        api_key=os.getenv("QDRANT_API_KEY")
    )
    
    embeddings = GooglePalmEmbeddings()

    vector_store = Qdrant(
        client=client, 
        collection_name=os.getenv("QDRANT_COLLECTION_NAME"), 
        embeddings=embeddings,
    )
    
    return vector_store

def main():
    load_dotenv()
    
    st.set_page_config(page_title="Ask Qdrant")
    st.header("Ask your remote database 💬")
    
    # create vector store
    vector_store = get_vector_store()
  
    # create chain 
    qa = RetrievalQA.from_chain_type(
        llm=HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta",model_kwargs={"temperature":0.6,"max_length":128,"context_window":2048,"max_new_tokens":256}),
        chain_type="stuff",
        retriever=vector_store.as_retriever()
    )

    # show user input
    user_question = st.text_input("Ask a question about your PDF:")
    if user_question:
        st.write(f"Question: {user_question}")
        answer = qa.run(user_question)
        st.write(f"Answer: {answer}")
    
        
if __name__ == '__main__':
    main()
