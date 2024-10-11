class Lista:
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
            elif self.fim != self.max - 1:  # Deslocar para o fim
                for i in range(self.fim, self.ini + posicao - 1, -1):
                    self.vetor[i + 1] = self.vetor[i]
                self.fim += 1
            else:  # Deslocar para o início
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

    def insertion_sort(self):
        if self.Vazia():
            return

        for i in range(self.ini + 1, self.fim + 1):
            key = self.vetor[i]
            j = i - 1
            while j >= self.ini and key < self.vetor[j]:
                self.vetor[j + 1] = self.vetor[j]
                j -= 1
            self.vetor[j + 1] = key


# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):

	# Check base case
	if high >= low:

		mid = (high + low) // 2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")

listra = Listra(6)

listra.inserir(0, 14)
listra.inserir(1, 11)
listra.inserir(2, 13)
listra.inserir(3, 12)
listra.inserir(4, 10)
listra.inserir(5, 15)

print("Antes da ordenação:")
listra.imprimir()

listra.insertion_sort()

print("Após a ordenação:")
listra.imprimir()
