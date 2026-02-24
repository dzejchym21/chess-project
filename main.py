import pygame
from constaints import *
from constaints import STATUS_BAR_HEIGHT
from visuals_and_assets_loader import *
from engine.board import *
from engine.ai import *
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

# Here we choose if the player is white or black
player_one_human = True # White pieces
player_two_human = False # Black pieces

running = True
while running:
    is_human_turn = (board.white_to_move and player_one_human) or (not board.white_to_move and player_two_human)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_over and is_human_turn:
                location = pygame.mouse.get_pos()
                #coordinates (row number, column number)
                col = location[0] // SQ_SIZE
                row = (location[1] - STATUS_BAR_HEIGHT) // SQ_SIZE

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
                    if sq_to in valid_moves:
                        move = Move(sq_from, sq_to, board)
                        if move.is_promotion:
                            choice = get_promotion_choice(screen, move.piece_moved.color, IMAGES)
                            board.make_move(move,is_virtual=True, promoted_to=choice)
                        else:
                            board.make_move(move, is_virtual=True)

                        game_status = board.check_end_game()
                        print(board.move_log)
                        if game_status:
                            print(f"Game Over: {game_status}")
                            game_over = True

                    sq_selected = ()
                    player_clicks = []
                    valid_moves = []

        #elif event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_u:
        #        board.undo_move()
        #        sq_selected = ()
        #        player_clicks = []
        #        print("Cofnięto ruch!")

    if not game_over and not is_human_turn:
        ai_move = find_best_move(board)
        if ai_move:
            pygame.time.delay(400)
            board.make_move(ai_move, is_virtual=True, promoted_to='Queen')

            sq_selected = ()
            player_clicks = []
            valid_moves = []

        game_status = board.check_end_game()
        if game_status:
            game_over = True

    draw_board(screen)
    draw_status_bar(screen, board)
    highlight_square(screen, sq_selected)
    if len(valid_moves) > 0:
        draw_valid_moves(screen, valid_moves)
    draw_pieces(screen, board, IMAGES)
    pygame.display.update()