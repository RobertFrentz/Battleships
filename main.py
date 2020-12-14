import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Battleships")
game_icon = pygame.image.load("Resources/Battleships_icon.jpg")
game_background = pygame.image.load("Resources/Battleships_background.png")
start_button = pygame.image.load("Resources/Battleships_startbutton.png")
start_button_rect = start_button.get_rect()
start_button_rect.topleft = (300, 500)

pygame.display.set_icon(game_icon)

battleship_color_red_button_player_1 = pygame.Rect(270, 150, 50, 50)
battleship_color_blue_button_player_1 = pygame.Rect(370, 150, 50, 50)
battleship_color_green_button_player_1 = pygame.Rect(470, 150, 50, 50)

battleship_color_red_button_player_2 = pygame.Rect(270, 350, 50, 50)
battleship_color_blue_button_player_2 = pygame.Rect(370, 350, 50, 50)
battleship_color_green_button_player_2 = pygame.Rect(470, 350, 50, 50)

big_font = pygame.font.SysFont('roboto', 70)
small_font = pygame.font.SysFont('roboto', 30)

color_button1_player_1 = (255, 0, 0)
color_button2_player_1 = (0, 255, 0)
color_button3_player_1 = (0, 0, 255)
color_button1_player_2 = (255, 0, 0)
color_button2_player_2 = (0, 255, 0)
color_button3_player_2 = (0, 0, 255)

game_running = True
game_scene = 'Main menu'


def draw_main_menu_scene():
    player_1 = big_font.render('Player 1', True, (255, 255, 255))
    player_2 = big_font.render('Player 2', True, (255, 255, 255))
    choose_battleship_color = small_font.render('Choose your battleship color', True, (255, 255, 255))
    start_button_text = small_font.render('Start Game', True, (255, 255, 255))
    window.blit(player_1, (300, 50))
    window.blit(player_2, (300, 250))
    window.blit(start_button, start_button_rect)
    window.blit(start_button_text, (345, 530))
    window.blit(choose_battleship_color, (250, 110))
    window.blit(choose_battleship_color, (250, 310))
    pygame.draw.rect(window, color_button1_player_1, battleship_color_red_button_player_1)
    pygame.draw.rect(window, color_button2_player_1, battleship_color_green_button_player_1)
    pygame.draw.rect(window, color_button3_player_1, battleship_color_blue_button_player_1)
    pygame.draw.rect(window, color_button1_player_2, battleship_color_red_button_player_2)
    pygame.draw.rect(window, color_button2_player_2, battleship_color_green_button_player_2)
    pygame.draw.rect(window, color_button3_player_2, battleship_color_blue_button_player_2)


def draw_game_scene():
    pass


while game_running:
    window.fill((0, 0, 0))
    window.blit(game_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if game_scene == 'Main menu':
                if start_button_rect.collidepoint(x, y):
                    game_scene = 'Game Playing'
                if battleship_color_red_button_player_1.collidepoint(x, y):
                    color_button1_player_1 = (255, 128, 128)
                    color_button2_player_1 = (0, 255, 0)
                    color_button3_player_1 = (0, 0, 255)
                if battleship_color_green_button_player_1.collidepoint(x, y):
                    color_button1_player_1 = (255, 0, 0)
                    color_button2_player_1 = (128, 255, 128)
                    color_button3_player_1 = (0, 0, 255)
                if battleship_color_blue_button_player_1.collidepoint(x, y):
                    color_button1_player_1 = (255, 0, 0)
                    color_button2_player_1 = (0, 255, 0)
                    color_button3_player_1 = (128, 128, 255)
                if battleship_color_red_button_player_2.collidepoint(x, y):
                    color_button1_player_2 = (255, 128, 128)
                    color_button2_player_2 = (0, 255, 0)
                    color_button3_player_2 = (0, 0, 255)
                if battleship_color_green_button_player_2.collidepoint(x, y):
                    color_button1_player_2 = (255, 0, 0)
                    color_button2_player_2 = (128, 255, 128)
                    color_button3_player_2 = (0, 0, 255)
                if battleship_color_blue_button_player_2.collidepoint(x, y):
                    color_button1_player_2 = (255, 0, 0)
                    color_button2_player_2 = (0, 255, 0)
                    color_button3_player_2 = (128, 128, 255)

    if game_scene == 'Main menu':
        draw_main_menu_scene()
    if game_scene == 'Game Playing':
        draw_game_scene()

    pygame.display.update()
