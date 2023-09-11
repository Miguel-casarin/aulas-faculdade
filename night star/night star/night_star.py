import pyxel as px

class Game():
    def __init__(self):

        self.x_inicial = 10
        self.y_inicial = 216

        self.pose= 0 

        self.cenario_images = ["cenario_1.png", "cenario_2.png", "cenario_3.png"]
        self.current_cenario = 0

        self.life_player = 100
        
        self.velocidade = 1
        self.boost_multiplier = 5
        self.boost_active = False


        px.init(256, 256, title="miguelzin studios")
        px.image(0).load(0, 0, 'cat_16x16.png')
        px.image(1).load(0, 0, self.cenario_images[self.current_cenario])
        px.run(self.update, self.draw)

    def keys(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_D):
            self.x_inicial = min(self.x_inicial + self.velocidade, px.width - 16)
            self.change_background_if_needed()  # Troque o cenário quando o jogador se move para a direita
        elif px.btn(px.KEY_A):
            self.x_inicial = max(self.x_inicial - self.velocidade, 0)
        elif px.btn(px.KEY_W):
            self.y_inicial = max(self.y_inicial - self.velocidade, 30)
        elif px.btn(px.KEY_S):
            self.y_inicial = min(self.y_inicial + self.velocidade, px.height - 40) #40 ta definindo o limite com o chão

        # Ativa o impulso quando a tecla de espaço for pressionada
        if px.btnp(px.KEY_C):
            self.boost_active = True

        # Desativa o impulso após um certo tempo
        if self.boost_active:
            self.velocidade = 3 * self.boost_multiplier
            self.boost_active = False
        else:
            self.velocidade = 1

    def change_background_if_needed(self):
        # Alterne o cenário quando o jogador se move para a direita
        if self.x_inicial >= px.width - 16:
            self.load_next_cenario()

    def load_next_cenario(self):
        self.current_cenario = (self.current_cenario + 1) % len(self.cenario_images)
        px.image(1).load(0, 0, self.cenario_images[self.current_cenario])
        self.x_inicial = 0  # Reposiciona o jogador do lado esquerdo

    def update(self):
        self.keys()

    def draw(self):
        
        px.cls(0)
        px.blt(0, 0, 1, 0, 0, px.width, px.height)
        px.blt(self.x_inicial, self.y_inicial, 0, 0, 0, 16, 16, 13)


Game()