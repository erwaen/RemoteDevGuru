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

    return {}


@router.post(
    path="/signin",
    name="auth:signin",
    status_code=fastapi.status.HTTP_202_ACCEPTED,
)
async def signin(
    
) -> dict:

    return {}
