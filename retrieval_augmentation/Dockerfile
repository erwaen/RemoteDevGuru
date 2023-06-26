FROM python:latest

ADD api_script.py .

RUN pip3 install "fastapi[all]" langchain pinecone-client

CMD [ "uvicorn", "api_script:app" ]