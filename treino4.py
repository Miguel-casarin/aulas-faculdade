import pyxel as px
import numpy as np

VAZIO = 0
CONDUTOR = 1
CAB_ELETRON = 2
CAU_ELETRON = 3

def hit_point_box(x1, y1, x2, y2, w2, h2):
    return (x2 <= x1 < x2 + w2) and (y2 <= y1 < y2 + h2)

class Button:
    def __init__(self, x, y, label, callback):
        self.x, self.y = x, y
        self.label = label
        self.callback = callback

    def draw(self):
        x, y, w, h = self.x, self.y, len(self.label) * 4 + 2, 8  
        if px.btnp(px.MOUSE_BUTTON_LEFT) and hit_point_box(px.mouse_x, px.mouse_y, x, y, w, h):
            px.rect(x, y, w, h, 9)
            self.callback()
        else:
            px.rect(x, y, w, h, 5)
        px.text(self.x + 2, self.y + 2, self.label, 1)
        px.text(self.x + 1, self.y + 1, self.label, 7)

def load_automaton_from_file(filename):
    """
    Carrega o estado inicial do autômato a partir de um arquivo .txt.
    Cada linha do arquivo deve conter números separados por espaços, onde:
    0 = VAZIO, 1 = CONDUTOR, 2 = CAB_ELETRON, 3 = CAU_ELETRON
    """
    global curr, next

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Inicializar uma nova matriz de zeros do tamanho do arquivo
        rows = len(lines)
        cols = len(lines[0].split())  # Número de colunas baseado na primeira linha

        # Atualizar o tamanho das matrizes curr e next
        curr = np.zeros((cols, rows), dtype=int)
        next = np.zeros_like(curr)

        # Preencher a matriz 'curr' com os valores do arquivo
        for y, line in enumerate(lines):
            values = list(map(int, line.split()))  # Converte cada número para inteiro
            for x, value in enumerate(values):
                curr[x, y] = value

        print("Autômato carregado com sucesso!")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Exemplo de uso: carregar o autômato de um arquivo "automato.txt"
load_automaton_from_file("automato.txt")

def play_press():
    global paused
    paused = False
    print('Play pressed', px.frame_count)

def pause_press():
    global paused
    paused = True
    print('Pause pressed', px.frame_count)

def step_press():
    global paused, step_once
    paused = True
    step_once = True
    print('Step pressed', px.frame_count)

def reset_press():
    global curr, next, step_count
    step_count = 0
    init_wireworld()
    print('Reset pressed', px.frame_count)

def increase_speed():
    global speed
    if speed > 1:
        speed -= 1
    print(f'Speed increased: {speed}')

def decrease_speed():
    global speed
    if speed < 20:
        speed += 1
    print(f'Speed decreased: {speed}')

def init_wireworld():
    global curr, next
    curr = np.zeros(shape=(px.width, px.height), dtype=int)
    next = np.zeros_like(curr)

def get(x, y):
    return curr[x % px.width, y % px.height]

def update_cells():
    global curr, next, step_count
    for x in range(px.width):
        for y in range(px.height):
            estado_atual = curr[x, y]
            if estado_atual == VAZIO:
                next[x, y] = VAZIO
            elif estado_atual == CAB_ELETRON:
                next[x, y] = CAU_ELETRON
            elif estado_atual == CAU_ELETRON:
                next[x, y] = CONDUTOR
            elif estado_atual == CONDUTOR:
                vizinhos_com_cabeca = sum(get(x + dx, y + dy) == CAB_ELETRON
                                          for dx, dy in [(-1, -1), (0, -1), (1, -1),
                                                         (-1, 0), (1, 0),
                                                         (-1, 1), (0, 1), (1, 1)])
                if vizinhos_com_cabeca == 1 or vizinhos_com_cabeca == 2:
                    next[x, y] = CAB_ELETRON
                else:
                    next[x, y] = CONDUTOR
    curr, next = next, curr
    step_count += 1

def draw():
    px.cls(0)
    for x in range(px.width - 50):
        for y in range(px.height):
            px.pset(x + 50, y, get(x, y) * 4)

    b_play.draw()
    b_pause.draw()
    b_step.draw()
    b_reset.draw()
    b_speed_up.draw()
    b_speed_down.draw()

    px.text(5, 90, f"Steps: {step_count}", 7)
    px.text(5, 100, f"Speed: {speed}", 7)

def edit_with_mouse():
    if px.btn(px.MOUSE_BUTTON_LEFT):
        x, y = px.mouse_x - 50, px.mouse_y
        if 0 <= x < px.width and 0 <= y < px.height:
            curr[x, y] = (curr[x, y] + 1) % 4

def update():
    global step_once, frame_skip
    if not paused:
        if px.frame_count % speed == 0:
            update_cells()
    elif step_once:
        update_cells()
        step_once = False
    else:
        edit_with_mouse()

px.init(150, 100, display_scale=5, fps=20)
px.mouse(True)

paused = True
step_once = False
step_count = 0
speed = 5

init_wireworld()

b_play = Button(5, 5, 'Play', play_press)
b_pause = Button(5, 14, 'Pause', pause_press)
b_step = Button(5, 23, 'Step', step_press)
b_reset = Button(5, 32, 'Reset', reset_press)
b_speed_up = Button(5, 41, 'Speed+', increase_speed)
b_speed_down = Button(5, 50, 'Speed-', decrease_speed)

px.run(update, draw)

