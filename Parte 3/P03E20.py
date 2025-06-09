while True:
    num = int(input("Digite um inteiro positivo menor que 16 para calcular o fatorial (ou -1 para sair): "))
    if num == -1:
        print("Saindo...")
        break
    if num < 0 or num >= 16:
        print("Número inválido! Deve ser positivo e menor que 16.")
        continue

    fatorial = 1
    for i in range(2, num + 1):
        fatorial *= i
    print(f"Fatorial de {num} é {fatorial}.")
