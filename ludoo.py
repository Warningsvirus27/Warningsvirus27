import pygame
import random
from pygame import mixer


def draw(name, x, y):
    screen.blit(name, (x, y))


def roll_dice():
    box = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 8]
    # box = [2]
    return box[random.randint(0, len(box)) - 1]


def listing_of_player(self, piece2, player):
    a = []
    player_list = (p11, p12, p13, p14, p24, p23, p22, p21)
    if player == 1:
        for x in player_list[0:4]:
            if x.piece == self.piece:
                a.append(x)
        for y in player_list[4:]:
            if y.piece == piece2:
                a.append(y)
    elif player == 2:
        for x in player_list[4:]:
            if x.piece == self.piece:
                a.append(x)
        for y in player_list[0:4]:
            if y.piece == piece2:
                a.append(y)

    return a


def pieces_together(self, player):
    together = []
    if self.piece == 0 or self.piece == 4 or self.piece == 8 or self.piece == 12 or self.piece == 24:
        if self.piece == 0:
            together = listing_of_player(self, 8, player)
        elif self.piece == 4:
            together = listing_of_player(self, 12, player)
        elif self.piece == 8:
            together = listing_of_player(self, 0, player)
        elif self.piece == 12:
            together = listing_of_player(self, 4, player)
        elif self.piece == 24:
            together = listing_of_player(self, 24, player)
    else:
        if 0 < self.piece < 9:
            together = listing_of_player(self, self.piece + 8, player)
        elif 8 < self.piece < 16:
            together = listing_of_player(self, self.piece - 8, player)
        elif 15 < self.piece < 20:
            together = listing_of_player(self, self.piece + 4, player)
        elif 19 < self.piece < 24:
            together = listing_of_player(self, self.piece - 4, player)
    cross_box(together)


def cross_box(a):
    # print('cross called')
    if len(a) == 8:
        a[0].x = a[0].board[a[0].piece][0] - 26
        a[0].y = a[0].board[a[0].piece][1] - 26
        a[1].x = a[1].board[a[1].piece][0] - 1
        a[1].y = a[1].board[a[1].piece][1] - 26
        a[2].x = a[2].board[a[2].piece][0] + 24
        a[2].y = a[2].board[a[2].piece][1] - 26
        a[3].x = a[3].board[a[3].piece][0] - 26
        a[3].y = a[3].board[a[3].piece][1]
        a[4].x = a[4].board[a[4].piece][0] - 26
        a[4].y = a[4].board[a[4].piece][1] + 28
        a[5].x = a[5].board[a[5].piece][0] - 1
        a[5].y = a[5].board[a[5].piece][1] + 28
        a[6].x = a[6].board[a[6].piece][0] + 24
        a[6].y = a[6].board[a[6].piece][1] + 28
        a[7].x = a[7].board[a[7].piece][0] + 24
        a[7].y = a[7].board[a[7].piece][1]
    elif len(a) == 7:
        a[0].x = a[0].board[a[0].piece][0] - 10
        a[0].y = a[0].board[a[0].piece][1] - 20
        a[1].x = a[1].board[a[1].piece][0] + 15
        a[1].y = a[1].board[a[1].piece][1] - 20
        a[2].x = a[2].board[a[2].piece][0] - 25
        a[2].y = a[2].board[a[2].piece][1]
        a[3].x = a[3].board[a[3].piece][0]
        a[3].y = a[3].board[a[3].piece][1]
        a[4].x = a[4].board[a[4].piece][0] + 25
        a[4].y = a[4].board[a[4].piece][1]
        a[5].x = a[5].board[a[5].piece][0] - 10
        a[5].y = a[5].board[a[5].piece][1] + 20
        a[6].x = a[6].board[a[6].piece][0] + 15
        a[6].y = a[6].board[a[6].piece][1] + 20
    elif len(a) == 6:
        a[0].x = a[0].board[a[0].piece][0] - 10
        a[0].y = a[0].board[a[0].piece][1] - 20
        a[1].x = a[1].board[a[1].piece][0] + 15
        a[1].y = a[1].board[a[1].piece][1] - 20
        a[2].x = a[2].board[a[2].piece][0] - 25
        a[2].y = a[2].board[a[2].piece][1]
        a[3].x = a[3].board[a[3].piece][0] + 30
        a[3].y = a[3].board[a[3].piece][1]
        a[4].x = a[4].board[a[4].piece][0] - 10
        a[4].y = a[4].board[a[4].piece][1] + 20
        a[5].x = a[5].board[a[5].piece][0] + 15
        a[5].y = a[5].board[a[5].piece][1] + 20
    elif len(a) == 5:
        a[0].x = a[0].board[a[0].piece][0] - 10
        a[0].y = a[0].board[a[0].piece][1] - 20
        a[1].x = a[1].board[a[1].piece][0] + 15
        a[1].y = a[1].board[a[1].piece][1] - 20
        a[2].x = a[2].board[a[2].piece][0] + 2
        a[2].y = a[2].board[a[2].piece][1]
        a[3].x = a[3].board[a[3].piece][0] - 10
        a[3].y = a[3].board[a[3].piece][1] + 20
        a[4].x = a[4].board[a[4].piece][0] + 15
        a[4].y = a[4].board[a[4].piece][1] + 20
    elif len(a) == 4:
        a[0].x = a[0].board[a[0].piece][0] - 15
        a[0].y = a[0].board[a[0].piece][1] - 15
        a[1].x = a[1].board[a[1].piece][0] + 15
        a[1].y = a[1].board[a[1].piece][1] - 15
        a[2].x = a[2].board[a[2].piece][0] - 15
        a[2].y = a[2].board[a[2].piece][1] + 15
        a[3].x = a[3].board[a[3].piece][0] + 15
        a[3].y = a[3].board[a[3].piece][1] + 15
    elif len(a) == 3:
        a[0].x = a[0].board[a[0].piece][0]
        a[0].y = a[0].board[a[0].piece][1] - 10
        a[1].x = a[1].board[a[1].piece][0] - 15
        a[1].y = a[1].board[a[1].piece][1] + 10
        a[2].x = a[2].board[a[2].piece][0] + 15
        a[2].y = a[2].board[a[2].piece][1] + 10
    elif len(a) == 2:
        a[0].x = a[0].board[a[0].piece][0] - 15
        a[0].y = a[0].board[a[0].piece][1]
        a[1].x = a[1].board[a[1].piece][0] + 15
        a[1].y = a[1].board[a[1].piece][1]
    elif len(a) == 1:
        a[0].x = a[0].board[a[0].piece][0]
        a[0].y = a[0].board[a[0].piece][1]


def kill(self, player, second_player):
    global enter_player1, enter_player2
    box = []
    if self.piece == 0 or self.piece == 4 or self.piece == 8 or self.piece == 12 or self.piece == 24:
        return 0
    else:
        if 0 < self.piece < 9:
            box = listing_of_player(self, self.piece + 8, player)
        elif 8 < self.piece < 16:
            box = listing_of_player(self, self.piece - 8, player)
        elif 15 < self.piece < 20:
            box = listing_of_player(self, self.piece + 4, player)
        elif 19 < self.piece < 24:
            box = listing_of_player(self, self.piece - 4, player)
        if len(box) == 2:
            player1 = str(box[0])
            player2 = str(box[1])
            if player1[24] == player2[24]:
                pass
            else:
                box.remove(self)
                box[0].piece = 0
                box[0].x = box[0].board[box[0].piece][0]
                box[0].y = box[0].board[box[0].piece][1]
                killed_piece = str(box[0])
                if killed_piece[24] == '1':
                    enter_player2 = True
                else:
                    enter_player1 = True
                check_killed_piece_spacing(box[0], second_player)
                return 1
        else:
            return 0


def check_killed_piece_spacing(self, player):
    pieces_together(self, player)


def starting():
    global dice
    global set_player1, set_player2, start2, start1
    if set_player1:
        if not start1:
            if dice == 1:
                start1 = True
            else:
                dice = roll_dice()
                set_player2 = True
                set_player1 = False
                start_note()

    elif set_player2:
        if not start2:
            if dice == 1:
                start2 = True
            else:
                dice = roll_dice()
                set_player2 = False
                set_player1 = True
                start_note()


def draw_winner_message(player):
    font = pygame.font.Font('freesansbold.ttf', 40)
    text11 = font.render('CONGRATULATIONS', True, (255, 0, 0))
    text12 = font.render('PLAYER 1', True, (255, 0, 0))
    text13 = font.render('WINS THE GAME!', True, (255, 0, 0))
    text21 = font.render('CONGRATULATIONS', True, (255, 0, 0))
    text22 = font.render('PLAYER 2', True, (255, 0, 0))
    text23 = font.render('WINS THE GAME!', True, (255, 0, 0))
    if player == 1:
        pygame.draw.rect(screen, (255, 255, 255), (48, 165, 420, 48))
        draw(text11, 50, 170)
        pygame.draw.rect(screen, (255, 255, 255), (160, 210, 210, 53))
        draw(text12, 170, 220)
        pygame.draw.rect(screen, (255, 255, 255), (88, 260, 360, 50))
        draw(text13, 90, 270)
    elif player == 2:
        pygame.draw.rect(screen, (255, 255, 255), (48, 165, 420, 48))
        draw(text21, 50, 170)
        pygame.draw.rect(screen, (255, 255, 255), (160, 210, 210, 53))
        draw(text22, 170, 220)
        pygame.draw.rect(screen, (255, 255, 255), (88, 260, 360, 50))
        draw(text23, 90, 270)


def winner():
    global winner1, winner2
    if p11.piece == p12.piece == p13.piece == p14.piece == 24:
        winner1 = True
    elif p21.piece == p22.piece == p23.piece == p24.piece == 24:
        winner2 = True


def have_to_kill():
    font = pygame.font.Font('freesansbold.ttf', 28)
    notice_to_kill_1 = font.render('Kill at least one piece of opponent', True, (255, 65, 0))
    notice_to_kill_2 = font.render('to enter the inner block', True, (255, 65, 0))
    pygame.draw.rect(screen, (255, 255, 255), (7, 242, 478, 35))
    pygame.draw.rect(screen, (255, 255, 255), (72, 267, 322, 35))
    draw(notice_to_kill_1, 10, 245)
    draw(notice_to_kill_2, 75, 270)


def restart(p1, p2, p3, p4):
    global dice
    if p1.piece == p2.piece == p3.piece == p4.piece == 15:
        p1.piece += dice - 16
        p1.x = p1.board[p1.piece][0]
        p1.y = p1.board[p1.piece][1]
        print('return 1')
        return 1
    print('return 0')
    return 0


class MovementPlayer2:
    def __init__(self, x, y, img_var, num):
        self.num = num
        self.piece = 0
        self.image = img_var
        self.x = x
        self.y = y
        self.defaultx = x
        self.defaulty = y

        # to set the outlook for the board for player 2
        # self.map0 = (self.defaultx, self.defaulty)
        self.map0 = (240, 430 - (80 * 4))
        self.map1 = (240 - 80, 430 - (80 * 4))
        self.map2 = (240 - (80 * 2), 430 - (80 * 4))
        self.map3 = (240 - (80 * 2), 430 - (80 * 3))
        self.map4 = (240 - (80 * 2), 430 - (80 * 2))
        self.map5 = (240 - (80 * 2), 430 - 80)
        self.map6 = (240 - (80 * 2), 430)
        self.map7 = (240 - 80, 430)
        self.map8 = (240, 430)
        self.map9 = (240 + 80, 430)
        self.map10 = (240 + (80 * 2), 430)
        self.map11 = (240 + (80 * 2), 430 - 80)
        self.map12 = (240 + (80 * 2), 430 - (80 * 2))
        self.map13 = (240 + (80 * 2), 430 - (80 * 3))
        self.map14 = (240 + (80 * 2), 430 - (80 * 4))
        self.map15 = (240 + 80, 430 - (80 * 4))
        self.map16 = (240 + 80, 430 - (80 * 3))
        self.map17 = (240 + 80, 430 - (80 * 2))
        self.map18 = (240 + 80, 430 - 80)
        self.map19 = (240, 430 - 80)
        self.map20 = (240 - 80, 430 - 80)
        self.map21 = (240 - 80, 430 - (80 * 2))
        self.map22 = (240 - 80, 430 - (80 * 3))
        self.map23 = (240, 430 - (80 * 3))
        self.map24 = (240, 430 - (80 * 2))

        self.board = (self.map0, self.map1, self.map2, self.map3, self.map4, self.map5,
                      self.map6, self.map7, self.map8, self.map9, self.map10, self.map11,
                      self.map12, self.map13, self.map14, self.map15, self.map16, self.map17,
                      self.map18, self.map19, self.map20, self.map21, self.map22, self.map23,
                      self.map24)

    def move(self):
        global dice
        global set_player1, kill_show
        global set_player2, enter_player2

        if self.piece != 24:
            self.piece = self.piece + dice
            if self.piece > 15:
                if enter_player2:
                    can_play = True
                else:
                    self.piece -= dice
                    if restart(p21, p22, p23, p24):
                        can_play = True
                        kill_show = False
                    else:
                        can_play = False
                        kill_show = True
            else:
                can_play = True
        else:
            can_play = False

        if self.piece > 24:
            self.piece = self.piece - 8
        laugh = kill(self, 2, 1)

        if laugh:
            mixer.music.load('images/laugh.mp3')
            mixer.music.play()
        pieces_together(self, 2)

        if can_play:
            dice = roll_dice()
            set_player1 = True
            set_player2 = False

        winner()


class MovementPlayer1:
    def __init__(self, x, y, img_var, num):
        self.num = num
        self.piece = 0
        self.image = img_var
        self.x = x
        self.y = y
        self.defaultx = x
        self.defaulty = y

        # to set the outlook for the board for player 1
        # self.map0 = (self.defaultx, self.defaulty)
        self.map0 = (240, 430)
        self.map1 = (240 + 80, 430)
        self.map2 = (240 + (80 * 2), 430)
        self.map3 = (240 + (80 * 2), 430 - 80)
        self.map4 = (240 + (80 * 2), 430 - (80 * 2))
        self.map5 = (240 + (80 * 2), 430 - (80 * 3))
        self.map6 = (240 + (80 * 2), 430 - (80 * 4))
        self.map7 = (240 + 80, 430 - (80 * 4))
        self.map8 = (240, 430 - (80 * 4))
        self.map9 = (240 - 80, 430 - (80 * 4))
        self.map10 = (240 - (80 * 2), 430 - (80 * 4))
        self.map11 = (240 - (80 * 2), 430 - (80 * 3))
        self.map12 = (240 - (80 * 2), 430 - (80 * 2))
        self.map13 = (240 - (80 * 2), 430 - 80)
        self.map14 = (240 - (80 * 2), 430)
        self.map15 = (240 - 80, 430)
        self.map16 = (240 - 80, 430 - 80)
        self.map17 = (240 - 80, 430 - (80 * 2))
        self.map18 = (240 - 80, 430 - (80 * 3))
        self.map19 = (240, 430 - (80 * 3))
        self.map20 = (240 + 80, 430 - (80 * 3))
        self.map21 = (240 + 80, 430 - (80 * 2))
        self.map22 = (240 + 80, 430 - 80)
        self.map23 = (240, 430 - 80)
        self.map24 = (240, 430 - (80 * 2))
        self.board = (self.map0, self.map1, self.map2, self.map3, self.map4, self.map5,
                      self.map6, self.map7, self.map8, self.map9, self.map10, self.map11,
                      self.map12, self.map13, self.map14, self.map15, self.map16, self.map17,
                      self.map18, self.map19, self.map20, self.map21, self.map22, self.map23,
                      self.map24)

    def move(self):
        global dice
        global set_player2, kill_show
        global set_player1, enter_player1
        if self.piece != 24:
            self.piece = self.piece + dice
            if self.piece > 15:
                if enter_player1:
                    can_play = True
                else:
                    self.piece -= dice
                    if restart(p11, p12, p13, p14):
                        can_play = True
                        kill_show = False
                    else:
                        can_play = False
                        kill_show = True
            else:
                can_play = True
        else:
            can_play = False

        if self.piece > 24:
            self.piece = self.piece - 8
        laugh = kill(self, 1, 2)

        if laugh:
            mixer.music.load('images/laugh.mp3')
            mixer.music.play()
        pieces_together(self, 1)
        if can_play:
            dice = roll_dice()
            set_player1 = False
            set_player2 = True

        winner()


def render():
    global dice
    global start1, start2, notify
    font = pygame.font.Font('freesansbold.ttf', 32)
    dice_value = font.render('dice =' + str(dice), True, (255, 255, 255))
    if not start1 and not start2:
        pygame.draw.rect(screen, (255, 0, 0), (195, 257, 125, 35))
        draw(dice_value, 200, 260)
    else:
        notify = False
        pygame.draw.rect(screen, (255, 0, 0), (195, 27, 120, 35))
        draw(dice_value, 200, 30)


def start_note():
    global start1, start2
    font = pygame.font.Font('freesansbold.ttf', 32)
    note = font.render('CAN START WHEN DICE IS "1"', True, (255, 251, 5))
    font = pygame.font.Font('freesansbold.ttf', 20)
    notice = font.render('Click on pieces to roll dice!', True, (255, 251, 5))
    if not start1 and not start2:
        draw(notice, 120, 50)
        draw(note, 11, 10)
    pygame.display.update()


def play():
    running = True
    global dice
    global set_player1
    global set_player2
    global glowp1
    global glowp2
    global start1
    global start2, kill_show

    # game loop
    while running:
        draw(back, 0, 0)
        draw(background, 50, 80)

        # to draw the pieces of player 1
        if glowp1['p11'] == 1:
            draw(player11glow, p11.x - 2, p11.y - 2)
        else:
            draw(player11, p11.x, p11.y)
        if glowp1['p12'] == 1:
            draw(player12glow, p12.x - 2, p12.y - 2)
        else:
            draw(player12, p12.x, p12.y)
        if glowp1['p13'] == 1:
            draw(player13glow, p13.x - 2, p13.y - 2)
        else:
            draw(player13, p13.x, p13.y)
        if glowp1['p14'] == 1:
            draw(player14glow, p14.x - 2, p14.y - 2)
        else:
            draw(player14, p14.x, p14.y)

        # to draw the pieces of player 2
        if glowp2['p21'] == 1:
            draw(player21glow, p21.x - 2, p21.y - 2)
        else:
            draw(player21, p21.x, p21.y)
        if glowp2['p22'] == 1:
            draw(player22glow, p22.x - 2, p22.y - 2)
        else:
            draw(player22, p22.x, p22.y)
        if glowp2['p23'] == 1:
            draw(player23glow, p23.x - 2, p23.y - 2)
        else:
            draw(player23, p23.x, p23.y)
        if glowp2['p24'] == 1:
            draw(player24glow, p24.x - 2, p24.y - 2)
        else:
            draw(player24, p24.x, p24.y)

        render()

        # to print the winnering status!
        if winner1:
            draw_winner_message(1)
        elif winner2:
            draw_winner_message(2)

        # to show to starting notice
        if notify:
            start_note()

        # to show the notice to have to kill a piece to enter the inner loop
        if kill_show:
            have_to_kill()

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()

            # to print the glowing pieces when mouse points to them
            if set_player1:
                if p11.x < pos[0] < (p11.x + 20) and p11.y < pos[1] < (p11.y + 20):
                    if p11.piece != 24:
                        glowp1['p11'] = 1
                elif not (p11.x < pos[0] < (p11.x + 20) and p11.y < pos[1] < (p11.y + 20)):
                    glowp1['p11'] = 0
                if p12.x < pos[0] < (p12.x + 20) and p12.y < pos[1] < (p12.y + 20):
                    if p12.piece != 24:
                        glowp1['p12'] = 1
                elif not (p12.x < pos[0] < (p12.x + 20) and p12.y < pos[1] < (p12.y + 20)):
                    glowp1['p12'] = 0
                if p13.x < pos[0] < (p13.x + 20) and p13.y < pos[1] < (p13.y + 20):
                    if p13.piece != 24:
                        glowp1['p13'] = 1
                elif not (p13.x < pos[0] < (p13.x + 20) and p13.y < pos[1] < (p13.y + 20)):
                    glowp1['p13'] = 0
                if p14.x < pos[0] < (p14.x + 20) and p14.y < pos[1] < (p14.y + 20):
                    if p14.piece != 24:
                        glowp1['p14'] = 1
                elif not (p14.x < pos[0] < (p14.x + 20) and p14.y < pos[1] < (p14.y + 20)):
                    glowp1['p14'] = 0

            elif set_player2:
                if p21.x < pos[0] < (p21.x + 20) and p21.y < pos[1] < (p21.y + 20):
                    if p21.piece != 24:
                        glowp2['p21'] = 1
                elif not (p21.x < pos[0] < (p21.x + 20) and p21.y < pos[1] < (p21.y + 20)):
                    glowp2['p21'] = 0
                if p22.x < pos[0] < (p22.x + 20) and p22.y < pos[1] < (p22.y + 20):
                    if p22.piece != 24:
                        glowp2['p22'] = 1
                elif not (p22.x < pos[0] < (p22.x + 20) and p22.y < pos[1] < (p22.y + 20)):
                    glowp2['p22'] = 0
                if p23.x < pos[0] < (p23.x + 20) and p23.y < pos[1] < (p23.y + 20):
                    if p23.piece != 24:
                        glowp2['p23'] = 1
                elif not (p23.x < pos[0] < (p23.x + 20) and p23.y < pos[1] < (p23.y + 20)):
                    glowp2['p23'] = 0
                if p24.x < pos[0] < (p24.x + 20) and p24.y < pos[1] < (p24.y + 20):
                    if p24.piece != 24:
                        glowp2['p24'] = 1
                elif not (p24.x < pos[0] < (p24.x + 20) and p24.y < pos[1] < (p24.y + 20)):
                    glowp2['p24'] = 0

            # to set the starting of the pieces.
            if events.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not start1 or not start2:
                    starting()

                kill_show = False

                if set_player1:
                    if start1:
                        if p11.x < pos[0] < (p11.x + 20) and p11.y < pos[1] < (p11.y + 20):
                            p11.move()
                            glowp1['p11'] = 0
                        elif p12.x < pos[0] < (p12.x + 20) and p12.y < pos[1] < (p12.y + 20):
                            p12.move()
                            glowp1['p12'] = 0
                        elif p13.x < pos[0] < (p13.x + 20) and p13.y < pos[1] < (p13.y + 20):
                            p13.move()
                            glowp1['p13'] = 0
                        elif p14.x < pos[0] < (p14.x + 20) and p14.y < pos[1] < (p14.y + 20):
                            p14.move()
                            glowp1['p14'] = 0

                if set_player2:
                    if start2:
                        if p21.x < pos[0] < (p21.x + 20) and p21.y < pos[1] < (p21.y + 20):
                            p21.move()
                            glowp2['p21'] = 0
                        elif p22.x < pos[0] < (p22.x + 20) and p22.y < pos[1] < (p22.y + 20):
                            p22.move()
                            glowp2['p22'] = 0
                        elif p23.x < pos[0] < (p23.x + 20) and p23.y < pos[1] < (p23.y + 20):
                            p23.move()
                            glowp2['p23'] = 0
                        elif p24.x < pos[0] < (p24.x + 20) and p24.y < pos[1] < (p24.y + 20):
                            p24.move()
                            glowp2['p24'] = 0

        pygame.display.update()


dice = roll_dice()
set_player1 = True
set_player2 = False
notify = True
winner1 = False
winner2 = False
glowp1 = {'p11': 0, 'p12': 0, 'p13': 0, 'p14': 0}
glowp2 = {'p21': 0, 'p22': 0, 'p23': 0, 'p24': 0}

# to initialize the screen
pygame.init()
screen = pygame.display.set_mode((500, 500))

# to initialize the icon and caption
pygame.display.set_caption("WARNINGSVIRUS27")
icon = pygame.image.load("images/icon.jpg")
pygame.display.set_icon(icon)

# to set the board
background = pygame.image.load("images/ludocrop.png")
back = pygame.image.load('images/back.jpg')

# to initialize the glowing pieces of player 1
player11glow = pygame.image.load("images/ludo 1 p1glow.png")
player12glow = pygame.image.load("images/ludo 2 p1glow.png")
player13glow = pygame.image.load("images/ludo 3 p1glow.png")
player14glow = pygame.image.load("images/ludo 4 p1glow.png")

# to initialize the glowing pieces of player2
player21glow = pygame.image.load("images/ludo 1 p2glow.png")
player22glow = pygame.image.load("images/ludo 2 p2glow.png")
player23glow = pygame.image.load("images/ludo 3 p2glow.png")
player24glow = pygame.image.load("images/ludo 4 p2glow.png")

# to initialize the player 1 obs
player11 = pygame.image.load("images/ludo 1 p1.png")
player12 = pygame.image.load("images/ludo 2 p1.png")
player13 = pygame.image.load("images/ludo 3 p1.png")
player14 = pygame.image.load("images/ludo 4 p1.png")

# to initialize the player 2 obs
player21 = pygame.image.load("images/ludo 1 p2.png")
player22 = pygame.image.load("images/ludo 2 p2.png")
player23 = pygame.image.load("images/ludo 3 p2.png")
player24 = pygame.image.load("images/ludo 4 p2.png")

# objects
p11 = MovementPlayer1(215, 430, player11, 1)
p12 = MovementPlayer1(240, 405, player12, 2)
p13 = MovementPlayer1(265, 430, player13, 3)
p14 = MovementPlayer1(240, 455, player14, 4)
p21 = MovementPlayer2(215, 110, player21, 1)
p22 = MovementPlayer2(240, 85, player22, 2)
p23 = MovementPlayer2(265, 110, player23, 3)
p24 = MovementPlayer2(240, 135, player24, 4)

# to set the pieces at default places in order.
pieces_together(p11, 1)
pieces_together(p12, 2)

start1 = False
start2 = False
enter_player1 = False
enter_player2 = False
kill_show = False

play()
