class Codigo:

    def __init__(self, nome, idade, numero):
        self.nome = nome
        self.idade = idade
        self.numero = numero

    def exibir(self):
        print(
            f"Meu nome é {self.nome} tenho {self.idade} anos sou travesti e hj já dei o cu {self.numero}"
        )

nome = str(input("seu nome.........: "))
idade = int(input("sua idade.......: "))
numero = int(input("numero qualquer: "))

estancia_codigo = Codigo(nome, idade, numero)

estancia_codigo.exibir()