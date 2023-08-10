def verifpalindromo(palavra):
    palavra = palavra.replace(" ", "").lower()

    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavra_exemplo = "Banana"
resultado = verifpalindromo(palavra_exemplo)

if resultado:
    print(f'A palavra "{palavra_exemplo}" é um palíndromo!')
else:
    print(f'A palavra "{palavra_exemplo}" não é um palíndromo.')