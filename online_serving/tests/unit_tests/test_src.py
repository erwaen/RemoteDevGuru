import fastapi

import source
from source.main import backend_app


def test_source_version() -> None:

    assert source.__version__ == "0.0.1"


def test_application_is_fastapi_instance() -> None:

    assert isinstance(backend_app, fastapi.FastAPI)
    assert backend_app.redoc_url == "/redoc"
    assert backend_app.docs_url == "/docs"
    assert backend_app.openapi_url == "/openapi.json"
    assert backend_app.redoc_url == "/redoc"
