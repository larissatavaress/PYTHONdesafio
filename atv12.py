def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 0:
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        mediana = (meio1 + meio2) / 2
    else:
        mediana = lista_ordenada[tamanho // 2]

    return mediana

numeros = [7, 2, 5, 1, 9, 3]
mediana_resultado = calcular_mediana(numeros)
print(f"A mediana dos valores na lista é: {mediana_resultado}")