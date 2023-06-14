"""View para conexion con el chat"""

import asyncio
from typing import Awaitable, Callable, Optional, Union
from fastapi import APIRouter, status, Query, HTTPException
from src.api.dependencies.indice_mock import IndiceMaxLenException
from src.models.schemas.chat_schemas import ChatResponse
from src.repository.openai_repository import OpenAiRepository
from fastapi.responses import StreamingResponse

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


class ChatOpenAIStreamingResponse(StreamingResponse):
    """Streaming response for openai chat model, inheritance from StreamingResponse."""
    Sender = Callable[[Union[str, bytes]], Awaitable[None]]
    from starlette.types import Send

    def __init__(
            self,
            generate: Callable[[Sender], Awaitable[None]],
            status_code: int = 200,
            media_type: Optional[str] = None,
    ) -> None:
        super().__init__(content=iter(()), status_code=status_code, media_type=media_type)
        self.generate = generate

    async def stream_response(self, send: Send) -> None:
        """Rewrite stream_response to send response to client."""
        await send(
            {
                "type": "http.response.start",
                "status": self.status_code,
                "headers": self.raw_headers,
            }
        )

        async def send_chunk(chunk: Union[str, bytes]):
            if not isinstance(chunk, bytes):
                chunk = chunk.encode(self.charset)
            await send({"type": "http.response.body", "body": chunk, "more_body": True})

        # send body to client
        await self.generate(send_chunk)

        # send empty body to client to close connection
        await send({"type": "http.response.body", "body": b"", "more_body": False})
        
@router.get('/stream')
async def stream(
    prompt: str = Query(..., example="Hola chat remote"),
):
    """Ejemplo de implementar chat gpt con stream mode activo
    """
    return ChatOpenAIStreamingResponse(OpenAiRepository().chat_stream_mode(prompt=prompt), media_type='text/event-stream')
