import sys
import pinecone
import tiktoken
from langchain.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from getpass import getpass

# Make sure that the user inputs a directory name as argument.
if len(sys.argv) < 2:
    print(
        "You must provide the directory in which the documents"\
        " are stored.")
    exit()

# Get the name of the directory in which the JSON files are stored.
json_doc = sys.argv[1]

# If the data is scrapped from LinkedIn, we have to embed the
# "detalle_del_puesto" field. If it is from a website, we embed
# the "content".
linked_in = input("Is the data from linkedIn? Enter Y (yes) or N (no): ")
jq_schema = '.[].content'
if linked_in.lower() == 'y' or linked_in.lower() == 'yes':
    jq_schema='.[].detalle_del_puesto'

# Load the JSON document stored in the file system.
loader = JSONLoader(file_path=json_doc, jq_schema=jq_schema)
documents = loader.load()

# Set the tokenizer
tokenizer = tiktoken.get_encoding('cl100k_base')

# Create a length function to know the amount of tokens of a given
# chunk of text.
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)

# Set the text splitter to separate a large documents into smaller
# chunks, because LLMs accept a limited amount of tokens.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=20,  # number of tokens overlap between chunks
    length_function=tiktoken_len,
    separators=['\n\n', '\n', ' ', '']
)

# Split the documents into smaller chunks of text.
docs = text_splitter.split_documents(documents)

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
index_name = 'remote-dev-guru'

Pinecone.from_documents(docs, embeddings, index_name=index_name)

print(
    f"All of the documents from the directory {directory}"\
    f" have been embedded and added to the Pinecone"\
    f" index {index_name}.")
