#Sequência Recursiva: 
def fibonacciR(n):
    if n <= 1:
        return n
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

numero = int(input("Digite um número: "))
n = numero + 1
for i in range(0, n):
    print(fibonacciR(i))
