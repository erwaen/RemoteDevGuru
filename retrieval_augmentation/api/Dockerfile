FROM python:latest

COPY [ "api_script.py", "requirements.txt", "./" ]

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "api_script:app" ]