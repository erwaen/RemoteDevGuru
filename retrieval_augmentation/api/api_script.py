import pinecone
import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain

class Query(BaseModel):
    query_content: str

# Initilize a Python "instance" of Pinecone.
pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV")
)

# Set the text embedding model. We will use one from OpenAI.
embeddings = OpenAIEmbeddings(
    model='text-embedding-ada-002',
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Set the name for the new Pinecone index.
index_name = 'remote-dev-guru'

# Initialize a vectorstore from an existing Pinecone index.
vectorstore = Pinecone.from_existing_index(
    index_name, embeddings, text_key='text')

# Completion LLM, for the Q&A functionality.
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name='gpt-3.5-turbo',
    temperature=0.0
    )


app = FastAPI()

# This endpoint does a similarity search with whatever is passed
# as a query. It returns the 4 most relevant documents from the
# vector database.
@app.post("/similarity_search")
async def process_query(query: Query):
    return {
        'results': vectorstore.similarity_search(query.query_content)
        }

# This endpoint answers questions based on information from the
# vector database. It also returns the sources of information.
@app.post("/qa")
async def process_query(query: Query):
    qa = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa(query.query_content)
