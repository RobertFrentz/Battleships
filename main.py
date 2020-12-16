import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

# Resources
pygame.display.set_caption("Battleships")
game_icon = pygame.image.load("Resources/Battleships_icon.jpg")
game_background = pygame.image.load("Resources/Battleships_background.png")
button = pygame.image.load("Resources/Battleships_default_button.png")
grid_rectangle = pygame.image.load("Resources/rectangle_transparent.png")

# Resources rectangles
start_button_rect = button.get_rect()
back_button_rect = button.get_rect()
done_button_rect = button.get_rect()
reset_button_rect = button.get_rect()
start_button_rect.topleft = (320, 500)
back_button_rect.topleft = (0, 0)
done_button_rect.topleft = (650, 430)
reset_button_rect.topleft = (650, 500)

pygame.display.set_icon(game_icon)

# Main menu colored rectangles
battleship_color_red_button_player_1_rect = pygame.Rect(270, 150, 50, 50)
battleship_color_blue_button_player_1_rect = pygame.Rect(370, 150, 50, 50)
battleship_color_green_button_player_1_rect = pygame.Rect(470, 150, 50, 50)

battleship_color_red_button_player_2_rect = pygame.Rect(270, 350, 50, 50)
battleship_color_blue_button_player_2_rect = pygame.Rect(370, 350, 50, 50)
battleship_color_green_button_player_2_rect = pygame.Rect(470, 350, 50, 50)

# Fonts
big_font = pygame.font.SysFont('roboto', 70)
small_font = pygame.font.SysFont('roboto', 25)

# Texts (main menu scene)
player_1_text = big_font.render('Player 1', True, (255, 255, 255))
player_2_text = big_font.render('Player 2', True, (255, 255, 255))
choose_battleship_color_text = small_font.render('Choose your battleship color', True, (255, 255, 255))
same_players_color_text = small_font.render('Players must have different colors for their battleship!', True,
                                            (255, 0, 0))
start_button_text = small_font.render('Start Game', True, (255, 255, 255))

# Texts (choosing battleships scene)
player_1_turn_text = big_font.render('Player 1 turn', True, (255, 255, 255))
player_2_turn_text = big_font.render('Player 2 turn', True, (255, 255, 255))
instructions1_text = small_font.render('Instructions: Select 6 adjacent horizontally or vertically tiles to '
                                       'deploy your '
                                       'battleship.', True, (255, 255, 255))
instructions2_text = small_font.render(
    'Left click to select tile. If you change your mind left click on the selected tile to unselect it.',
    True, (255, 255, 255))
back_button_text = small_font.render('Back', True, (255, 255, 255))
done_button_text = small_font.render('Done', True, (255, 255, 255))
reset_button_text = small_font.render('Reset', True, (255, 255, 255))
invalid_done_text = small_font.render('You need to select 6 tiles in order to continue!', True, (255, 0, 0))

# Main menu rectangles set colors
color_button1_player_1 = (255, 128, 128)
color_button2_player_1 = (0, 255, 0)
color_button3_player_1 = (0, 0, 255)
color_button1_player_2 = (255, 0, 0)
color_button2_player_2 = (128, 255, 128)
color_button3_player_2 = (0, 0, 255)

game_running = True
game_scene = 'Main menu'
player_turn = 1
grid_created = False
grid_rectangles_list = []
player_1_battleship = []
player_2_battleship = []
player_1_battleship_color = (255, 0, 0)
player_2_battleship_color = (0, 255, 0)
players_same_color = False
valid_done = True
valid_tile_selection = True


# Functions
def create_grid():
    global grid_rectangles_list
    grid_rectangle_element = grid_rectangle.get_rect()
    grid_rectangle_element.topleft = (80, 150)
    grid_rectangles_list.append(grid_rectangle_element)
    for i in range(0, 7):
        if i == 0:
            for j in range(1, 7):
                grid_rectangle_new_element = grid_rectangle.get_rect()
                grid_rectangle_new_element.topleft = grid_rectangles_list[j - 1].topright
                grid_rectangles_list.append(grid_rectangle_new_element)
        else:
            for j in range(0, 7):
                grid_rectangle_new_element = grid_rectangle.get_rect()
                grid_rectangle_new_element.topleft = grid_rectangles_list[7 * (i - 1) + j].bottomleft
                grid_rectangles_list.append(grid_rectangle_new_element)


def draw_grid():
    global grid_rectangles_list
    global grid_created
    if not grid_created:
        create_grid()
        grid_created = True
    else:
        for grid_element in grid_rectangles_list:
            window.blit(grid_rectangle, grid_element)


def draw_main_menu_scene():
    window.blit(player_1_text, (300, 50))
    window.blit(player_2_text, (300, 250))
    window.blit(button, start_button_rect)
    window.blit(start_button_text, (345, 520))
    window.blit(choose_battleship_color_text, (275, 110))
    window.blit(choose_battleship_color_text, (275, 310))
    if players_same_color:
        window.blit(same_players_color_text, (150, 570))

    pygame.draw.rect(window, color_button1_player_1, battleship_color_red_button_player_1_rect)
    pygame.draw.rect(window, color_button2_player_1, battleship_color_green_button_player_1_rect)
    pygame.draw.rect(window, color_button3_player_1, battleship_color_blue_button_player_1_rect)
    pygame.draw.rect(window, color_button1_player_2, battleship_color_red_button_player_2_rect)
    pygame.draw.rect(window, color_button2_player_2, battleship_color_green_button_player_2_rect)
    pygame.draw.rect(window, color_button3_player_2, battleship_color_blue_button_player_2_rect)


def draw_choosing_battleships_scene():
    draw_grid()
    window.blit(instructions1_text, (50, 100))
    window.blit(instructions2_text, (50, 120))
    window.blit(button, back_button_rect)
    window.blit(button, done_button_rect)
    window.blit(button, reset_button_rect)
    window.blit(back_button_text, (50, 20))
    window.blit(done_button_text, (700, 450))
    window.blit(reset_button_text, (700, 520))
    if player_turn == 1:
        window.blit(player_1_turn_text, (250, 30))
        for rect in player_1_battleship:
            battleship_tile = pygame.Rect(rect.x + 20, rect.y + 10, 40, 40)
            pygame.draw.rect(window, player_1_battleship_color, battleship_tile)
    elif player_turn == 2:
        window.blit(player_2_turn_text, (250, 30))
        for rect in player_2_battleship:
            battleship_tile = pygame.Rect(rect.x + 20, rect.y + 10, 40, 40)
            pygame.draw.rect(window, player_2_battleship_color, battleship_tile)
    if not valid_done:
        window.blit(invalid_done_text, (200, 580))


def is_tile_selection_valid(player_number, element_to_check):
    if player_number == 1:
        for rect in player_1_battleship:
            if rect.x == element_to_check.x and (rect.y + 60 == element_to_check.y or rect.y - 60 == element_to_check.y):
                return True
            if rect.y == element_to_check.y and (rect.x + 80 == element_to_check.x or rect.x - 80 == element_to_check.x):
                return True
        return False
    elif player_number == 2:

        for rect in player_2_battleship:
            if rect.x == element_to_check.x and (
                    rect.y + 60 == element_to_check.y or rect.y - 60 == element_to_check.y):
                return True
            if rect.y == element_to_check.y and (
                    rect.x + 80 == element_to_check.x or rect.x - 80 == element_to_check.x):
                return True
        return False


# Game loop
while game_running:
    window.fill((0, 0, 0))
    window.blit(game_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if game_scene == 'Main menu':
                players_same_color = False
                if start_button_rect.collidepoint(x, y):
                    if player_1_battleship_color == player_2_battleship_color:
                        players_same_color = True
                    else:
                        game_scene = 'Choosing battleships'
                        players_same_color = False
                if battleship_color_red_button_player_1_rect.collidepoint(x, y):
                    player_1_battleship_color = (255, 0, 0)
                    color_button1_player_1 = (255, 128, 128)
                    color_button2_player_1 = (0, 255, 0)
                    color_button3_player_1 = (0, 0, 255)
                if battleship_color_green_button_player_1_rect.collidepoint(x, y):
                    player_1_battleship_color = (0, 255, 0)
                    color_button1_player_1 = (255, 0, 0)
                    color_button2_player_1 = (128, 255, 128)
                    color_button3_player_1 = (0, 0, 255)
                if battleship_color_blue_button_player_1_rect.collidepoint(x, y):
                    player_1_battleship_color = (0, 0, 255)
                    color_button1_player_1 = (255, 0, 0)
                    color_button2_player_1 = (0, 255, 0)
                    color_button3_player_1 = (128, 128, 255)
                if battleship_color_red_button_player_2_rect.collidepoint(x, y):
                    player_2_battleship_color = (255, 0, 0)
                    color_button1_player_2 = (255, 128, 128)
                    color_button2_player_2 = (0, 255, 0)
                    color_button3_player_2 = (0, 0, 255)
                if battleship_color_green_button_player_2_rect.collidepoint(x, y):
                    player_2_battleship_color = (0, 255, 0)
                    color_button1_player_2 = (255, 0, 0)
                    color_button2_player_2 = (128, 255, 128)
                    color_button3_player_2 = (0, 0, 255)
                if battleship_color_blue_button_player_2_rect.collidepoint(x, y):
                    player_2_battleship_color = (0, 0, 255)
                    color_button1_player_2 = (255, 0, 0)
                    color_button2_player_2 = (0, 255, 0)
                    color_button3_player_2 = (128, 128, 255)
            elif game_scene == 'Choosing battleships':
                if back_button_rect.collidepoint(x, y):
                    game_scene = 'Main menu'
                    player_1_battleship = []
                    player_2_battleship = []
                elif done_button_rect.collidepoint(x, y):
                    if player_turn == 1:
                        if len(player_1_battleship) == 6:
                            player_turn = 2
                            valid_done = True
                        else:
                            valid_done = False
                    elif player_turn == 2:
                        if len(player_2_battleship) == 6:
                            game_scene = 'Game Started'
                            valid_done = True
                        else:
                            valid_done = False
                elif reset_button_rect.collidepoint(x, y):
                    if player_turn == 1:
                        player_1_battleship = []
                    elif player_turn == 2:
                        player_2_battleship = []
                else:
                    for element in grid_rectangles_list:
                        if element.collidepoint(x, y):
                            valid_tile_selection = True
                            if player_turn == 1:
                                if element in player_1_battleship:
                                    continue
                                else:
                                    if 6 > len(player_1_battleship) > 0:
                                        if is_tile_selection_valid(1, element):
                                            player_1_battleship.append(element)
                                        else:
                                            valid_tile_selection = False
                                    elif len(player_1_battleship) == 0:
                                        player_1_battleship.append(element)

                            elif player_turn == 2:
                                if element in player_2_battleship:
                                    continue
                                else:
                                    if 6 > len(player_2_battleship) > 0:
                                        if is_tile_selection_valid(2, element):
                                            player_2_battleship.append(element)
                                        else:
                                            valid_tile_selection = False
                                    elif len(player_2_battleship) == 0:
                                        player_2_battleship.append(element)
                        valid_done = True

    if game_scene == 'Main menu':
        draw_main_menu_scene()
    if game_scene == 'Choosing battleships':
        draw_choosing_battleships_scene()

    pygame.display.update()
