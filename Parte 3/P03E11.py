num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = 0

# Garante que o menor vem antes
inicio = min(num1, num2) + 1
fim = max(num1, num2)

print("\nNúmeros no intervalo entre os dois:")
for i in range(inicio, fim):
    print(i, end=' ')


soma += i
print(f"\n\nA soma dos números no intervalo é: {soma}")