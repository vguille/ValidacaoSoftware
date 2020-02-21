def fibonacci(n):
    if n <= 1:        
        return n   
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        

try:
    nterms = int(input("Digite o valor para a sequencia: "))

    if type(nterms) == int:
        if nterms <= 0:
            print("Por favor digite um valor positivo")
        else:
            fib = fibonacci(nterms)
            print("Valor da sequencia:", fib)            
except ValueError:
    print("Informe apenas numeros inteiros")