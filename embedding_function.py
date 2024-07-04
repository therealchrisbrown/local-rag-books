from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings

def get_embeddings():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings