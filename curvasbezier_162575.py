import math
import pyxel as px

class Curva_de_bezier:
    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3, color):
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.color = color
    
    def calculo_pontos(self, t):
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        
        x = b0 * self.x0 + b1 * self.x1 + b2 * self.x2 + b3 * self.x3
        y = b0 * self.y0 + b1 * self.y1 + b2 * self.y2 + b3 * self.y3
        return x, y
    
    def calculo_tang_vetor(self, t):
        d0 = -3 * (1 - t) ** 2
        d1 = 3 * (1 - t) ** 2 - 6 * (1 - t) * t
        d2 = 6 * (1 - t) * t - 3 * t ** 2
        d3 = 3 * t ** 2
        
        dx = d0 * self.x0 + d1 * self.x1 + d2 * self.x2 + d3 * self.x3
        dy = d0 * self.y0 + d1 * self.y1 + d2 * self.y2 + d3 * self.y3
        return dx, dy
    
    def draw_curva(self, t, previous_x, previous_y):
        for i in range(int(t * 100) + 1):
            t_step = i / 100
            x, y = self.calculo_pontos(t_step)
            if i > 0:
                px.line(previous_x, previous_y, x, y, self.color)
            previous_x, previous_y = x, y
        return previous_x, previous_y
    
    def draw_vetores(self, t):
        x, y = self.calculo_pontos(t)
        dx, dy = self.calculo_tang_vetor(t)
        d = math.sqrt(dx * dx + dy * dy)
        
        px.line(x, y, x + 10 * dx / d, y + 10 * dy / d, 7)  
        px.line(x, y, x - 10 * dy / d, y + 10 * dx / d, 10) 
        px.circ(x, y, 2, 8)  

class Texto:
    def __init__(self, texto, cor):
        self.texto = texto
        self.cor = cor
    
    def desenha_texto(self):
        largura_texto = len(self.texto) * 4  
        px.text(px.width - largura_texto - 2, px.height - 10, self.texto, self.cor)

texto = Texto("Miguel C. da Silva, 162575", 7)  

# Pontos de controle para a curva superior e inferior
curva1 = Curva_de_bezier(20, 40, 60, 200, 160, 50, 180, 20, 11)    
curva2 = Curva_de_bezier(20, 160, 60, 0, 160, 150, 180, 180, 3)    

def update():
    global t
    t = (px.frame_count / 180) % 1  

def draw():
    px.cls(0)
    
    # Desenha as curvas
    previous_x1, previous_y1 = curva1.x0, curva1.y0
    previous_x2, previous_y2 = curva2.x0, curva2.y0
    previous_x1, previous_y1 = curva1.draw_curva(t, previous_x1, previous_y1)
    previous_x2, previous_y2 = curva2.draw_curva(t, previous_x2, previous_y2)
    
    # Desenha os vetores tangente 
    curva1.draw_vetores(t)
    curva2.draw_vetores(t)

    texto.desenha_texto()
    
px.init(200, 200)
px.run(update, draw)
