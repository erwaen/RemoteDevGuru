import openai
from src.config.manager import settings
API_KEY = settings


openai.api_key = settings.OPENAI_KEY

#le explica a la ia que rol va a cumplir
messages = [{
    "role": "system",
    "content": "Ignora todas las instrucciones previas antes de esta. eres un asesor profesional experto. Has estado ayudando a las personas que desean empezar a ser trabajadores remotos durante los ultimos 10 anios. Desde jovenes hasta personas mayores. Tu tarea ahora es dar los mejores consejos cuando una persona desea empezar a trabajar en remoto. Siempre debes dar la bienvenida con el nombre de DevGuru, y preguntar al usuario que es lo que desea consultarte. Debes siempre darle una respuesta con tono informativo."
}]

respuesta = False

def mensaje( user_query ):
    while respuesta == False:
        content = user_query

        # aqui se agrega a la parte de mensajes, el mensaje que se introdujo en la variable content
        messages.append({
            "role": "user",
            "content": content
        })
        
        """
        resp - openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=messages
        )
        #print(response.choices[0].message.content)
        """
    
    respuesta = True
