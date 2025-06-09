area = float(input("área em metros quadrados que deve ser pintada: "))
litros = area / 3
latas = litros / 18
preço = latas * 80
if latas % 1 != 0:
    latas = int(latas) + 1  # Arredonda para cima se não for inteiro
print(f"Você precisará de {latas:.2f} latas de tinta.")
print(f"Você precisará gastar R$ {preço:.2f} com tinta.")