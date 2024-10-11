class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox =None

class pilha_c:
    def __init__ (self, max):
        self.max = max
        self.top = None
        self.vetor = [None]*max

class pilha_e:
    def __init__ (self):
        self.topo = None
    
    def push(self,valor):
        if (self.top == None):
            aux = Nodo

        else:
