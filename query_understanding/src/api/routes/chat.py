import fastapi

from src.api.dependencies.repository import get_repository

from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

router = fastapi.APIRouter(prefix="/chat", tags=["chat"])


@router.post(
    "/user_message",
    name="chat:user_message",
)
async def user_message(
    
) -> dict:
    """
    Se recibe la consulta que hace el usuario
    """
    return {"message":"se recibe lo que el usuario escribe"}

@router.get(
    "/user_answer",
    name="chat:user_answer",
)
async def user_answers(
    
) -> dict:
    """
    Se envia al usuario las respuestas a su pregunta 
    """
    return {"message":"se envia la respuesta de chatgpt al chat con el usuario"}


@router.get(
    "/user_questions",
    name="chat:user_questions",
    
)
async def user_questions(
    
) -> dict:
    """
    Se envia al usuario 3 posibles preguntas que tenga sobre la respuesta de le da el chatbot
    """
    return {"message":"el backend online le envia al frontend las posibles preguntas que tenga el usuario segun su respuesta"}