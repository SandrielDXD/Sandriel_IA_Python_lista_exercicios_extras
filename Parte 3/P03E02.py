while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    if nome == senha:
        print("Erro: O nome não pode ser igual à senha.")
    else:
        print(f"Cadastro realizado com sucesso! Nome: {nome}, Senha: {senha}")
        break