def num_pares(lista):

    num_pares = [numero for numero in lista if numero % 2 == 0]
    return num_pares

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = num_pares(lista_de_numeros)
print(resultado)
