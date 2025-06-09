A = 80000
B = 200000
taxa_a = 0.03  # 3%
taxa_b = 0.015 # 1.5%
anos = 0

while A <= B:
    A += A * taxa_a
    B += B * taxa_b
    anos += 1

print(f"Levará {anos} anos para a população do país A ultrapassar ou igualar a de B.")
print(f"População final A: {int(A)}")
print(f"População final B: {int(B)}")
