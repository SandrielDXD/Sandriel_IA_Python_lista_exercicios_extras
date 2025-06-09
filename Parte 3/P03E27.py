qtd_turmas = int(input("Quantidade de turmas: "))
total_alunos = 0

for i in range(qtd_turmas):
    while True:
        alunos = int(input(f"Alunos na turma {i+1} (máximo 40): "))
        if 0 <= alunos <= 40:
            total_alunos += alunos
            break
        else:
            print("Valor inválido, máximo 40 alunos por turma.")

media = total_alunos / qtd_turmas if qtd_turmas > 0 else 0
print(f"Número médio de alunos por turma: {media:.2f}")
