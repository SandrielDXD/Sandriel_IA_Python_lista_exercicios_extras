maior = 0

for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    if maior is 0 or num > maior:
        maior = num

print(f"\nO maior número digitado foi: {maior}")
