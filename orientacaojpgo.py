import pyxel as px 

class Jogo():
    def __init__(self):

        self.x = 50
        self.y = 50
        self.life = 200 
        self.velocidade = 1

        self.x_inimigo = 200
        self.y_inimigo = 150

        self.boost_multiplier = 5  
        self.boost_active = False

        self.tiros = []
        self.tiro_velocidade = 3 

        px.init(320, 240, title="miguelzin studios")
        px.image(0).load(0,0,'cat_16x16.png')
        px.run(self.update, self.draw)

    def keys(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_RIGHT):
            self.x = min(self.x + self.velocidade, px.width - 16)
        elif px.btn(px.KEY_LEFT):
            self.x = max(self.x - self.velocidade, 0)
        elif px.btn(px.KEY_UP):
            self.y = max(self.y - self.velocidade, 50)
        elif px.btn(px.KEY_DOWN):
            self.y = min(self.y + self.velocidade, px.height - 16)
    
        # Ativa o impulso quando a tecla de espaço for pressionada
        if px.btnp(px.KEY_SPACE):
            self.boost_active = True
    
        # Desativa o impulso após um certo tempo
        if self.boost_active:
            self.velocidade = 3 * self.boost_multiplier  
            self.boost_active = False
        else:
            self.velocidade = 1
        #tiro
        if px.btnp(px.KEY_C):
            self.boost_active = True
            self.disparar_tiro() 

    def verifica_colisao(self,x1, y1, x2, y2, cor):
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
    def disparar_tiro(self):
        novo_tiro = {'x': self.x + 6, 'y': self.y, 'ativo': True}
        self.tiros.append(novo_tiro)

    def update(self):
        self.keys()

        cor = px.pget(self.x, self.y)
        if cor == 5:
            self.x = self.x -5
            self.y = self.y -5
    
        if self.verifica_colisao (self.x, self.y, self.x+15, self.y+15, 8):
            self.life = self.life - 1

        # Atualizar posições dos tiros
        for tiro in self.tiros:
            if tiro['ativo']:
                tiro['y'] -= self.tiro_velocidade    
        # Verificar colisões entre tiros e inimigos
        for tiro in self.tiros:
            if tiro['ativo'] and px.pget(tiro['x'], tiro['y']) == 8:  # Cor do inimigo
                tiro['ativo'] = False
                self.life -= 10
        
        

    def draw(self):
        px.cls(0)
        px.rect(0, 80, 160, 20, 5)
        px.rect(30, 200, 130, 20, 5)
        px.blt(self.x, self.y, 0, 0, 0, 16, 16, 13)

         # Desenhar tiros ativos
        for tiro in self.tiros:
            if tiro['ativo']:
                px.rect(tiro['x'], tiro['y'], tiro['x'] + 2, tiro['y'] + 6, 12)

        #colisao
        px.circ(self.x_inimigo, self.y_inimigo, 30, 8)
        px.text(70, 60, str(self.life), px.frame_count % 16)

Jogo()