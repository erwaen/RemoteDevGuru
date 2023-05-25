
from pydantic import BaseModel


class ChatResponse(BaseModel):
    """Schema de respuesta del ep user_message"""
    respuestas: list[str]
    preguntas_sugeridas: list[str]
