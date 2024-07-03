from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings

def get_embeddings():
    embeddings = BedrockEmbeddings(
        credentials_profile_name="default", region_name="us-east-1"

    )
    return embeddings