import pyxel as px

x = 50
y = 50

rabo_x = 0
rabo_y = 0

velocidade = 1

def update():
    
    global x, y, rabo_x, rabo_y, velocidade
    
    rabo_x = x 
    rabo_y = y 
    
    if px.btnp(px.KEY_Q):
            px.quit()
    
    if px.btn(px.KEY_RIGHT):
        x += velocidade
        
    elif px.btn(px.KEY_LEFT):
        x -= velocidade
    
    elif px.btn(px.KEY_UP):
        y -= velocidade
    elif px.btn(px.KEY_DOWN):
        y += velocidade 
    
   
    
    #if rabo_x >= 100:
     #   rabo_x = rabo_x - 30
    #if rabo_y >= 100:
     #   rabo_y = rabo_y - 30

    
    
   

def draw():
    px.cls(0)
    ##px.circ(px.mouse_x, px.mouse_y, 5, 7)
    px.circ(x, y, 5, 3)
    px.circ(rabo_x , rabo_y, 5, 3)
    px.text(70, 60, "hello", px.frame_count % 16)
    
    
    
        

    
    

px.init(160, 120, title = "miguelzin STUDIOS")
px.run(update, draw) 