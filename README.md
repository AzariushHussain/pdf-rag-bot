
## Prerequisites

- Python 3.8+
- [Pinecone API](https://www.pinecone.io/) account
- [Cohere API](https://cohere.ai/) account
- Docker (optional, for containerization)

### Clone the repository:
```bash
git clone https://github.com/AzariushHussain/pdf-rag-bot.git
```

### Navigate to the project directory:
```bash
cd .\question-answer-bot\
```
### Set up the environment variables by creating a .env file in the root of your project and add the following:
- PINECONE_API_KEY
- CO_API_KEY

### Python Libraries

The following Python libraries are required:
- `streamlit`
- `cohere`
- `pinecone-client`
- `pymupdf`
- `python-dotenv`

You can install them by running:
```bash
pip install -r requirements.txt
```

### Run the app with Streamlit:
```bash
streamlit run app.py
```