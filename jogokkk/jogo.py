import pyxel as px

x = 10
y = 50
pose = 0
velocidade = 1

def update():

    global x, velocidade

    if px.btn(px.KEY_RIGHT):
        x = x + velocidade
    if px.btn(px.KEY_LEFT):
        x = x - velocidade
    global y
    if px.btn(px.KEY_UP):
        y = y - velocidade
    if px.btn(px.KEY_DOWN):
        y = y + velocidade
    
    
   
    
   



def draw():
    global pose
    px.cls(0)
    if int(pose) == 0:
# blt x, y, img, u, v, w, h)
        px.blt(x, y,0,0,0,8,8)
    else:
        px.blt(x, y,0,8,0,8,8)
    pose = pose + 0.1
    if pose > 2:
        pose = 0

px.init(100, 100)
px.image(0).load(0,0,'noguchi_128x128.png')
px.run(update, draw)