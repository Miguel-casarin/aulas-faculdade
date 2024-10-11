import math
import pyxel as px

class BezierCurve:
    def __init__(self, x0, y0, x1, y1, x2, y2, x3, y3, color):
        self.x0, self.y0 = x0, y0
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3
        self.color = color
    
    def calculate_points(self, t):
        b0 = (1 - t) ** 3
        b1 = 3 * (1 - t) ** 2 * t
        b2 = 3 * (1 - t) * t ** 2
        b3 = t ** 3
        
        x = b0 * self.x0 + b1 * self.x1 + b2 * self.x2 + b3 * self.x3
        y = b0 * self.y0 + b1 * self.y1 + b2 * self.y2 + b3 * self.y3
        return x, y
    
    def calculate_tangent_vector(self, t):
        d0 = -3 * (1 - t) ** 2
        d1 = 3 * (1 - t) ** 2 - 6 * (1 - t) * t
        d2 = 6 * (1 - t) * t - 3 * t ** 2
        d3 = 3 * t ** 2
        
        dx = d0 * self.x0 + d1 * self.x1 + d2 * self.x2 + d3 * self.x3
        dy = d0 * self.y0 + d1 * self.y1 + d2 * self.y2 + d3 * self.y3
        return dx, dy
    
    def draw_curve(self, t, previous_x, previous_y):
        for i in range(int(t * 100) + 1):
            t_step = i / 100
            x, y = self.calculate_points(t_step)
            if i > 0:
                px.line(previous_x, previous_y, x, y, self.color)
            previous_x, previous_y = x, y
        return previous_x, previous_y
    
    def draw_vectors(self, t):
        x, y = self.calculate_points(t)
        dx, dy = self.calculate_tangent_vector(t)
        d = math.sqrt(dx * dx + dy * dy)
        
        px.line(x, y, x + 15 * dx / d, y + 15 * dy / d, 8)  
        px.line(x, y, x - 15 * dy / d, y + 15 * dx / d, 9) 
        px.circ(x, y, 3, 10)  

class CustomText:
    def __init__(self, text, color):
        self.text = text
        self.color = color
    
    def draw_text(self):
        text_width = len(self.text) * 4  
        px.text(px.width - text_width - 2, px.height - 10, self.text, self.color)

# Pontos de controle para a nova forma das curvas superior e inferior
curve1 = BezierCurve(30, 50, 90, 150, 130, 80, 170, 30, 5)    
curve2 = BezierCurve(30, 150, 90, 50, 130, 120, 170, 170, 6)    

def update():
    global t
    t = (px.frame_count / 180) % 1  

def draw():
    px.cls(1)  # Alterando a cor de fundo
    
    # Desenha as curvas
    previous_x1, previous_y1 = curve1.x0, curve1.y0
    previous_x2, previous_y2 = curve2.x0, curve2.y0
    previous_x1, previous_y1 = curve1.draw_curve(t, previous_x1, previous_y1)
    previous_x2, previous_y2 = curve2.draw_curve(t, previous_x2, previous_y2)
    
    # Desenha os vetores tangente
    curve1.draw_vectors(t)
    curve2.draw_vectors(t)

px.init(200, 200)
px.run(update, draw)
