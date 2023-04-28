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
    Aqui se registra el correo del usuario que sera vinculado a su cuenta
    """
    return {"message":"usuario registrado correctamente"}


@router.post(
    path="/signin",
    name="auth:signin",
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def signin(
    
) -> dict:
    """
    Para iniciar sesion con un usuario ya registrado con su correo
    """
    return {"message":"el usuario inicio sesion correctamente"}


@router.post(
    path="/logout",
    name="auth:logout",
)
async def logout(
    
) -> dict:
    """
    Cerrar sesion y desconectarse del backend
    """
    return {"message":"el usuario ha cerrado sesion correctamente"}