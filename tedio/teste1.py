import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((640, 480))

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Load player image and background image
player = pygame.image.load("DinoSprites_mort.gif")
background = pygame.image.load("map1.png")

# Get the rectangle representing the player's position
position = player.get_rect()

# Set up the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.blit(background, (0, 0))

    # Update player position
    position = position.move(2, 0)

    # Draw the player on the updated position
    screen.blit(player, position)

    # Update the display
    pygame.display.update()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
