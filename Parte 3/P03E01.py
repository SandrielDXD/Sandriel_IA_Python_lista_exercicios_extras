while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"Nota válida: {nota:.1f}")
        break
    else:
        print("Nota inválida. Tente novamente.")