N = int(input("Quantas notas você vai informar? "))

soma = 0
for _ in range(N):
    nota = float(input("Digite a nota: "))
    soma += nota

media = soma / N if N > 0 else 0

print(f"A média aritmética é: {media:.2f}")
