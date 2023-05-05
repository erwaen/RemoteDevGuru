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
    Query del usuario

    Se recibe la consulta del usuario, para ser procesada y enviada a las diferentes APIs()

    Parameters: 
        - query y otros parametros predefinidos por frontend

    Response:
        - 

    """
    return {"message":"se recibe lo que el usuario escribe"}

@router.get(
    "/user_answer",
    name="chat:user_answer",
)
async def user_answers(
    
) -> dict:
    """
    Respuesta al usuario

    El usuario obtiene la respuesta a su consulta anterior()

    Parametros: 
        - 

    Retorno:
        - llas 3 respuestas de la IA

    """
    return {"message":"se envia la respuesta de chatgpt al chat con el usuario"}


@router.get(
    "/user_questions",
    name="chat:user_questions",
    
)
async def user_questions(
    
) -> dict:
    """
    Preguntas del usuario

    Se envian 3 posibles preguntas que podria tener el usuario sobre la respuesta que le da la IA()

    Parametros: 
        - la respuesta que dio la IA

    Retorno:
        - C3 posibles preguntas cortas
        
    """
    return {"message":"el backend online le envia al frontend las posibles preguntas que tenga el usuario segun su respuesta"}