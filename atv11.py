import random

def jogo_adivinhacao():

    numero_secreto = random.randint(1, 100)

    tentativas = 0
    while True:

        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1


        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente novamente! O número é maior.")
        else:
            print("Tente novamente! O número é menor.")


jogo_adivinhacao()