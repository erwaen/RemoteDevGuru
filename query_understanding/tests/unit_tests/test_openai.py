"""Test open ai domain"""


from src.repository.openai_repository import BaseLlmRepository


class OpenAIMock(BaseLlmRepository):
    """Mockeamos la funcionaladidad de openai con todos los posibles casos de uso"""
    def get_coincidence_embedding(self, message: str, result_number: int = 5):
        respuesta = []
        for i in range(result_number):
            respuesta.append(str(i))
        return respuesta
    def get_coincidence_externo(self, message: str, result_number: int = 5) -> list[str]:
        pass

def test_similar_text() -> None:
    result_number = 10
    message = "Hola"
    res: list = OpenAIMock().get_coincidence_embedding(message=message, result_number=result_number)
    assert res is list
    assert result_number is len(res)