A = float(input("Digite a população inicial do país A: "))
B = float(input("Digite a população inicial do país B: "))
taxa_a = float(input("Digite a taxa de crescimento anual do país A (em %): ")) / 100
taxa_b = float(input("Digite a taxa de crescimento anual do país B (em %): ")) / 100
anos = 0

while A <= B:
    A += A * taxa_a
    B += B * taxa_b
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a de B.")
print(f"População final A: {int(A)}")
print(f"População final B: {int(B)}")
