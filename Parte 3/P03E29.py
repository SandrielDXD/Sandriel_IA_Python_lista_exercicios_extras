print("Lojas Quase Dois - Tabela de preços")
preco_unitario = 1.99

for i in range(1, 51):
    total = preco_unitario * i
    print(f"{i} - R$ {total:.2f}")

