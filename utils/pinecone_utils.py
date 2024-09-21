from config.pinecone import get_pinecone_index
import numpy as np
from sklearn.decomposition import PCA

def reduce_dimension(embeddings, target_dimension=1024):
    """Reduces the dimensionality of embeddings to target_dimension using PCA."""
    if embeddings.shape[1] > target_dimension:
        if embeddings.shape[0] > target_dimension:
            pca = PCA(n_components=target_dimension)
            embeddings = pca.fit_transform(embeddings)
        else:
            print(f"Insufficient samples for PCA. Keeping original dimensions: {embeddings.shape[1]}")
    return embeddings

def upsert_document_chunks(chunks, embeddings):
    index = get_pinecone_index()

    embeddings = np.array(embeddings)
    embeddings = reduce_dimension(embeddings)
    embeddings = [embedding.tolist()[:1024] for embedding in embeddings]
    vectors = [(str(i), embedding) for i, embedding in enumerate(embeddings)]
    try:
        index.upsert(vectors=vectors)
    except Exception as e:
        print(f"Error upserting vectors: {e}")
        raise

def normalize_vector(vector):
    """Normalizes the vector to unit length."""
    vector = np.array(vector)  
    norm = np.linalg.norm(vector)
    
    print(f"Norm before normalization: {norm}")
    
    if norm == 0:
        print("Warning: Normalizing a zero vector.")
        return vector 
    return vector / norm

def validate_embedding(embedding):
    """Ensure no NaN, Inf, or very small values are in the embedding."""
    if np.isnan(embedding).any():
        raise ValueError("Query embedding contains NaN values.")
    if np.isinf(embedding).any():
        raise ValueError("Query embedding contains Inf values.")
    if (embedding < -1e6).any() or (embedding > 1e6).any():
        raise ValueError("Query embedding contains extremely large values.")
    
    embedding = np.clip(embedding, -1e3, 1e3)  
    return embedding

def query_similar_chunks(query_embedding, top_k=3):
    index = get_pinecone_index()

    query_embedding = np.array(query_embedding)
    if query_embedding.shape[0] != 1024:
        raise ValueError(f"Query embedding must have 1024 dimensions, but it has {query_embedding.shape[0]} dimensions.")
    query_embedding = validate_embedding(query_embedding)
    query_embedding = normalize_vector(query_embedding)
    query_embedding = [query_embedding.tolist()]
    try:
        response = index.query(vector=query_embedding, top_k=top_k)
    except Exception as e:
        print(f"Error querying Pinecone: {e}")
        raise

    return response
