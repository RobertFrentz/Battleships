import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Battleships")
game_icon = pygame.image.load("Resources/Battleships_icon.jpg")
pygame.display.set_icon(game_icon)

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    window.fill((0, 0, 0))
    pygame.display.update()
