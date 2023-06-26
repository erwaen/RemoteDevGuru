from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

class Query(BaseModel):
    query_content: str

@asynccontextmanager
async def lifespan(app: FastAPI):



app = FastAPI(lifespan=lifespan)

app = FastAPI()

@app.post("/")
async def process_query(query: Query):
    return query
