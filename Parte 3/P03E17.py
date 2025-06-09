num = int(input("Digite um número inteiro para calcular o fatorial: "))

if num < 0:
    print("Fatorial não existe para números negativos.")
elif num == 0 or num == 1:
    print(f"O fatorial de {num} é 1.")
else:
    fatorial = 1
    for i in range(2, num + 1):
        fatorial *= i
    print(f"O fatorial de {num} é {fatorial}.")
