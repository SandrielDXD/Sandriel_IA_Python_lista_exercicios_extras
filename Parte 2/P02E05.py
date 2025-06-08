letra = input("Digite uma letra: ").lower()

if len(letra) != 1 or not letra.isalpha():
    print("Por favor, digite apenas uma letra válida!")
else:
    if letra in "aeiou":
        print(f"'{letra}' é uma vogal")
    else:
        print(f"'{letra}' é uma consoante")
