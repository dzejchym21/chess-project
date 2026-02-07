import pygame
from constaints import *
from visuals_and_assets_loader import *
from engine.board import Board
from engine.Pieces import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGES = load_images()
pygame.display.set_caption('Chess Game')
pygame.display.set_icon(IMAGES['logo'])
pygame.display.flip()

sq_selected = () # it's a selected square
player_clicks = [] # it's a table containing player move: [(square_from), (square_to)]
board = Board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()
            col = location[0] // SQ_SIZE
            row = location[1] // SQ_SIZE

            # if a square is already selected, we deselect it
            if sq_selected == (row, col):
                sq_selected = ()
                player_clicks = []
            else:
                sq_selected = (row, col)
                player_clicks.append(sq_selected)

            #if len(player_clicks) == 2:
            # TODO:
            #  add player movement logic (getting piece object, valid moves and finally making the move)


    draw_board(screen)
    highlight_square(screen, sq_selected)
    draw_pieces(screen, board, IMAGES)
    pygame.display.update()