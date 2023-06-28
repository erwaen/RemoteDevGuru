FROM python:latest

COPY [ "load_documents.py", "aux_methods.py", "./" ]

RUN pip3 install langchain pinecone-client tiktoken

ENTRYPOINT [ "python3", "load_documents.py" ]