def soma():
    num1 = int(input("Digite o primeiro número (entre 1 e 100): "))
    num2 = int(input("Digite o segundo número (entre 1 e 100): "))

    if 1 <= num1 <= 100 and 1 <= num2 <= 100:
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")
    else:
        print("Por favor, digite números entre 1 e 100.")

soma()











