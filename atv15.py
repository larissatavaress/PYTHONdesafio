def ordenar_lista_crescente(lista):

    lista.sort()
    return lista


numeros = [10, 5, 20, 15, 8, 99,123]
numeros_ordenados = ordenar_lista_crescente(numeros)
print("Lista ordenada:", numeros_ordenados)