class node:
    def __init__ (self,info):
        self.info = info
        self.prox = None 

class listaEnc:
    def __init__(self):
        self.incio = None
        self.tam = 0

    def insere(self, posicao, valor):
        if(posicao > 0 and posicao <= self.tam + 1):
            novo = node(valor)
            self.tam += 1
            if(posicao == 1):
                novo.prox = self.incio
                self.inicio = novo
            else:
                aux = self.inicio
                count = 1 
                while (aux.prox != None and count < posicao - 1):
                    aux = aux.prox
                    count += 1
                if (aux != None):
                    novo.prox = aux.prox
                    aux.prox = novo
    
    
    insere(0,1)
    
    
