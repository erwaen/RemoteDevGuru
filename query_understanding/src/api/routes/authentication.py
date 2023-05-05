import fastapi

from src.api.dependencies.repository import get_repository

from src.securities.authorizations.jwt import jwt_generator
from src.utilities.exceptions.database import EntityAlreadyExists
from src.utilities.exceptions.http.exc_400 import (
    http_exc_400_credentials_bad_signin_request,
    http_exc_400_credentials_bad_signup_request,
)

router = fastapi.APIRouter(prefix="/auth", tags=["authentication"])


@router.post(
    "/signup",
    name="auth:signup",
    status_code=fastapi.status.HTTP_201_CREATED,
    
)
async def signup(
    
) -> dict:
    """
    Crear usuario

    Enviar el usuario nuevo al servidor()

    Parametros: 
        - credenciales nuevas del usuario: correo y contrasena

    Retorno:
        - Confirmacion de que el usuario se registro correctamente

    """
    return {"message":"usuario registrado o no registrado"}


@router.post(
    path="/signin",
    name="auth:signin",
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def signin(
    
) -> dict:
    """
    Iniciar Sesion

    Preguntar al servidor si tiene al usuario y contrasena registrados()

    Parametros: 
        - credenciales del usuario: correo y contrasena

    Retorno:
        - Confirmacion o Negacion de la existencia del usuario en el servidor

    """
    return {"message":"estado de inicio de sesion"}


@router.post(
    path="/logout",
    name="auth:logout",
)
async def logout(
    
) -> dict:
    """
    Cerrar sesion

    Cerrar la sesion del usuario actual, para que ya no pueda acceder al servicio()

    Parametros: 
        - credenciales del usuario: correo y contrasena

    Retorno:
        - Sesion cerrada correctamente

    """
    return {"message":"sesion cerrada"}