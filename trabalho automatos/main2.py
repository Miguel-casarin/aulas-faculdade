estados = []
alfabeto = []
transicoes = {}
estado_inicial = None
estados_finais = []

# Entrada dos estados
print("Digite os estados. Pressione espaço e depois Enter para finalizar.")
while True:
    estado = input('Informe um estado: ')
    
    if estado == ' ':
        break

    estados.append(estado)

print("Estados:", estados)

# Entrada do alfabeto
print("Digite os caracteres do alfabeto. Pressione espaço e depois Enter para finalizar.")
while True:
    caracter = input('Informe um caracter do alfabeto: ')
    
    if caracter == ' ':
        break

    alfabeto.append(caracter)

print("Alfabeto:", alfabeto)

# Entrada das transições
print("Digite as transições para cada estado e caracter.")
for estado in estados:
    transicoes_local = {}
    for caracter in alfabeto:
        transicao = input(f'Informe a transição para (estado: {estado}, caracter: {caracter}): ')
        transicoes_local[caracter] = transicao
    transicoes[estado] = transicoes_local

print("Transições:", transicoes)

# Definição do estado inicial
estado_inicial = input('Informe o estado inicial: ')
print("Estado inicial:", estado_inicial)

# Definição dos estados finais
print("Informe os estados finais. Pressione espaço e depois Enter para finalizar.")
while True:
    estado_final = input('Informe um estado final: ')
    
    if estado_final == ' ':
        break

    estados_finais.append(estado_final)

print("Estados finais:", estados_finais)

# Verificação de palavras
print("Digite palavras para verificar. Pressione espaço e depois Enter para finalizar.")
while True:
    estado_atual = estado_inicial
    palavra = input('Informe a palavra: ')

    if palavra == ' ':
        break

    for caracter in palavra:
        if caracter in alfabeto:
            proximo_estado = transicoes[estado_atual].get(caracter)
            estado_atual = proximo_estado
        else:
            print(f"Caracter '{caracter}' não pertence ao alfabeto.")
            break
    else:
        if estado_atual in estados_finais:
            print('Palavra aceitável')
        else:
            print('Palavra não aceitável')

print("Estados:", estados)
print("Alfabeto:", alfabeto)
print("Transições:", transicoes)
print("Estado inicial:", estado_inicial)
print("Estados finais:", estados_finais)
