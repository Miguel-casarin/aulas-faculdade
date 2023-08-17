import pyxel as px 

x = 50
y = 50

def update():
    global x
    global y
    
    if px.btn(px.KEY_RIGHT):
        x += 1
    elif px.btn(px.KEY_LEFT):
        x -= 1
    
    elif px.btn(px.KEY_UP):
        y -= 1
    elif px.btn(px.KEY_DOWN):
        y += 1

def draw():
    px.cls(5)
    px.blt(x,y,0,0,0,16,16,13)

px.init(100, 100, title='miguelzin estudios')
px.image(0).load(0,0,'cat_16x16.png')
px.run(update, draw)