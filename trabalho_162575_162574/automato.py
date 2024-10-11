import pyxel as px
import numpy as np

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

def play_press():
    global paused
    paused = False

def pause_press():
    global paused
    paused = True

def step_press():
    global paused, step_once
    paused = True
    step_once = True

def reset_press():
    global curr, next, step_count
    step_count = 0
    load_from_file('estado_inicial.txt')

def increase_speed():
    global speed_factor
    if speed_factor > 1:
        speed_factor -= 1

def decrease_speed():
    global speed_factor
    speed_factor += 1

def init_wireworld():
    global curr, next
    curr = np.zeros(shape=(px.width, px.height), dtype=int)
    next = np.zeros_like(curr)

def load_from_file(filename):
    global curr
    with open(filename, 'r') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                curr[x, y] = int(char)

def get(x, y):
    return curr[x % px.width, y % px.height]

def update_cells():
    global curr, next, step_count
    for x in range(px.width):
        for y in range(px.height):
            cell = get(x, y)
            if cell == 1:
                next[x, y] = 2
            elif cell == 2:
                next[x, y] = 3
            elif cell == 3:
                neighbors = sum(get(x+dx, y+dy) == 1 for dx in [-1, 0, 1] for dy in [-1, 0, 1] if (dx, dy) != (0, 0))
                next[x, y] = 1 if neighbors == 1 or neighbors == 2 else 3
            else:
                next[x, y] = 0
    curr, next = next, curr
    step_count += 1

def draw():
    px.cls(0)
    colors = {0: 0, 1: 9, 2: 10, 3: 7}
    for x in range(px.width - 100):
        for y in range(px.height):
            px.pset(x + 100, y, colors[get(x, y)])
    b_play.draw()
    b_pause.draw()
    b_step.draw()
    b_reset.draw()
    b_speed_up.draw()
    b_speed_down.draw()
    px.text(5, px.height - 10, f"Steps: {step_count}", 7)

def edit_with_mouse():
    if px.btn(px.MOUSE_BUTTON_LEFT):
        x, y = px.mouse_x - 100, px.mouse_y
        if 0 <= x < px.width and 0 <= y < px.height:
            curr[x, y] = 3

def update_speed():
    global speed_counter
    speed_counter += 1
    if speed_counter % speed_factor == 0:
        update_cells()

px.init(150, 150, display_scale=3, fps=20)
px.mouse(True)

paused = True
step_once = False
step_count = 0
speed_counter = 0
speed_factor = 10

init_wireworld()
load_from_file('estado_inicial.txt')

b_play = Button(5, 5, 'Play', play_press)
b_pause = Button(5, 14, 'Pause', pause_press)
b_step = Button(5, 23, 'Step', step_press)
b_reset = Button(5, 32, 'Reset', reset_press)
b_speed_up = Button(5, 41, 'Speed+', increase_speed)
b_speed_down = Button(5, 50, 'Speed-', decrease_speed)

def update():
    global step_once
    if not paused or step_once:
        update_speed()
        step_once = False
    edit_with_mouse()

px.run(update, draw)
