import pygame
import time

win_size = 500
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((win_size, win_size))
pygame.display.set_caption('snake war game!')
row = 20
gap = win_size // row
line_coordinate = gap
end = win_size - line_coordinate
x_change = 0
y_change = 0
starting = False
start = False


def draw_snake(array, length, array2, length2):
    global line_coordinate, win, image
    win.blit(image, (0, 0))
    blue = (0, 204, 204)
    blue_body = (51, 255, 153)
    red = (204, 0, 0)
    red_body = (255, 51, 51)
    if len(array) != 0 and len(array2) != 0:
        for i in range(length):
            if i == 0:
                pygame.draw.rect(win, red, (array[i][0] + 2, array[i][1] + 1, line_coordinate - 2, line_coordinate - 2))
            else:
                pygame.draw.rect(win, red_body,
                                 (array[i][0] + 2, array[i][1] + 1, line_coordinate - 2, line_coordinate - 2))
        for i in range(length2):
            if i == 0:
                pygame.draw.rect(win, blue,
                                 (array2[i][0] + 2, array2[i][1] + 1, line_coordinate - 2, line_coordinate - 2))
            else:
                pygame.draw.rect(win, blue_body,
                                 (array2[i][0] + 2, array2[i][1] + 1, line_coordinate - 2, line_coordinate - 2))
    clock.tick(7)
    pygame.display.update()


def render_message(player, player2, message_number):
    global winner, starting_pos2, starting_pos1
    font = pygame.font.SysFont('comicsansms', 27)
    if message_number == 1:
        message = font.render('{} player entered outside boundary'.format(player), True, (255, 251, 5))
        message1 = font.render('{} player WON'.format(player2), True, (255, 251, 5))
        pygame.draw.rect(win, (204, 0, 204), (14, 225, 480, 35))
        pygame.draw.rect(win, (204, 0, 204), (155, 265, 220, 35))
        win.blit(message, (22, 225))
        win.blit(message1, (160, 260))
    elif message_number == 2:
        message = font.render('{} player bit himself'.format(player), True, (255, 251, 5))
        message1 = font.render('{} player WON'.format(player2), True, (255, 251, 5))
        pygame.draw.rect(win, (204, 0, 204), (95, 223, 315, 35))
        pygame.draw.rect(win, (204, 0, 204), (155, 265, 225, 35))
        win.blit(message, (100, 225))
        win.blit(message1, (160, 260))
    elif message_number == 3:
        message = font.render('{} have eaten each others head'.format(player), True, (255, 251, 5))
        message1 = font.render('ITS A DRAW', True, (255, 251, 5))
        pygame.draw.rect(win, (204, 0, 204), (2, 232, 500, 35))
        pygame.draw.rect(win, (204, 0, 204), (167, 265, 177, 35))
        win.blit(message, (5, 225))
        win.blit(message1, (170, 260))
        starting_pos2.clear()
        starting_pos2.clear()
    elif message_number == 4:
        message = font.render('{} player WON'.format(player), True, (255, 251, 5))
        pygame.draw.rect(win, (204, 0, 204), (157, 232, 230, 35))
        win.blit(message, (160, 228))
    pygame.display.update()
    time.sleep(5)
    winner = True


def kill(array1, array2):
    global player1_length, player2_length
    head1 = array1[0]
    head2 = array2[0]
    if head1 == head2:
        render_message('red - blue', 'none', 3)
    elif head1 in array2:
        player2_length -= 1
    elif head2 in array1:
        player1_length -= 1
    elif head1 in array1[1:]:
        render_message('red', 'blue', 2)
    elif head2 in array2[1:]:
        render_message('blue', 'red', 2)


def starting_message():
    global start
    font = pygame.font.SysFont('comicsansms', 27)
    message = font.render('click up/down to start', True, (255, 0, 0))
    pygame.draw.rect(win, (0, 200, 0), (120, 185, 290, 30))
    win.blit(message, (125, 180))
    pygame.display.update()


def win_match(array1, array2):
    if len(array1) == 1:
        render_message('blue', 'red', 4)
    if len(array2) == 1:
        render_message('red', 'blue', 4)


def play():
    global start
    global line_coordinate, starting_pos1, starting_pos2, player1_loose, player2_loose, winner
    player1_x_coordinate = starting_pos1[0][0]
    player1_y_coordinate = starting_pos1[0][1]
    player2_x_coordinate = starting_pos2[0][0]
    player2_y_coordinate = starting_pos2[0][1]
    player1_x_change = 0
    player1_y_change = 0
    player2_x_change = 0
    player2_y_change = 0
    player1_direction_x = False
    player1_direction_y = True
    player2_direction_x = False
    player2_direction_y = True
    start1 = False
    start2 = False
    # to draw the grid line structure of the screen
    while not winner:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                winner = True
                pygame.quit()
                quit()
            if events.type == pygame.KEYDOWN:
                start = True
                if player1_direction_y:
                    if events.key == pygame.K_s:
                        start1 = True
                        player1_y_change = line_coordinate
                        player1_x_change = 0
                        player1_direction_x = True
                        player1_direction_y = False
                    if events.key == pygame.K_w:
                        start1 = True
                        player1_y_change = -line_coordinate
                        player1_x_change = 0
                        player1_direction_x = True
                        player1_direction_y = False
                elif player1_direction_x:
                    if events.key == pygame.K_d:
                        player1_x_change = line_coordinate
                        player1_y_change = 0
                        player1_direction_x = False
                        player1_direction_y = True
                    if events.key == pygame.K_a:
                        player1_x_change = -line_coordinate
                        player1_y_change = 0
                        player1_direction_x = False
                        player1_direction_y = True

                if player2_direction_y:
                    if events.key == pygame.K_DOWN:
                        start2 = True
                        player2_y_change = line_coordinate
                        player2_x_change = 0
                        player2_direction_x = True
                        player2_direction_y = False
                    if events.key == pygame.K_UP:
                        start2 = True
                        player2_y_change = -line_coordinate
                        player2_x_change = 0
                        player2_direction_x = True
                        player2_direction_y = False
                elif player2_direction_x:
                    if events.key == pygame.K_RIGHT:
                        player2_x_change = line_coordinate
                        player2_y_change = 0
                        player2_direction_x = False
                        player2_direction_y = True
                    if events.key == pygame.K_LEFT:
                        player2_x_change = -line_coordinate
                        player2_y_change = 0
                        player2_direction_x = False
                        player2_direction_y = True
        if not start:
            starting_message()

        if start1 and start2:
            kill(starting_pos1, starting_pos2)
        win_match(starting_pos1, starting_pos2)
        player1_x_coordinate += player1_x_change
        player1_y_coordinate += player1_y_change
        player2_x_coordinate += player2_x_change
        player2_y_coordinate += player2_y_change

        if 0 > player1_x_coordinate or player1_x_coordinate > end or 0 > player1_y_coordinate or \
                player1_y_coordinate > end:
            render_message('red', 'blue', 1)
            starting_pos1.clear()
        if 0 > player2_x_coordinate or player2_x_coordinate > end or 0 > player2_y_coordinate or \
                player2_y_coordinate > end:
            render_message('blue', 'red', 1)
            starting_pos2.clear()

        if start1:
            starting_pos1.insert(0, [player1_x_coordinate, player1_y_coordinate])
            starting_pos1.pop()
        if start2:
            starting_pos2.insert(0, [player2_x_coordinate, player2_y_coordinate])
            starting_pos2.pop()
        draw_snake(starting_pos1, player1_length, starting_pos2, player2_length)
    pygame.display.update()


starting_pos1 = [[line_coordinate * 6, line_coordinate * 10],
                 [line_coordinate * 5, line_coordinate * 10],
                 [line_coordinate * 4, line_coordinate * 10],
                 [line_coordinate * 3, line_coordinate * 10],
                 [line_coordinate * 2, line_coordinate * 10],
                 [line_coordinate * 1, line_coordinate * 10]]
starting_pos2 = [[line_coordinate * 14, line_coordinate * 10],
                 [line_coordinate * 15, line_coordinate * 10],
                 [line_coordinate * 16, line_coordinate * 10],
                 [line_coordinate * 17, line_coordinate * 10],
                 [line_coordinate * 18, line_coordinate * 10],
                 [line_coordinate * 19, line_coordinate * 10]]
image = pygame.image.load('images/grid.png')
player1_length = 6
player2_length = 6
winner = False
player1_loose = False
player2_loose = False

play()
