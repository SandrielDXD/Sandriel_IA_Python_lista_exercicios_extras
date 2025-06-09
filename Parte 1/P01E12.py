genero = input("Digite seu gênero (M para masculino, F para feminino): ").strip().upper()
altura = float(input("altura de uma pessoa (em metros): "))
if genero == 'M':
    IMC = (72.7 * altura) - 58
elif genero == 'F':
    IMC = (62.1 * altura) - 44.7
else:
    print("Gênero inválido. Por favor, insira 'M' ou 'F'.")
    IMC = None
print(f"O peso ideal da pessoa é {IMC:.2f}.")

