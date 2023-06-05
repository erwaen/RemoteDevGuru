import tiktoken
import pinecone
from uuid import uuid4
from langchain.document_loaders import UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from tqdm.auto import tqdm
from getpass import getpass

# Get the Pinecone API key.
PINECONE_API_KEY = getpass("Pinecone API Key: ")
# Get the Pinecone environment (found in the API section).
PINECONE_ENV = input("Pinecone environment: ")

# Set the name for the new Pinecone index.
index_name = 'stanford-enc-retrieval-augmentation'

# Initilize a Python "instance" of Pinecone.
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

# If the given index doesn't exist, create a new one.
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        name=index_name,
        metric='dotproduct',
        dimension=1536 # 1536 dim of text-embedding-ada-002
    )

# Select the given Pinecone index.
index = pinecone.GRPCIndex(index_name)

# Load an HTML document stored in the file system.
loader = UnstructuredHTMLLoader(
    "./stanford-encyclopedia-entries/plato.stanford.edu/"\
    "entries/political-obligation/index.html"
    )

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

# Set the OpenAI embedding model.
model = 'text-embedding-ada-002'

# Get OpenAI API key.
OPENAI_API_KEY = getpass("OpenAI API Key: ")

# Set the text embedding model. We will use one from OpenAI.
embed = OpenAIEmbeddings(
    model=model,
    openai_api_key=OPENAI_API_KEY
)

# The text for the knowledge base.
data = loader.load()

# Array to store the processed data.

batch_limit = 100

texts = []
metadatas = []


# For every document (webpage) divide the text data into smaller chunks
# and reformat every chunk of text.
for doc in tqdm(data):

    # Save the url of the page in the "source" field of the metadata.
    metadata = {
        'source': doc.metadata['source'].replace(
        './stanford-encyclopedia-entries', 'https://')
    }

    # Split the page into chunks of text.
    chunks = text_splitter.split_text(doc.page_content)

    chunks_metadatas = [{
        "chunk": j, "text": text, **metadata
    } for j, text in enumerate(chunks)]

    texts.extend(chunks)
    metadatas.extend(chunks_metadatas)

    # if we have reached the batch_limit we can add texts
    if len(texts) >= batch_limit:
        ids = [str(uuid4()) for _ in range(len(texts))]
        embeds = embed.embed_documents(texts)
        index.upsert(vectors=zip(ids, embeds, metadatas))
        texts = []
        metadatas = []

if len(texts) > 0:
    ids = [str(uuid4()) for _ in range(len(texts))]
    embeds = embed.embed_documents(texts)
    index.upsert(vectors=zip(ids, embeds, metadatas))

# Normal Pinecone index.
index = pinecone.Index(index_name)

text_field = "text"

vectorstore = Pinecone(
    index, embed.embed_query, text_field
    )

# completion llm
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

qa = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

print(qa("What are the two problems that the divine command theory faces as a theory of political obligation?"))
