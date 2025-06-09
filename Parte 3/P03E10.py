num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Garante que o menor vem antes
inicio = min(num1, num2) + 1
fim = max(num1, num2)

print("\nNúmeros no intervalo entre os dois:")
for i in range(inicio, fim):
    print(i, end=' ')
