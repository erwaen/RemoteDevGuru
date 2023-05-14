import openai

API_KEY = "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"


openai.api_key = API_KEY

#Contexto del asistente
messages = [{"role":"system",
             "content":"Eres un asistente para los nuevos programadores que quieren empezar a trabajar en remoto. Les ayudaras respondiendo todas las preguntas que tienen. Te llamas DevGuru y siempre saludas cuando comienzas la conversacion."}
            ]

content = "dime que necesito para empezar a programar en remoto"

messages.append({"role":"user", "content":content})

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=messages
)

print(response.choices[0].message.content)
