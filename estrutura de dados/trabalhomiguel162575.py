
fila = [25, 32, 7, 19, 10, 5, 8]
fila_ordenada = []
pilha_a = []
pilha_b= []

class Pilha:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


class FilaComDuasPilhas:
    def _init_(self):
        self.pilha1 = Pilha()
        self.pilha2 = Pilha()

    def enfileirar(self, item):
        self.pilha1.push(item)

    def desenfileirar(self):
        if self.pilha2.is_empty():
            while not self.pilha1.is_empty():
                self.pilha2.push(self.pilha1.pop())
        return self.pilha2.pop()

# Exemplo de uso:
fila = FilaComDuasPilhas()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print(fila.desenfileirar())  # Saída: 1
print(fila.desenfileirar())  # Saída: 2
print(fila.desenfileirar())  # Saída: 3
while len(fila)> 0:
    while len(pilha_a>0) and fila[i]> pilha_a.topo:
        pilha_b.append(pilha-a.topo)
        fila[i].pop
    while pilha_b > 0:
        pilha_a.append(pilha_b.topo)