import fastapi

from src.api.dependencies.repository import get_repository

from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

router = fastapi.APIRouter(prefix="/history", tags=["history"])

@router.get(
    "/chat_history",
    name="history:chat_history",
)
async def chat_history(
    
) -> dict:
    """
    Historial de chats

    el usuario consulta al servidor el historial de chats que tiene guardados()

    Parametros: 
        - nombre de usuario

    Retorno:
        - lista de chats guardados

    """
    return {"message":"se devuelve el historial de chats del usuario"}

@router.delete(
    "/chat_delete",
    name="history:chat_delete",
)
async def chat_delete(
    
) -> dict:
    """
    Eliminar chats

    El usuario envia el ID de un chat o varios chats que desea eliminar()

    Parametros: 
        - nombre de usuario y id del chat

    Retorno:
        - confirmacion de eliminacion del chat
    
    """
    return {"message":"se elimina el chat que el usuario marca"}

