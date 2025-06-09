N = int(input("Quantos números deseja informar? "))

menor = None
maior = None
soma = 0

for _ in range(N):
    num = float(input("Digite um número: "))
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num
    soma += num

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
