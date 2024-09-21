import streamlit as st
from utils.pdf_utils import extract_text_from_pdf, truncate_text
from utils.embedding_utils import final_response, generate_embeddings
from utils.pinecone_utils import upsert_document_chunks, query_similar_chunks
from config.pinecone import get_pinecone_index

st.title("PDF Question-Answer Bot")
st.write("""
Upload a PDF document, and ask questions based on its content. 
The bot will return the most relevant text based on your query.
""")

index = get_pinecone_index()

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    st.write("Processing your PDF...")
    pdf_text = extract_text_from_pdf(uploaded_file)
    st.write("Extracted Text:")
    st.text_area("", pdf_text, height=300)

    def create_overlapping_chunks(text, chunk_size=100, overlap=20):
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size - overlap):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks

    text_chunks = create_overlapping_chunks(pdf_text)
    st.write("Generating embeddings for the document...")
    embeddings = generate_embeddings(text_chunks)
    st.write("Indexing document in Pinecone...")
    upsert_document_chunks(text_chunks, embeddings)
    st.write("Document successfully indexed.")
    st.write("Now, you can ask a question based on the uploaded PDF.")
    question = st.text_input("Enter your question")
    
    if question:
        question_embedding = generate_embeddings([question])[0]
        st.write("Fetching the most relevant information...")
        results = query_similar_chunks(question_embedding, top_k=3)
        best_match = max(results["matches"], key=lambda match: match['score'])
        response = final_response(text_chunks[int(best_match['id'])], question)
        st.write("Best Answer:")
        st.write(response)
        st.write("Document segments referred:")
        st.write(truncate_text(text_chunks[int(best_match['id'])]))
