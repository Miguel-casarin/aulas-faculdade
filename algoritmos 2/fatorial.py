def fat(num):
    if num ==0:
        return 1
    else:
        return num * fat(num-1)

numero = int(input('entre com seu numero: '))
fatorial = fat(numero)
print(fatorial)