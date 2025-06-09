num = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))

if 1 <= num <= 10:
    print(f"\nTabuada de {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Número inválido! Digite um número entre 1 e 10.")
