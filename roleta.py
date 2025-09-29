import random, questionary, time

itens_roleta = [0]

def pergunta():
    global escolha
    pergunta = questionary.select(
        "O que deseja fazer?",
        choices=["Rolar a roleta", "Adicionar um item", "Remover um item", "Sair"]
    ).ask()  

    if pergunta == "Rolar a roleta":
        escolha = 1

    elif pergunta == "Adicionar um item":
        escolha = 2

    elif pergunta == "Remover um item":
        escolha = 3

    elif pergunta == "Sair":
        exit()
        
def consequencias():
    global escolha
    if escolha == 2:
        adicionar = input("Novo item -> ")
        itens_roleta.append(adicionar)
        print("Itens da roleta:")
        print(itens_roleta[1:])

    elif escolha == 3:
        print(itens_roleta[1:])
        escolha = int(input("Escreva o numero do item que deseja remover"))
        del(itens_roleta[escolha])
        print("Itens da roleta:")
        print(itens_roleta[1:])

    elif escolha == 1:
        print("GIRANDO A ROLETA...")
        time.sleep(1.7)
        resultado_roleta = random.choice(itens_roleta[1:])
        print(resultado_roleta)

while True:
    pergunta()
    consequencias()
