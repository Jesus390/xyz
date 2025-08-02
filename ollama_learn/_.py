from ollama import Client, generate

# Inicializa el cliente Ollama
client = Client()  # Reemplaza con el nombre de tu modelo


while True:
    print(">> ", end="")
    prompt = input()
    if prompt == "salir": break
    respuesta = generate(
        model='gemma3:4b',
        prompt=prompt,
        stream=False  # True si querés recibir fragmentos
    )

    print(respuesta['response'])


# while True:
#     # Define el prompt
#     print(">> ", end='')
#     prompt = input()

#     if prompt == "salir": break

#     # Genera la respuesta
#     response = client.generate(
#         prompt,
#         max_tokens=200,
#         temperature=0.7,
#         top_p=0.9
#     )

#     # Imprime la respuesta
#     print(response)
