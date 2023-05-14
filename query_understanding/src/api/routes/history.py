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
    "/chat_history/{user_id}",
    name="history:chat_history",
)
async def chat_history(
    user_id: str,
    #repository = Depends(get_repository)
) -> dict:
    """
    Historial de chats

    el usuario consulta al servidor el historial de chats que tiene guardados()

    Parametros: 
        - nombre de usuario

    Retorno:
        - lista de chats guardados

    """
    chat_history = await repository.history.get_chat_history(user_id) # Get the chat history for the given user_id from the repository
    return {"chat_history": chat_history} # Return the chat history as a dictionary

@router.delete(
    "/chat_delete/{user_id}/{chat_id}",
    name="history:chat_delete",
)
async def chat_delete(
    user_id: str,
    chat_id: str,
    #repository = Depends(get_repository)
) -> dict:
    """
    Eliminar chats

    El usuario envia el ID de un chat para eliminarlo()

    Parametros: 
        - nombre de usuario y id del chat

    Retorno:
        - confirmacion de eliminacion del chat
    
    """
    try:
        await repository.history.delete_chat(user_id, chat_id) # Delete the chat with the given chat_id for the given user_id from the repository
        return {"message": f"El chat con ID {chat_id} ha sido eliminado exitosamente"} # Return success message
    except EntityDoesNotExist as e:
        raise http_exc_400_credentials_bad_signin_request(e.custom_message) # Raise exception if chat is not found in the repository