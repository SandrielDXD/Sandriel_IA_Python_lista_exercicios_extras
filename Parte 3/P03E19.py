N = int(input("Quantos números deseja informar? "))

menor = None
maior = None
soma = 0

for _ in range(N):
    while True:
        num = float(input("Digite um número entre 0 e 1000: "))
        if 0 <= num <= 1000:
            break
        else:
            print("Número inválido! Tente novamente.")

    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num
    soma += num

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")
