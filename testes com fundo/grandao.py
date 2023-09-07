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

        self.largura_tela = 270
        self.altura_tela = 240

        self.camera_x = 0  # Posição X da câmera
        self.camera_y = 0  # Posição Y da câmera

        px.init(self.largura_tela, self.altura_tela, title="miguelzin studios")
        px.image(0).load(0, 0, 'cat_16x16.png')
        px.image(1).load(0, 0, "limite.png")
        px.run(self.update, self.draw)

    def keys(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_RIGHT):
            self.x += self.velocidade
        elif px.btn(px.KEY_LEFT):
            self.x -= self.velocidade
        elif px.btn(px.KEY_UP):
            self.y -= self.velocidade
        elif px.btn(px.KEY_DOWN):
            self.y += self.velocidade

        if px.btnp(px.KEY_SPACE):
            self.boost_active = True

        if self.boost_active:
            self.velocidade = 3 * self.boost_multiplier
            self.boost_active = False
        else:
            self.velocidade = 1

        if px.btnp(px.KEY_C):
            self.disparar_tiro()

    def verifica_colisao(self, x1, y1, x2, y2, cor):
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
            self.x -= 5
            self.y -= 5

        for tiro in self.tiros:
            if tiro['ativo']:
                tiro['y'] -= self.tiro_velocidade
        for tiro in self.tiros:
            if tiro['ativo'] and px.pget(tiro['x'], tiro['y']) == 8:
                tiro['ativo'] = False
                self.life -= 10

    def draw(self):
        px.cls(0)  # Limpe a tela com a cor de fundo padrão (cor 0)

        # Desenhe a imagem de fundo com o deslocamento da câmera
        px.blt(-self.camera_x, -self.camera_y, 1, 0, 0, px.width, px.height)

        # Desenhe o jogador
        px.blt(self.x, self.y, 0, 0, 0, 16, 16, 13)

        # Desenhe tiros ativos
        for tiro in self.tiros:
            if tiro['ativo']:
                px.rect(tiro['x'], tiro['y'], tiro['x'] + 2, tiro['y'] + 6, 12)

        # Desenhe outras partes do jogo, como colisões e vida
        px.circ(self.x_inimigo, self.y_inimigo, 30, 8)
        px.text(70, 60, str(self.life), px.frame_count % 16)

        # Atualize a tela
        px.flip()

# Inicialize o jogo
Jogo()
