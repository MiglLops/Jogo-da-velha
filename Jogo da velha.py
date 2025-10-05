#Jogo da velha - inicio 24/09/2025
def jogar():
    lista_print = ["[0]", "[1]", "[2]", "[3]",
            "[4]", "[5]", "[6]",
            "[7]", "[8]", "[9]"]

    def grades():
        print(lista_print[1], lista_print[2], lista_print[3])
        print(lista_print[4], lista_print[5], lista_print[6])
        print(lista_print[7], lista_print[8], lista_print[9])
        print()

    def turnos():
        escolha = int(input("Escolha a casa para jogar 'X':"))
        pop = lista_print.pop(escolha)
        X = lista_print.insert(escolha, "X") 
        grades()
        detectar_venceu()
        escolha = int(input("Escolha a casa para jogar 'O':"))
        pop = lista_print.pop(escolha)
        O = lista_print.insert(escolha, "O") 

    def detectar_venceu():
        combinacoes = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],  
            [1, 4, 7],  
            [2, 5, 8],  
            [3, 6, 9],  
            [1, 5, 9],  
            [3, 5, 7]   
        ]
        for a, b, c in combinacoes:
            if lista_print[a] == lista_print[b] == lista_print[c]:
                print("FIM - Jogador", lista_print[a], "venceu!")
                grades()
                novamente = input("Deseja jogar novamente? S/n: ")
                if novamente == "n":
                    exit()
                else:
                    jogar()

    jogando = True
    while jogando == True:
        grades()
        turnos()
        detectar_venceu()

jogar()


