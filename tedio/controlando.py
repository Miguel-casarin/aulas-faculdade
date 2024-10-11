import pygame
from pygame.locals import QUIT, K_a, K_d, K_w, K_s

pygame.init()
fps = pygame.time.Clock()
running = True

screen_x = 640
screen_y = 480

screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption('miguelzin studios')

player_coordenate_x, player_coordenate_y = 320, 240  # Posição inicial do jogador
player = pygame.image.load("DinoSprites_mort.gif")
player_rect = player.get_rect(topleft=(player_coordenate_x, player_coordenate_y))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    # Atualiza as coordenadas do jogador
    player_coordenate_x += (keys[K_d] - keys[K_a]) * 5
    player_coordenate_y += (keys[K_s] - keys[K_w]) * 5
    
    # Garante que o jogador não saia dos limites da tela
    x = max(0, min(player_coordenate_x, screen_x - player_rect.width))
    y = max(0, min(player_coordenate_y, screen_y - player_rect.height))

    player_rect.topleft = (x, y)

    screen.fill((0, 0, 0))
    screen.blit(player, player_rect.topleft)
    pygame.display.flip()

    fps.tick(30)
