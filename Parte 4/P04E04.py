nome = input("Digite o seu nome: ")

print("\nSeu nome em escada:")
for i in range(1, len(nome) + 1):
    print(nome[:i].upper())