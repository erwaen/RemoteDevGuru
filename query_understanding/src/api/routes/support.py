import fastapi

from src.api.dependencies.repository import get_repository

from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

router = fastapi.APIRouter(prefix="/support", tags=["support"])

@router.post(
    "/user_support",
    name="support:user_support",
    
)
async def user_support(
    
) -> dict:
    """
    Soporte de usuario

    el usuario envia un formulario con un problema que haya tenido al utilizar el chatbot()

    Parametros: 
        - nombre de usuario y una descripcion del problema que ha tenido

    Retorno:
        - 
    
    """
    return {"message":"se recibe los errores/problemas que envia el usuario"}

