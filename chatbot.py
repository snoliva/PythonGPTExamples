from openai import OpenAI

client = OpenAI(
    api_key = 'XXXXX'
)

preguntas_anteriores = []
respuestas_anteriores = []
#No almacena el contexto de la conversa
def preguntar_chat_gpt(pregunta, modelo="gpt-3.5-turbo", role="user"):
    respuesta = client.chat.completions.create(
        model=modelo,
        messages=[{"role":role, "content":pregunta}],
        max_tokens=150,
        n=1
    )
    return respuesta.choices[0].message.content

print("Bienvenido a nuestra chatbot. Escribe salir cuando quieras terminar")

while True:
    pregunta = input("\nTu: ")
    if pregunta.lower() == "salir":
        break
    prompt = f"El usuario pregunta: {pregunta}\nChat gpt responde"
    respuesta_gpt = preguntar_chat_gpt(prompt)
    print("ChatGPT:", respuesta_gpt)
