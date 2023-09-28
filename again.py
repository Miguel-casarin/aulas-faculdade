# Arrumar o sistema de gravidade que parrou de funcionar, fazer uma classe para mudar os cenários e criar a classe e a mecânica no inimigo
# o trabalho de ontem foi pequeno mas com bons passos, agora arruma o resto ai 
# ideia fazer uma classe somente para as keys, pois a logica de mudar o cenario usa meu x inicial 

import pyxel as px

class Cenario:
        def __init__(self):
            self.cenario_images = ["cenario_1.png", "cenario_2.png", "cenario_3.png"]
            self.current_cenario = 0

            px.image(1).load(0, 0, self.cenario_images[self.current_cenario])
     
        def change_background_if_needed(self):
        # Alterne o cenário quando o jogador se move para a direita
            if self.x_inicial >= px.width - 16:
                self.load_next_cenario()

        def load_next_cenario(self):
            self.current_cenario = (self.current_cenario + 1) % len(self.cenario_images)
            px.image(0).load(0, 0, self.cenario_images[self.current_cenario])
            self.x_inicial = 0  # Reposiciona o jogador do lado esquerdo

class Inimigo:
    def __init__(self):
        self.x_inimigo = 100
        self.y_inimigo = 80

    def update(self):
        pass

    def draw(self):
        pass

class Player:
    def __init__(self):
        
        self.x_inicial = 50
        self.y_inicial = 40
        
        self.life_player = 100
        
        self.velocidade = 1
        self.boost_multiplier = 5
        self.boost_active = False
        
        self.disparo_active = False
        self.tiros = []
        
        self.altura_limite_pulo = 90
        self.jump_height = -60
        self.gravity = 0.5
        self.jump_active = False
        self.y_velocity = 0.0
        
        self.jump_delay = 30
        self.jump_delay_counter = 0

        self.cenario = Cenario()
        
        
        px.init(256, 256, title="miguelzin studios")
        px.image(0).load(0, 0, 'dread2.png')
        
        px.run(self.update, self.draw)

    def keys(self):
        if px.btnp(px.KEY_Q):
            px.quit()

        if px.btn(px.KEY_D):
            self.x_inicial = min(self.x_inicial + self.velocidade, px.width - 16)
            self.cenario.change_background_if_needed()

        elif px.btn(px.KEY_A):
            self.x_inicial = max(self.x_inicial - self.velocidade, 0)

        if self.jump_delay_counter <= 0 and px.btn(px.KEY_W) and self.y_inicial > self.altura_limite_pulo:
            self.y_inicial = max(self.y_inicial - self.velocidade, self.altura_limite_pulo)
            self.jump_delay_counter = self.jump_delay

        elif self.jump_delay_counter > 0:
            self.jump_delay_counter -= 1


        if px.btnp(px.KEY_SPACE):
            self.boost_active = True

        if self.boost_active:
            self.velocidade = 3 * self.boost_multiplier
            self.boost_active = False
        else:
            self.velocidade = 1

        if px.btnp(px.KEY_W):
            self.jump_active = True
            self.y_velocity = self.jump_height

        if px.btnp(px.KEY_P):
            tiro = self.x_inicial
            self.tiros.append(tiro)

    def apply_gravity(self):
        if not self.jump_active:
            self.y_velocity += self.gravity
            self.y_inicial += self.y_velocity

            if self.y_inicial >= px.height - 65:
                self.y_inicial = px.height - 65
                self.jump_active = False
                self.y_velocity = 0

    def update(self):
        self.keys()
        self.apply_gravity()

    def draw(self):
        px.cls(0)  # Clear the screen
        px.blt(self.x_inicial, self.y_inicial, 0, 0, 0, 30, 30, 13)
        for i in range(len(self.tiros)):
            self.tiros[i] += 3
            px.rect(self.tiros[i], self.y_inicial + 12, 5, 5, 8)

class Keyss(self):
    def __init__(self):
        pass

class Game:
    def __init__(self):
        self.personagem = Player()
        self.inimigo = Inimigo()

if __name__ == "__main__":
    Game()
