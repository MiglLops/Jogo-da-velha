import random 

acerto = False
numero = random.randint(0, 99)
print(numero)
tentativas = 0

while acerto != True:

    numero_jogador = int(input("Escreva um numero de 0 a 100:"))

    if numero_jogador < numero:
        print("O numero é maior") 
        tentativas += 1
    elif numero_jogador > numero:
        print("O numero é menor")
        tentativas += 1
    else:
        print("ACERTOU!")
        print(f"Voce fez {tentativas} tentativas!")
        acerto = True