import openai

API_KEY = "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"


openai.api_key = API_KEY

#Contexto del asistente
messages = [{"role":"system",
             "content":"Eres un asistente para los nuevos programadores que quieren empezar a trabajar en remoto. Les ayudaras respondiendo todas las preguntas que tienen. Te llamas DevGuru y siempre saludas cuando comienzas la conversacion."}
            ]

respuesta = False
while respuesta == False:
    content = "dime que necesito para empezar a programar en remoto"

    if content == "exit":
        break

    messages.append({"role":"user", "content":content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    
    response_content = response.choices[0].message.content
    
    messages.append({"role":"assistant", "content":response})

    print(response.choices[0].message.content)
    
    input()
    respuesta = True