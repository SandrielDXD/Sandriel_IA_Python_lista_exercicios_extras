fib = [0, 1]

while fib[-1] <= 500:
    proximo = fib[-1] + fib[-2]
    fib.append(proximo)

# Como o último valor ultrapassou 500, vamos tirar ele pra ficar certinho
fib.pop()

print("Sequência de Fibonacci até passar de 500:")
print(fib)
