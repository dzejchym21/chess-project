import pygame
from constaints import *
from visuals_and_assets_loader import *
from engine.board import Board
from engine.pieces import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGES = load_images()
pygame.display.set_caption('Chess Game')
pygame.display.set_icon(IMAGES['logo'])
pygame.display.flip()

sq_selected = () # it's a selected square
player_clicks = [] # it's a table containing player move: [(square_from), (square_to)]
valid_moves = []
board = Board()
game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over:
                location = pygame.mouse.get_pos()
                #coordinates (row number, column number)
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE

                # if a square is already selected, we deselect it
                if sq_selected == (row, col):
                    sq_selected = ()
                    player_clicks = []
                    valid_moves = []
                else:
                    if len(player_clicks) == 0:
                        piece = board.get_piece(row, col)
                        if piece != 0 and ((board.white_to_move and piece.color == 'w') or (not board.white_to_move and piece.color == 'b')):
                            sq_selected = (row, col)
                            player_clicks.append(sq_selected)
                            valid_moves = board.get_legal_moves(piece)
                    elif len(player_clicks) == 1:
                        sq_selected = (row, col)
                        player_clicks.append(sq_selected)
                if len(player_clicks) == 2:
                    sq_from = player_clicks[0]
                    sq_to = player_clicks[1]

                    if board.make_move(sq_from, sq_to):
                        game_status = board.check_end_game()
                        if game_status:
                            print(f"Game Over: {game_status}")
                            game_over = True

                    sq_selected = ()
                    player_clicks = []
                    valid_moves = []

    draw_board(screen)
    highlight_square(screen, sq_selected)
    if len(valid_moves) > 0:
        draw_valid_moves(screen, valid_moves)
    draw_pieces(screen, board, IMAGES)
    pygame.display.update()