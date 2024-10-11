class ListaContigua:
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def Vazia(self):
        return self.ini == -1

    def inserir(self, posicao, dado):
        if self.fim - self.ini + 1 < self.max and 0 <= posicao <= self.fim - self.ini + 1:
            if self.Vazia():
                self.ini = 0
                self.fim = 0
            elif self.fim != self.max - 1:  
                for i in range(self.fim, self.ini + posicao - 1, -1):
                    self.vetor[i + 1] = self.vetor[i]
                self.fim += 1
            else: 
                for i in range(self.ini, self.ini + posicao):
                    self.vetor[i - 1] = self.vetor[i]
                self.ini -= 1

            self.vetor[self.ini + posicao] = dado
            return True
        else:
            return False

    def imprimir(self):
        if not self.Vazia():
            print(self.vetor[self.ini:self.fim + 1])
        else:
            print("Lista vazia")

    def ordenar(self):
        if not self.Vazia():
            for i in range(self.ini + 1, self.fim + 1):
                key = self.vetor[i]
                j = i - 1
                while j >= self.ini and key < self.vetor[j]:
                    self.vetor[j + 1] = self.vetor[j]
                    j -= 1
                self.vetor[j + 1] = key

    def busca_binaria(self, valor):
        if self.Vazia():
            raise ValueError("Lista vazia")
        return self._busca_binaria_recursiva(valor, self.ini, self.fim)

    def _busca_binaria_recursiva(self, valor, inicio, fim):
        if inicio > fim:
            raise ValueError("Valor não encontrado")
        meio = (inicio + fim) // 2
        if self.vetor[meio] == valor:
            return meio - self.ini
        elif self.vetor[meio] < valor:
            return self._busca_binaria_recursiva(valor, meio + 1, fim)
        else:
            return self._busca_binaria_recursiva(valor, inicio, meio - 1)


lista = ListaContigua(6)

lista.inserir(0, 5)
lista.inserir(1, 13)
lista.inserir(2, 7)
lista.inserir(3, 9)
lista.inserir(4, 11)
lista.inserir(5, 4)

lista.ordenar()

#vai mostrar a posição depois da ordenação 
pos = lista.busca_binaria(11)
print(f"Elemento encontrado na posição {pos}")



