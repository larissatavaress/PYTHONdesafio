import random

def lancar_dado():

    return random.randint(1, 6)

def calcular_soma_dos_dados():

    dado1 = lancar_dado()
    dado2 = lancar_dado()
    return dado1 + dado2

if __name__ == "__main__":

    soma = calcular_soma_dos_dados()

    print(f"O resultado do lançamento dos dados foi: {soma}")