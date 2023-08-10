def palavras_maiusculas(lista_strings):

    palavras_maiusculas_lista = []

    for palavra in lista_strings:

        palavras_maiusculas_lista.append(palavra.upper())

    return palavras_maiusculas_lista

lista_strings = ["exemplo", "jeovanna", "programação", "python"]
resultado = palavras_maiusculas(lista_strings)
print("Palavras em letras maiúsculas:", resultado)