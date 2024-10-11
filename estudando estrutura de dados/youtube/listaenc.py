from node import Node

class Linkedlist:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        if self.head:
            #inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node()
        self._size = self._size + 1

    def __len__(self):
        return self._size

    def _getnode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __set__(self, index, elen):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")

    def __getitem__(self, index):
        pointer = self._getnode(index)
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")   
    
    def __setitem__(self, index, elem):
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
             raise IndexError("list index out of range")
    

    def index(self, elen):
        pointer = self.head
        while(pointer):
            if pointer.data == elen:
                return i
            pointer = pointer.next
            i =i+1
        raise ValueError("{} is noto in list".format(elen))
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index -1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1



lista = Linkedlist()