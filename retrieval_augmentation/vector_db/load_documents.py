import sys
import os
import pinecone
import tiktoken
from langchain.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
from aux_methods import (
    user_input_to_bool,
    metadata_fun_linkedin,
    metadata_fun_web
    )

# Make sure that the user inputs a file name as argument.
if len(sys.argv) < 2:
    print("You must provide a file from which to extract the data.")
    exit()

# Get the name of the JSON file passed as argument to the script.
json_doc = sys.argv[1]

# Load the variables from the .env file as environment variables.
load_dotenv()

# If the data is scrapped from LinkedIn, we have to embed the
# "detalle_del_puesto" field. If it is from a website, we embed
# the "content" field.
linked_in = user_input_to_bool(
    "Is the data from LinkedIn? Enter Y (yes) or N (no): ")
content_key = 'detalle_del_puesto' if linked_in else 'content'

# Load the JSON document stored in the file system.
loader = JSONLoader(
    file_path=json_doc,
    jq_schema='.[]',
    content_key=content_key,
    # The scrapper for LinkedIn is different from the one used for
    # scrapping data from other websites.
    metadata_func=metadata_fun_linkedin if linked_in else metadata_fun_web
    )
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

# Vectorize the documents and upsert the vector to the Pinecone index.
Pinecone.from_documents(docs, embeddings, index_name=index_name)

# Print a success message for the user.
print(
    f"All of the documents from the directory {json_doc}"\
    f" have been embedded and added to the Pinecone"\
    f" index {index_name}.")
