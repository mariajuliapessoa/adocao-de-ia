import random

produtos = {
    "blusa": ["blusa vermelha", "blusa azul", "blusa preta"],
    "saia": ["saia longa floral", "saia curta jeans", "saia lápis preta"],
    "vestido": ["vestido estampado", "vestido longo vermelho", "vestido preto básico"]
}

respostas = {
    "horário": "Nosso horário de atendimento é de segunda a sábado, das 9h às 19h.",
    "entrega": "O prazo de entrega é de 3 a 7 dias úteis, dependendo da sua região.",
    "troca": "Você pode trocar produtos em até 30 dias com nota fiscal.",
    "default": "Desculpe, não entendi. Você pode perguntar sobre produtos, entrega, troca ou horário."
}

print(" Chatbot da Loja de Roupas ativado! Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ").lower()
    
    if pergunta == "sair":
        print("Chatbot: Obrigado! Até logo! 👋")
        break
    
    encontrado = False
    for categoria in produtos:
        if categoria in pergunta:
            sugestao = random.choice(produtos[categoria])
            print(f"Chatbot: Temos {sugestao}. Gostaria de ver mais opções?")
            encontrado = True
            break
    
    if not encontrado:
        resposta = respostas["default"]
        for chave in respostas:
            if chave in pergunta:
                resposta = respostas[chave]
                break
        print(f"Chatbot: {resposta}")
