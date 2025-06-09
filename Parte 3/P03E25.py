n = int(input("Número de pessoas na turma: "))
soma_idades = 0

for _ in range(n):
    idade = int(input("Digite a idade: "))
    soma_idades += idade

media = soma_idades / n

if 0 <= media <= 25:
    print(f"Média: {media:.2f} — Turma jovem")
elif 26 <= media <= 60:
    print(f"Média: {media:.2f} — Turma adulta")
else:
    print(f"Média: {media:.2f} — Turma idosa")
