total_eleitores = int(input("Número total de eleitores: "))
votos = [0, 0, 0]  # índice 0,1,2 = candidatos 1,2,3

for i in range(total_eleitores):
    while True:
        voto = int(input(f"Eleitor {i+1}, digite seu voto (1, 2 ou 3): "))
        if voto in [1, 2, 3]:
            votos[voto-1] += 1
            break
        else:
            print("Voto inválido! Tente novamente.")

print(f"Votos do candidato 1: {votos[0]}")
print(f"Votos do candidato 2: {votos[1]}")
print(f"Votos do candidato 3: {votos[2]}")
