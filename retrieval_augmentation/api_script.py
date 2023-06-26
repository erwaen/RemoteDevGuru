from fastapi import FastAPI
from pydantic import BaseModel
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from getpass import getpass

class Query(BaseModel):
    query_content: str

# Get the Pinecone API key.
PINECONE_API_KEY = getpass("Pinecone API Key: ")
# Get the Pinecone environment (found in the API section).
PINECONE_ENV = input("Pinecone environment: ")

# Initilize a Python "instance" of Pinecone.
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

# Get OpenAI API key.
OPENAI_API_KEY = getpass("OpenAI API Key: ")
model = 'text-embedding-ada-002'

# Set the text embedding model. We will use one from OpenAI.
embeddings = OpenAIEmbeddings(
    model=model,
    openai_api_key=OPENAI_API_KEY
)

# Set the name for the new Pinecone index.
index_name = 'test'

docsearch = Pinecone.from_existing_index(
    index_name, embeddings, text_key='text')

app = FastAPI()

@app.post("/")
async def process_query(query: Query):
    return docsearch.similarity_search(query.query_content)
