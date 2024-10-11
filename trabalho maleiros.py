import pyxel

# Definindo os estados do Wireworld
VAZIO = 0
CONDUTOR = 1
CAB_ELETRON = 2
CAU_ELETRON = 3

# Dimensões da grade
LARGURA_GRADE = 40
ALTURA_GRADE = 30
TAMANHO_CELULA = 10

class Wireworld:
    def __init__(self):
        pyxel.init(LARGURA_GRADE * TAMANHO_CELULA, ALTURA_GRADE * TAMANHO_CELULA + 20)
        
        pyxel.title("Wireworld")

        # Inicializa a grade com todas as células vazias
        self.grade = [[VAZIO for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]
        
        # Inicializa um exemplo de circuito simples
        self.grade[10][15] = CONDUTOR
        self.grade[10][16] = CONDUTOR
        self.grade[10][17] = CAB_ELETRON
        self.grade[10][18] = CAU_ELETRON

        # Controle de estado
        self.em_execucao = False  # Indica se a simulação está em execução ou pausa
        
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        # Verifica se o botão de sair (tecla Q) foi pressionado
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Verifica se o botão de espaço (play/pause) foi pressionado
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.em_execucao = not self.em_execucao

        # Se a simulação está em execução, atualiza a grade
        if self.em_execucao:
            self.atualizar_grade()

    def atualizar_grade(self):
        nova_grade = [[VAZIO for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]

        for y in range(ALTURA_GRADE):
            for x in range(LARGURA_GRADE):
                estado_atual = self.grade[y][x]
                if estado_atual == VAZIO:
                    nova_grade[y][x] = VAZIO
                elif estado_atual == CAB_ELETRON:
                    nova_grade[y][x] = CAU_ELETRON
                elif estado_atual == CAU_ELETRON:
                    nova_grade[y][x] = CONDUTOR
                elif estado_atual == CONDUTOR:
                    vizinhos_com_cabeca = self.contar_vizinhos_com_cabeca(x, y)
                    if vizinhos_com_cabeca == 1 or vizinhos_com_cabeca == 2:
                        nova_grade[y][x] = CAB_ELETRON
                    else:
                        nova_grade[y][x] = CONDUTOR

        self.grade = nova_grade

    def desenhar(self):
        pyxel.cls(0)  # Limpa a tela
        for y in range(ALTURA_GRADE):
            for x in range(LARGURA_GRADE):
                cor = self.obter_cor(self.grade[y][x])
                pyxel.rect(x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA, cor)

        # Desenha o botão de play/pause
        if self.em_execucao:
            pyxel.text(5, ALTURA_GRADE * TAMANHO_CELULA + 5, "PAUSAR [ESPACO]", 7)
        else:
            pyxel.text(5, ALTURA_GRADE * TAMANHO_CELULA + 5, "EXECUTAR [ESPACO]", 7)

    def obter_cor(self, estado_celula):
        if estado_celula == VAZIO:
            return 0  # preto
        elif estado_celula == CONDUTOR:
            return 9  # azul
        elif estado_celula == CAB_ELETRON:
            return 11  # amarelo
        elif estado_celula == CAU_ELETRON:
            return 8  # vermelho

    def contar_vizinhos_com_cabeca(self, x, y):
        # Conta quantos vizinhos são CAB_ELETRON
        vizinhos = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        contagem = 0
        for dx, dy in vizinhos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < LARGURA_GRADE and 0 <= ny < ALTURA_GRADE:
                if self.grade[ny][nx] == CAB_ELETRON:
                    contagem += 1
        return contagem

# Inicializa o Wireworld
Wireworld()
