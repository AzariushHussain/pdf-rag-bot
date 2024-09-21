from sklearn.decomposition import PCA
import numpy as np

def reduce_dimensions(embeddings, target_dim=1024):
    pca = PCA(n_components=target_dim)
    reduced_embeddings = pca.fit_transform(embeddings)
    return reduced_embeddings