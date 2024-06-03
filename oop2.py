class Soma:
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def conta(self):
         return self.numero1 + self.numero2


valor1 = int(input("entre valor: "))
valor2 = int(input("entre valor: "))

soma_estancia = Soma(valor1, valor2)

resultado = soma_estancia.conta()

print("resultado = ", resultado)
