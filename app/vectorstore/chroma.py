from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from core.config import os


embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)

vector_store = Chroma(
    collection_name="chatbot_documents",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)