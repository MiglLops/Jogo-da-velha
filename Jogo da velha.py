#Jogo da velha - inicio 24/09/2025

lista_print = ["[0]", "[1]", "[2]", "[3]",
         "[4]", "[5]", "[6]",
         "[7]", "[8]", "[9]"]

jogando = True
while jogando == True:
    print(lista_print[1], lista_print[2], lista_print[3])
    print(lista_print[4], lista_print[5], lista_print[6])
    print(lista_print[7], lista_print[8], lista_print[9])

    escolha = int(input("Escolha a casa para jogar 'X':"))
    pop = lista_print.pop(escolha)
    X = lista_print.insert(escolha, "X")

    #pra ve se ganhou

    if lista_print[2] and lista_print[5] and lista_print[8] == "X":
        print("venceu")
    elif lista_print[1] and lista_print[5] and lista_print[9] == "X":
        print("venceu")
    elif lista_print[3] and lista_print[5] and lista_print[7] == "X":
        print("venceu")
    elif lista_print[1] and lista_print[4] and lista_print[7] == "X":
        print("venceu")
    elif lista_print[3] and lista_print[6] and lista_print[9] == "X":
        print("venceu")
