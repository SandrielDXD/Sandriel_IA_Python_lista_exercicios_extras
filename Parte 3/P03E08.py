soma = 0

for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    soma += num
print(f"\nA soma dos números digitados é: {soma}")

media= soma / 5
print(f"A média dos números digitados é: {media:.2f}")
