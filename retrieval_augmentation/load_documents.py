import sys
import os
import pinecone
from langchain.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from getpass import getpass

if len(sys.argv) < 2:
    print(
        "You must provide the directory in which the documents"\
        " are stored.")
    exit()

# Get the name of the directory in which the JSON files are stored.
directory = sys.argv[1]

# List every JSON document in the directory.
directory = './linkedin_docs'
json_docs = []
for entry in os.listdir(directory):
    path = os.path.join(directory, entry)
    if os.path.isfile(path):
        json_docs.append(path)

linked_in = input("Is the data from linked in? Enter Y (yes) or N (no): ")
jq_schema = '.[].content'
if linked_in.lower() == 'y':
    jq_schema='.[].detalle_del_puesto'

# Load the JSON documents stored in the file system.
for json_doc in json_docs:
    loader = JSONLoader(
        file_path=json_doc,
        jq_schema=jq_schema)

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=0)

docs = text_splitter.split_documents(documents)

# Get the Pinecone API key.
PINECONE_API_KEY = getpass("Pinecone API Key: ")
# Get the Pinecone environment (found in the API section).
PINECONE_ENV = input("Pinecone environment: ")

# Set the name for the new Pinecone index.
index_name = 'test'

# Select the given Pinecone index.
index = pinecone.Index(index_name)

# Get OpenAI API key.
OPENAI_API_KEY = getpass("OpenAI API Key: ")
model = 'text-embedding-ada-002'

# Set the text embedding model. We will use one from OpenAI.
embeddings = OpenAIEmbeddings(
    model=model,
    openai_api_key=OPENAI_API_KEY
)

Pinecone.from_documents(docs, embeddings, index_name=index_name)

print(
    f"All of the documents from the directory {directory}"\
    " have been embedded and added to the Pinecone"\
    " index {index_name}.")
