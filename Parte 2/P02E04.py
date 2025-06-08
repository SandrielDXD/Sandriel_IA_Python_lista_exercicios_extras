sexo = input("Digite F para Feminino ou M para: ")

sexo = sexo.upper()

if sexo == "F":
    print("F - feminino")
elif sexo == "M":
    print("M - Masculino")
else:
    print("Sexo Inválido")