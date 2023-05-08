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
    credentials: dict,
    #auth_repository = Depends(get_repository)
) -> dict:
    """
    Iniciar Sesion

    Preguntar al servidor si tiene al usuario y contrasena registrados()

    Parametros: 
        - credenciales del usuario: correo y contrasena

    Retorno:
        - Confirmacion o Negacion de la existencia del usuario en el servidor

    """
    try:
        user = await auth_repository.validate_user(credentials)
        access_token = jwt_generator.create_access_token(user)
        return {"access_token": access_token}
    except EntityAlreadyExists:
        raise http_exc_400_credentials_bad_signup_request()

@router.post(
    path="/signin",
    name="auth:signin",
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)

async def signin(
    credentials: dict,
    #auth_repository = Depends(get_repository)
) -> dict:
    """
    Iniciar Sesion

    Preguntar al servidor si tiene al usuario y contrasena registrados()

    Parametros: 
        - credenciales del usuario: correo y contrasena

    Retorno:
        - Confirmacion o Negacion de la existencia del usuario en el servidor

    """
    try:
        user = await auth_repository.validate_user(credentials)
        access_token = jwt_generator.create_access_token(user)
        return {"access_token": access_token}
    except EntityAlreadyExists:
        raise http_exc_400_credentials_bad_signin_request()


@router.post(
    path="/logout",
    name="auth:logout",
)
async def logout(
    # This endpoint does not require credentials since it is only logging out the current user
) -> dict:
    """
    Cerrar sesion

    Cerrar la sesion del usuario actual, para que ya no pueda acceder al servicio()

    Parametros: 
        - No se requieren credenciales ya que solo se está cerrando la sesion del usuario actual

    Retorno:
        - Sesion cerrada correctamente

    """
    # Code to log out the current user and remove their authentication credentials
    return {"message":"sesion cerrada"}