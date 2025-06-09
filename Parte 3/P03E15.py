n = int(input("digite um número inteiro positivo: "))
fib = [1, 1]

if n == 1:
    print("Sequência de Fibonacci:", fib[:1])
elif n == 2:
    print("Sequência de Fibonacci:", fib)
else:
    for i in range(2, n):
        proximo = fib[i-1] + fib[i-2]
        fib.append(proximo)
    print("Sequência de Fibonacci:", fib)