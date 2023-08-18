import pyxel as px

x = 50
y = 50

velocidade = 1

boost_multiplier = 5  # Fator de multiplicação para o boost
boost_active = False  # Indica se o boost está ativo

def update():

    global x, y, velocidade, boost_multiplier, boost_active
    
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


def draw():
    px.cls(0)
    px.rect(0, 80, 160, 20, 5)
    px.rect(30,200,130,20,5)
    px.blt(x,y,0,0,0,16,16,13)


px.init(320, 240, title="miguelzin studios")
px.image(0).load(0,0,'cat_16x16.png')
px.run(update, draw)
