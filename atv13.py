def contar_ocorrencias_palavras(texto):

    contagem_palavras = {}

    palavras = texto.lower().split()

    for palavra in palavras:
        palavra = palavra.strip(",.!?():;\"'")


        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    return contagem_palavras

texto = input("Digite um texto: ")
ocorrencias_palavras = contar_ocorrencias_palavras(texto)

print("Ocorrências de cada palavra:")
for palavra, ocorrencias in ocorrencias_palavras.items():
    print(f"{palavra}: {ocorrencias}")