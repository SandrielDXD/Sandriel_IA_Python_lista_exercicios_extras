peso = float(input("Digite o peso dos peixes (em kg): "))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print(f"Peso excedido: {excesso:.2f} kg")
    print(f"Multa a ser paga: R$ {multa:.2f}")