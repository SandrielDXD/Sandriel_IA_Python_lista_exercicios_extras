num = int(input("Digite um número inteiro para verificar se é primo: "))

if num < 2:
    print(f"{num} não é primo.")
else:
    divisores = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisores.append(i)

    if not divisores:
        print(f"{num} é primo.")
    else:
        print(f"{num} não é primo. É divisível por: {divisores}")
