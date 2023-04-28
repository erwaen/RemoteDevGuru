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
    Se le envia al usuario la lista de chats que tiene guardado
    """
    return {"message":"se devuelve el historial de chats del usuario"}

@router.delete(
    "/chat_delete",
    name="history:chat_delete",
)
async def chat_delete(
    
) -> dict:
    """
    El usuario solicita la eliminacion de uno o varios chats registrados
    """
    return {"message":"se elimina el chat que el usuario marca"}

