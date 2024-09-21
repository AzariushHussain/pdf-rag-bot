
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

## Demo:

![alt text](<Screenshot (8).png>)

- Above is the main sccreen of the project<br><br>


![alt text](<Screenshot (9).png>)

- Upload the pdf of your choice<br><br>

![alt text](<Screenshot (10).png>)

- Text will be extracted from the document and indexed.<br><br>

![alt text](<Screenshot (11).png>)

- Put in the query you want the answer to<br><br>

![alt text](<Screenshot (12).png>)

- In response you will receive the appropriate answeer and the portion of document referred to.<br><br>

![alt text](<Screenshot (13).png>)
- Incase there is no deta related to the query, you  will receive a text saying "The text does not provide information about ...." and also the portion that was closest and referred.