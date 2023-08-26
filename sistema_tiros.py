import pyxel as px

x = 50
y = 50
life = 20 
velocidade = 1

x_inimigo = 200
y_inimigo = 150

boost_multiplier = 5  # Fator de multiplicação para o boost
boost_active = False  # Indica se o boost está ativo

x_tiro = 5
y_tiro = 5

#função de tiro 
def bala(ataque_x, ataque_y):
    ataque_x = x + x_tiro
    ataque_y = y = y_tiro
    
    




def verifica_colisao(x1, y1, x2, y2, cor):
    if px.pget(x1, y1) == cor:
        return True
    elif px.pget(x2, y1) == cor:
        return True
    elif px.pget(x1, y2) == cor:
        return True
    elif px.pget(x2, y2) == cor:
        return True
    else:
        return False 
    

def update():

    global x, y, velocidade, boost_multiplier, boost_active, life, x_inimigo, y_inimigo
   
    if px.btnp(px.KEY_Q):
        px.quit()
    
    if px.btn(px.KEY_RIGHT):
        x = min(x + velocidade, px.width - 16)  
    elif px.btn(px.KEY_LEFT):
        x = max(x - velocidade, 0)  
    
    elif px.btn(px.KEY_UP):
        #altura limite
        y = max(y - velocidade, 50) 
    elif px.btn(px.KEY_DOWN):
        y = min(y + velocidade, px.height - 16)
    
    # Ativa o boost quando a tecla de espaço for pressionada
    if px.btnp(px.KEY_SPACE):
        boost_active = True
    
    # Desativa o boost após um certo tempo
    if boost_active:
        velocidade = 3 * boost_multiplier  # Ajuste o valor de multiplicação conforme necessário
        boost_active = False
    else:
        velocidade = 1


    #colisão cor 
    cor = px.pget(x, y)
    if cor == 5:
        x = x -5
        y = y -5
    
    if verifica_colisao (x, y, x+15, y+15, 8):
        life = life - 1
    
    if px.btn(px.KEY_C):
        bala (x_tiro, y_tiro)

        def draw ():
            pex.rect()


def draw():
    
    global life
    px.cls(0)
    px.rect(0, 80, 160, 20, 5)
    px.rect(30,200,130,20,5)
    px.blt(x,y,0,0,0,16,16,13)
    
    px.circ(x_inimigo, y_inimigo, 30, 8)
    px.text(70, 60, str(life) , px.frame_count % 16)


px.init(320, 240, title="miguelzin studios")
px.image(0).load(0,0,'cat_16x16.png')
px.run(update, draw)
