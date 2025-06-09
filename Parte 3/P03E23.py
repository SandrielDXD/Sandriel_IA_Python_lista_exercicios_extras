N = int(input("Digite um número inteiro N para listar primos até N: "))

cont_divisoes = 0

for num in range(2, N + 1):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        cont_divisoes += 1
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=" ")

print(f"\nNúmero total de divisões executadas: {cont_divisoes}")
