## TEMA!, FAZER UM DECK, INSERE NO INICIO E FIM 

class Filacont:
    def __init__(self, max):
        self.vetor = max * [None]
        self.ini = None
        self.fim = None
        self.tam = 0
        self.max = max

    def consultar(self):
        if (self.tam > 0):
            return self.vetor[self.ini]
    
    def insere(self, valor):
        if(self.max > self.tam):
            if (self.tam == 0):
                self.ini = 0
                self.fim =0 

            elif (self.fim == self.max - 1):
                self.fim = 0
            else:
                self.fim +=1
        
        self.vetor[self.fim] = valor
        self.tam += 1 

def remover(self):
    if self.tam > 0:
        if self.tam == 1:
            self.ini = None
            self.fim = None
        elif self.ini == self.max-1:
            self.ini = 0
        else:
            self.ini += 1

        self.tam -= 1