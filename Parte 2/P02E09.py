produto1 = float(input("Digite o preço do primeiro produto: R$ "))
produto2 = float(input("Digite o preço do segundo produto: R$ "))
produto3 = float(input("Digite o preço do terceiro produto: R$ "))

menor_preco = min(produto1, produto2, produto3)

if menor_preco == produto1:
    recomendacao = "primeiro produto"
elif menor_preco == produto2:
    recomendacao = "segundo produto"
else:
    recomendacao = "terceiro produto"

print(f"\nRecomendação de compra: Você deve comprar o {recomendacao}, que custa R${menor_preco:.2f}")