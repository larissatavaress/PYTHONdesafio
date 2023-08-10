def imprimir_numerosn(n):

    if n < 0:
        print("Por favor, informe um número inteiro positivo.")
        return

    for i in range(n + 1):
        print(i)

numero = int(input("Digite um número inteiro positivo: "))

print("Números naturais de 0 até", numero, "em ordem crescente:")
imprimir_numerosn(numero)