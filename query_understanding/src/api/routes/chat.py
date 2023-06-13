"""View para conexion con el chat"""

from fastapi import APIRouter, status, Query, HTTPException
from src.api.dependencies.indice_mock import IndiceMaxLenException
from src.models.schemas.chat_schemas import ChatResponse
from src.repository.openai_repository import OpenAiRepository


router = APIRouter(prefix="/chat", tags=["chat"])

@router.get(
    "/",
    name="chat:message",
    response_model=ChatResponse,
    status_code= status.HTTP_200_OK,
    summary="Respuesta chat"
)
async def chat_message(
    prompt: str = Query(..., example="Hola chat remote"),
) -> ChatResponse:
    """
    Endpoint para manejar las solicitudes de mensajes del usuario. 
    Recibe los mensajes enviados por el usuario en el chat, los procesa 
    y envía una respuesta al usuario. 

    Parameters: 
        - prompt: mensaje enviado por el usuario

    Returns:
        - respuestas: Se retorna una lista con dos posibles respuestas
            [
                0: Información relevante del indexador offline
                1: Respuesta generado por la IA 
            ]
        - preguntas_sugeridas: Lista de posibles preguntas futuras del usuario
    """
    openai = OpenAiRepository()
    try:
        responses = openai.get_chat_response(message=prompt, result_number=1)
    except IndiceMaxLenException as e:
        raise HTTPException(status_code=400, detail=e)

    return {
            "respuestas": responses,
            "preguntas_sugeridas": openai.sugerence_questions(question=prompt)
        }

@router.get('/stream')
async def stream(
    prompt: str = Query(..., example="Hola chat remote"),
):
    """Ejemplo de implementar chat gpt con stream mode activo
    En este caso no es recomendable usar
    Se deberia de usar websockets para la integracion"""
    OpenAiRepository().chat_stream_mode(prompt=prompt)
    return {}
