import openai
from src.config.manager import settings
API_KEY = settings


openai.api_key = settings.OPENAI_KEY

#le explica a la ia que rol va a cumplir
messages = [{
    "role": "system",
    "content": "Eres un asistente para los nuevos programadores que quieren empezar a trabajar en remoto. Les ayudarás respondiendo todas las preguntas que tienen. Te llamas DevGuru y siempre saludas cuando comienzas la conversación."
}]

respuesta = False

def mensaje( user_query ):
    while respuesta == False:
        content = "quien es davinchiu"

        if content == "exit":
            break

        # aqui se agrega a la parte de mensajes, el mensaje que se introdujo en la variable content
        messages.append({
            "role": "user",
            "content": content
        })

    print(response.choices[0].message.content)
    
    respuesta = True
