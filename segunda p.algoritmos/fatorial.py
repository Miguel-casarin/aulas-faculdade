numero = int(input("entre com um valor: "))

def fatorial_iter(n):
    resultado = 1
    while n > 0:
        resultado = resultado * n
        n = n -1
    
    return resultado

fatorial = fatorial_iter(numero)
print("{}\n".format(fatorial))

#fatorial usando recursividade
def fatorial_rec(n):
    if n == 0:
        return IndexError("number not suported")
    else:
        # segue o caso de recursividade a função chama a si mesma
        return n * fatorial_rec(n - 1) 

fatorial_recursivo = fatorial_rec(numero)
print("{}\n".format(fatorial_recursivo))



