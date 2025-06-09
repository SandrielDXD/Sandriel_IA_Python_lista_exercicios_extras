def validar_nome():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) >= 3:
            return nome
        print("Nome deve ter pelo menos 3 caracteres.\n")

def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if 0 <= idade <= 150:
                return idade
            print("Idade deve estar entre 0 e 150.\n")
        except ValueError:
            print("Digite um número válido para a idade.\n")

def validar_salario():
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario >= 0:
                return salario
            print("Salário não pode ser negativo.\n")
        except ValueError:
            print("Digite um valor numérico válido para o salário.\n")

def validar_sexo():
    while True:
        sexo = input("Digite seu sexo (M/F): ").strip().upper()
        if sexo in ['M', 'F']:
            return sexo
        print("Sexo deve ser 'M' ou 'F'.\n")

def validar_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil (S/C/V/D): ").strip().upper()
        if estado_civil in ['S', 'C', 'V', 'D']:
            return estado_civil
        print("Estado civil deve ser 'S', 'C', 'V' ou 'D'.\n")

# Agora a mágica
nome = validar_nome()
idade = validar_idade()
salario = validar_salario()
sexo = validar_sexo()
estado_civil = validar_estado_civil()

print(f"\nCadastro realizado com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
