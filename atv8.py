def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None

    menor_palavra = lista_palavras[0]
    maior_palavra = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) < len(menor_palavra):
            menor_palavra = palavra
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    return menor_palavra, maior_palavra

if __name__ == "__main__":

    lista_palavras = input("Digite as palavras separadas por espaço: ").split()

    menor, maior = encontrar_maior_menor_palavra(lista_palavras)

    if menor and maior:
        print(f"A menor palavra é: {menor}")
        print(f"A maior palavra é: {maior}")
    else:
        print("A lista de palavras está vazia.")