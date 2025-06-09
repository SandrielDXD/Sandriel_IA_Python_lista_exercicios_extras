import math
while True:
    # Entrada
    area = float(input("Área em metros quadrados que deve ser pintada: "))

    # Adiciona 10% de folga
    area *= 1.1

    # Calcula litros necessários
    litros = area / 6

    # Cálculo usando apenas latas de 18L
    latas = math.ceil(litros / 18)
    preco_latas = latas * 80

    # Cálculo usando apenas galões de 3.6L
    galoes = math.ceil(litros / 3.6)
    preco_galoes = galoes * 25

    # Cálculo misto (economizar com menos desperdício)
    latas_misto = int(litros / 18)
    resto = litros - (latas_misto * 18)
    galoes_misto = math.ceil(resto / 3.6)
    preco_misto = (latas_misto * 80) + (galoes_misto * 25)

    # Saída
    print(f"\nVocê precisará de aproximadamente {litros:.2f} litros de tinta.\n")

    print(">> Situação 1 - Apenas latas de 18L:")
    print(f"  {latas} latas - Total: R$ {preco_latas:.2f}")

    print(">> Situação 2 - Apenas galões de 3.6L:")
    print(f"  {galoes} galões - Total: R$ {preco_galoes:.2f}")

    print(">> Situação 3 - Mistura (menos desperdício):")
    print(f"  {latas_misto} latas e {galoes_misto} galões - Total: R$ {preco_misto:.2f}")

    # Pergunta se deseja continuar
    continuar = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
    if continuar != 's':
        print("Encerrando o programa.")
        quit() # Encerra o programa se a entrada for 'n'
        