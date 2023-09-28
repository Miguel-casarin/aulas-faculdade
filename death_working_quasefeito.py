finalizar a colisão entre objetos

import pyxel as px

class Game():
    def __init__(self):

        self.x_inicial = 50
        self.y_inicial = 40
        
        self.x_inimigo = 220
        self.y_inimigo = 190


        self.cenario_images = ["cenario_1.png", "cenario_2.png", "cenario_3.png"]
        self.current_cenario = 0

        self.life_player = 100
        
        self.velocidade = 1
        self.boost_multiplier = 5
        self.boost_active = False
        
        self.disparo_active = False
        
        self.tiros_x = []
        self.tiros_y = []

        self.altura_limite_pulo = 90  # Altura máxima que a tecla "W" pode subir
        self.jump_height = -60  # Altura do pulo (negativa para ir para cima)
        self.gravity = 0.5      # Valor da gravidade
        self.jump_active = False
        self.y_velocity = 0.5

        # Contador de tempo para o atraso da tecla "W"
        self.jump_delay = 30  # Define o tempo de atraso em quadros
        self.jump_delay_counter = 0

        px.init(256, 256, title="miguelzin studios")
        px.image(0).load(0, 0, 'dread2.png')
        px.image(2).load(0,0,'gosth.png')
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

        # Lógica para o pulo limitado com atraso
        if self.jump_delay_counter <= 0 and px.btn(px.KEY_W) and self.y_inicial > self.altura_limite_pulo:
            self.y_inicial = max(self.y_inicial - self.velocidade, self.altura_limite_pulo)
            self.jump_delay_counter = self.jump_delay  # Define o contador de atraso

        elif self.jump_delay_counter > 0:
            self.jump_delay_counter -= 1

        elif px.btn(px.KEY_S):
            self.y_inicial = min(self.y_inicial + self.velocidade, px.height - 10 ) #40 ta definindo o limite com o chão

        # Ativa o impulso quando a tecla de espaço for pressionada
        if px.btnp(px.KEY_SPACE):
            self.boost_active = True

        # Desativa o impulso após um certo tempo
        if self.boost_active:
            self.velocidade = 3 * self.boost_multiplier
            self.boost_active = False
        else:
            self.velocidade = 1

        # Adiciona a lógica para pular reto para cima
        if px.btnp(px.KEY_W):
            self.y_inicial -= 50
            
        if px.btnp(px.KEY_P):
            tiro = self.tiros_x 
            self.tiros_x.append(self.x_inicial + 20)
            self.tiros_y.append(self.y_inicial)

    def change_background_if_needed(self):
        # Alterne o cenário quando o jogador se move para a direita
        if self.x_inicial >= px.width - 16:
            self.load_next_cenario()

    def load_next_cenario(self):
        self.current_cenario = (self.current_cenario + 1) % len(self.cenario_images)
        px.image(1).load(0, 0, self.cenario_images[self.current_cenario])
        self.x_inicial = 0  # Reposiciona o jogador do lado esquerdo

    def apply_gravity(self):
        if not self.jump_active:
            self.y_velocity += self.gravity
            self.y_inicial += self.y_velocity

            # Impedir que o jogador caia abaixo do chão
            if self.y_inicial >= px.height - 65:
                self.y_inicial = px.height - 65
                self.jump_active = False
                self.y_velocity = 0
                
    
    def movimenta_inimigo(self):
        if self.x_inimigo != -30:
            self.x_inimigo = self.x_inimigo - 0.5
            if self.x_inimigo <= -30:
                self.x_inimigo = 260
    
    #bonder box do inimigo, tiros
    def verifica_tiro_inimigo(self.tiros_x, self.tiros_y):
        
        if self.tiros_x > self.x_inimigo and self.tiros_y > self.y_inimigo:
            return True
        else:
            return False
        
        
    
    
    
        
            

    def update(self):
        self.keys()
        self.apply_gravity()
        self.movimenta_inimigo()

    def draw(self):
        
        px.cls(0)
        px.blt(0, 0, 1, 0, 0, px.width, px.height)
        px.blt(self.x_inicial, self.y_inicial, 0, 0, 0, 30, 30, 13)
        px.blt(self.x_inimigo, self.y_inimigo, 2, 0, 0, 30, 30, 13)
        if len(self.tiros_x) != 0:
            for i in range (len(self.tiros_x)):
                self.tiros_x[i]+=3
                px.rect(self.tiros_x[i], self.tiros_y[i] + 12, 5,5,8)
        
   
Game()