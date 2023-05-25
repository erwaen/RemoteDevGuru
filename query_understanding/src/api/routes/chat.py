"""View para conexion con el chat"""

from fastapi import APIRouter, status, Query
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
    return {
            "respuestas": openai.get_coincidence(message=prompt, result_number=1),
            "preguntas_sugeridas": openai.get_coincidence_externo(message=f"Sugiereme 2 preguntas, teniendo en cuenta que la pregunta anterior fue {prompt}")
        }

# @router.get('/embending')
# async def embedding():
#   verificar si el archivo es de tipo pdf
#     OpenAiDomain().embedding()
#     return 'success'
