nome = input("Digite o seu nome: ")

print("\nSeu nome em escada invertida:")
for i in range(len(nome), 0, -1):
    print(nome[:i].upper())