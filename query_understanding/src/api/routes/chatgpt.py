import openai

API_KEY = ""

openai.api_key = API_KEY

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

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        response_content = response.choices[0].message.content

        # aqui se agrega la respuesta a la lista de mensajes para mantener el contexto de la conversacion
        messages.append({
            "role": "assistant",
            "content": response
        })

        print(response.choices[0].message.content)
        input()
        respuesta = True
