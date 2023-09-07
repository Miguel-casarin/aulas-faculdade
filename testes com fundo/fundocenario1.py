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

        # Lista de cenários (imagens)
        self.cenario_images = ["cenario_1.png", "cenario_2.png", "cenario_3.png"]
        self.current_cenario = 0  # Índice do cenário atual

        px.init(256, 256, title="miguelzin studios")
        px.image(0).load(0, 0, 'cat_16x16.png')
        px.image(1).load(0, 0, self.cenario_images[self.current_cenario])
        px.run(self.update, self.draw)

    def keys(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_RIGHT):
            self.x = min(self.x + self.velocidade, px.width - 16)
            self.change_background_if_needed()  # Troque o cenário quando o jogador se move para a direita
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

    def change_background_if_needed(self):
        # Alterne o cenário quando o jogador se move para a direita
        if self.x >= px.width - 16:
            self.load_next_cenario()

    def load_next_cenario(self):
        self.current_cenario = (self.current_cenario + 1) % len(self.cenario_images)
        px.image(1).load(0, 0, self.cenario_images[self.current_cenario])
        self.x = 0  # Reposiciona o jogador do lado esquerdo

    def update(self):
        self.keys()

    def draw(self):
        px.cls(0)
        px.blt(0, 0, 1, 0, 0, px.width, px.height)
        px.blt(self.x, self.y, 0, 0, 0, 16, 16, 13)

Jogo()
