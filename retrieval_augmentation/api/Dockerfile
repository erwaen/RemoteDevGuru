FROM python:latest

COPY api_script.py .

RUN pip3 install "fastapi[all]" langchain pinecone-client

EXPOSE 8000

CMD [ "uvicorn", "api_script:app" ]