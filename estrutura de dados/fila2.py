class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

class FilaEnc:
    def __init__(self):
        self.tam = 0
        self.ini = None
        self.fim = None

    def consultar(self):
        if(self.tam > 0): ## ou self.ini diferente de None
            return self.ini.info
        else:
            return None

    def inserir(self, valor):
        elem = Nodo(valor)

        if (self.tam == 0):
            self.ini = elem
        else:
            self.fim.prox = elem
            
        self.fim = elem
        self.tam += 1
    
    def remover(self):
        if (self.tam > 0):
            self.ini = self.ini.prox
            if ( self.tam == 1):
                self.fim = None
        
            self.tam -=1
            return set
    
        else:
            return None
    

F = FilaEnc() ## estancia class 

num_insere = int(input("quer inserir quantos valores: "))

for i in range(num_insere):
    elemento = int(input("elemento: "))
    F.inserir(elemento)


for i in range(F.tam):
    F.remover()

    print(F.consultar())

