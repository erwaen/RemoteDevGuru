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
    "/send_report",
    name="support:send_report",
)
async def send_report(
    report_data: dict
) -> None:
    """
    Endpoint que maneja la recepción de informes por parte de los usuarios.

    Parametros:
        report_data: un diccionario con la información del informe.

    Retorno:
        None
    """
    try:
        repository = get_repository()
        await repository.create_report(report_data)
    except EntityAlreadyExists:
        pass