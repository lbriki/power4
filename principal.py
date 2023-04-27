import numpy as np
import pygame
import sys
import math
from pygame import mixer
from collections import namedtuple
import page3
mixer.init()
yay = pygame.mixer.Sound('./sounds/yay.mp3')

ROW_COUNT = 6
COLUMN_COUNT = 7
BLACK = (0, 0, 0)
Color = namedtuple('RGB','red, green, blue')
class RGB(Color):
    Color = BLACK
    def hex_format(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red,self.green,self.blue)
ALICEBLUE = RGB(240, 248, 255)
PINK1 = RGB(255, 70, 70)
ANTIQUEWHITE = RGB(250, 235, 215)
LAWNGREEN = RGB(255, 80, 60)
BLUE=RGB(0, 0, 255)
RED = RGB(255, 0, 0)
YELLOW = RGB(255, 255, 0)

def start():
    mixer.init()
    sound = pygame.mixer.Sound('./sounds/sound.mp3')
    mixer.Channel(0).play(sound)

    class board():
        def __init__(self):
            self.lg = ROW_COUNT
            self.col = COLUMN_COUNT
            self.board= np.zeros((ROW_COUNT, COLUMN_COUNT))

        def drop_piece(self, row, col, piece):
            self.board[row][col] = piece
        def is_valid_location(self, col):
            return self.board[ROW_COUNT - 1][col] == 0
        def get_next_open_row(self, col):
            for r in range(ROW_COUNT):
                if self.board[r][col] == 0:
                    return r
        def print_board(self):
            print(np.flip(self.board, 0))
        def winning_move(self, piece):
            # Check horizontal locations for win
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT):
                    if self.board[r][c] == piece and self.board[r][c + 1] == piece and self.board[r][c + 2] == piece and self.board[r][
                        c + 3] == piece:
                        return True

            # Check vertical locations for win
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT - 3):
                    if self.board[r][c] == piece and self.board[r + 1][c] == piece and self.board[r + 2][c] == piece and self.board[r + 3][
                        c] == piece:
                        return True

            # Check positively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT - 3):
                    if self.board[r][c] == piece and self.board[r + 1][c + 1] == piece and self.board[r + 2][c + 2] == piece and self.board[r + 3][
                        c + 3] == piece:
                        return True

            # Check negatively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(3, ROW_COUNT):
                    if self.board[r][c] == piece and self.board[r - 1][c + 1] == piece and self.board[r - 2][c + 2] == piece and self.board[r - 3][
                        c + 3] == piece:
                        return True
        def draw_board(self):
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    pygame.draw.rect(screen, RED, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                    pygame.draw.circle(screen, PINK1, (
                    int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    if self.board[r][c] == 1:
                        pygame.draw.circle(screen, BLACK , (
                        int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
                    elif self.board[r][c] == 2:
                        pygame.draw.circle(screen,ANTIQUEWHITE , (
                        int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            pygame.display.update()


    b = board()
    b.print_board()

    game_over = False
    turn = 0
    b.print_board()
    #pygame.display.update()
    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    pygame.init()
    b.draw_board()
    b.print_board()
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, LAWNGREEN, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, BLACK, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, ANTIQUEWHITE, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if b.is_valid_location(col):
                        row = b.get_next_open_row( col)
                        b.drop_piece( row, col, 1)

                        if b.winning_move( 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True


                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if b.is_valid_location( col):
                        row = b.get_next_open_row( col)
                        b.drop_piece( row, col, 2)

                        if b.winning_move( 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                b.print_board()
                b.draw_board()

                turn += 1
                turn = turn % 2

        if game_over:
            mixer.Channel(0).play(yay)
            pygame.time.wait(2000)
            page3.go()
            pygame.quit()
#start()


