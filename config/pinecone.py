import os
from pinecone import Pinecone, ServerlessSpec

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")

def init_pinecone():
    return Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

def get_pinecone_index(index_name="question-answer-bot"):
    pc = init_pinecone()
    
    index_names = pc.list_indexes().names()
    if index_name in index_names:
        index = pc.Index(index_name)
    else:
        index = pc.create_index(
            name=index_name,
            dimension=1024,  
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    return index
