def mediac(lista):
    if not lista:
        return 0.0

    soma = sum(lista) 
    media = soma / len(lista) 
    return media

numeros = [1, 2, 3, 4, 5]
media_resultado = mediac(numeros)
print(f"A média dos números é: {media_resultado}")