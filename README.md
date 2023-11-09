# ple
# Ask Qdrant

This Streamlit app allows you to ask questions about your PDF documents using the LangChain framework with Qdrant vector store.

## Setup

Before running the application, make sure to set up the necessary environment variables in a `.env` file. You can use the following template:

```plaintext
# .env file

# Qdrant Configuration
QDRANT_HOST=<QDRANT_HOST_URL>
QDRANT_API_KEY=<QDRANT_API_KEY>
QDRANT_COLLECTION_NAME=<QDRANT_COLLECTION_NAME>

# Hugging Face Hub Configuration
HUGGINGFACEHUB_API_TOKEN=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
pip install streamlit langchain qdrant-client
