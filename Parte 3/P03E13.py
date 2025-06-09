base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente (inteiro positivo): "))

resultado = 1

for _ in range(abs(expoente)):
    resultado *= base

# Se o expoente for negativo, inverte o resultado (como fração)
if expoente < 0:
    resultado = 1 / resultado

print(f"\n{base} elevado a {expoente} é igual a {resultado}")
