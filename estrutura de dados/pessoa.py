class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade

        # atributo privado, so ao alcance da classe
        self.__cpf = cpf
    
    # esse metodo usa, então posso chamar ele fora da classe para ver o cpf
    def print_cpf(self):
        print(self.__cpf)

ronaldo = Pessoa('ronaldo', 23, "044.998.700-03")
ronaldo.print_cpf()


    