FROM python:latest

COPY [ "load_documents.py", "aux_methods.py", "requirements.txt", "./" ]

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "load_documents.py" ]