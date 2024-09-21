import cohere
import os
from dotenv import load_dotenv
import numpy as np
from sklearn.decomposition import PCA

load_dotenv()

COHERE_API_KEY = os.getenv("CO_API_KEY")
co = cohere.Client(COHERE_API_KEY)

def generate_embeddings(text_list):
    embeddings = co.embed(texts=text_list, model="embed-english-light-v2.0").embeddings
    embeddings = np.array(embeddings)
    
    return embeddings

def final_response(text, question):
    response = co.generate(
        model='command-xlarge-nightly',
        prompt=f"Based on the following text, answer the question: {question}\n\nText: {text}",
        max_tokens=100
    )
    return response.generations[0].text
