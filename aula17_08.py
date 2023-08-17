import pyxel as px

x = 50
y = 50

def update():
    global x, y
    x = x + 0.5
    y = y + 0.5
    if px.btnp(px.KEY_Q):
            px.quit()
    
    if x >= 160:
        x = 0
    if y >= 120:
        y = 0
    

def draw():
    ##px.cls(4)
    ##px.circ(px.mouse_x, px.mouse_y, 5, 7)
    px.circ(x, y, 5, px.frame_count % 16)
    
    px.text(70, 60, "hello", px.frame_count % 16)
    
        

    
    

px.init(160, 120, title = "miguelzin STUDIOS")
px.run(update, draw) 