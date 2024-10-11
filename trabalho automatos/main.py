
estados = []
alfabeto = []
transicaoes = {}
estado_inicial = None
estado_final = None
estados_finais = []

{'q0' :{}}

while True:
    estado = input('informe um caracter: ')
    
    if (estado == ' '):
        break

    estados.append(estado)

print(estado)

while True:
    caracter = input('informe um caracter: ')
    
    if (caracter == ' '):
        break

    alfabeto.append(caracter)

for estado in estados:
    transicoes_local = {}
    for caracter in alfabeto:
        transicao = input(f' informe transicoes{estado, caracter} = ')
        transicoes_local[caracter] = transicao
    transicaoes[estado] = transicoes_local

estado_inicial = input('informe o estado inicial: ')

while True:
    if(estado_final):
        break

    estados_finais.append(estado_final)

while True:
    estado_atual = estado_inicial
    palavra = input('informe a palavra: ')

    for caracter in palavra:
        proximo_extado = transicaoes[estado_atual][caracter]
        estado_atual = proximo_extado
    
    if (estado_atual in estados_finais):
        print('palavra aceitavel')
    else:
        print('essa porra n')


print(estados)
print(alfabeto)
print(transicaoes)


