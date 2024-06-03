class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.idade = 20

    def exibir(self):
        print(self.nome, self.idade)

#estamciando a classe
guilherme = Cliente("guilherme", "email@email.com")

guilherme.exibir()