import fastapi
import openai


from src.api.dependencies.repository import get_repository

from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

openai.api_key = API_KEY

router = fastapi.APIRouter(prefix="/chat", tags=["chat"])

@router.post(
    "/user_message",
    name="chat:message",
)
async def user_message(
    message: str, # Se recibe el mensaje del usuario
    use_offline_info: bool = False, # Opciones de procesamiento según el origen de la respuesta
) -> dict:
    """
    Endpoint para manejar las solicitudes de mensajes del usuario. 
    Recibe los mensajes enviados por el usuario en el chat, los procesa 
    y envía una respuesta al usuario. 

    Parameters: 
        - message: mensaje enviado por el usuario
        - use_offline_info: booleano para indicar si se empleará información del indexador offline

    Returns:
        - Mensaje de respuesta generado por la IA o información relevante del indexador offline, 
        según lo especificado en use_offline_info.
    """
    #a partir de aqui llamaremos al modulo de chatgpt para enviar el query del usuario

    
    return {"message":respuestas()}