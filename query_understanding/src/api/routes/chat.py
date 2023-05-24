import fastapi
from src.llms.domain.openai import OpenAiDomain

from src.config.manager import settings
from src.api.dependencies.repository import get_repository
from src.api.routes.chatgpt import mensaje

from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

router = fastapi.APIRouter(prefix="/chat", tags=["chat"])

@router.post(
    "/user_message",
    name="chat:message",
)
async def user_message(
    message: str, # Se recibe el mensaje del usuario
) -> dict:
    """
    Endpoint para manejar las solicitudes de mensajes del usuario. 
    Recibe los mensajes enviados por el usuario en el chat, los procesa 
    y envía una respuesta al usuario. 

    Parameters: 
        - message: mensaje enviado por el usuario

    Returns:
        - Mensaje de respuesta generado por la IA o información relevante del indexador offline
    """
    resp = OpenAiDomain().getSimiliarText(message=message)
    # return {"message": resp['texto']}
    return {"message": resp}

# @router.get('/embending')
# async def embedding():
#     OpenAiDomain().embedding()
#     return 'success'
