import pygame
from constaints import *
from pygame import Rect

def draw_board(scr):
    colors = [LIGHT_SQUARE, DARK_SQUARE]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[(row + col) % 2]
            pygame.draw.rect(scr, color, Rect(col*SQ_SIZE, row*SQ_SIZE + STATUS_BAR_HEIGHT, SQ_SIZE, SQ_SIZE))

def draw_pieces(scr, b, images_dict):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = b.board[row][col]
            if piece != 0:
                img_key = piece.image_name
                img = images_dict[img_key]
                scr.blit(img, (col*SQ_SIZE, row*SQ_SIZE + STATUS_BAR_HEIGHT))


def highlight_square(scr, sq_selected):
    if sq_selected != ():
        r, c = sq_selected
        s = pygame.Surface((SQ_SIZE, SQ_SIZE))
        s.set_alpha(100)
        s.fill(pygame.Color('yellow'))
        scr.blit(s, (c*SQ_SIZE, r*SQ_SIZE + STATUS_BAR_HEIGHT))

#This function loads all graphics and put them into images dictionary
def load_images():
    images = {}
    pieces = ["logo",
                "wP", "wB", "wR", "wN", "wK", "wQ",
                "bP", "bB", "bR", "bN", "bK", "bQ"
              ]
    for piece in pieces:
        full_path = f"assets/{piece}.png"
        img = pygame.image.load(full_path)
        images[piece] = pygame.transform.smoothscale(img, (SQ_SIZE, SQ_SIZE))

    return images

def draw_valid_moves(scr, moves):
    for move in moves:
        r, c = move
        center = (c * SQ_SIZE + SQ_SIZE//2, r * SQ_SIZE + STATUS_BAR_HEIGHT + SQ_SIZE//2)
        pygame.draw.circle(scr, (100, 100, 100), center, 12)

def get_promotion_choice(screen, color, img):
    options = ['Queen', 'Knight', 'Bishop', 'Rook']
    choice = None

    menu_width = 410
    menu_height = 150
    x_start = (WIDTH - menu_width) // 2
    y_start = (HEIGHT - menu_height) // 2

    while choice is None:
        pygame.draw.rect(screen, (50, 50, 50), (x_start, y_start, menu_width, menu_height))
        pygame.draw.rect(screen, (255, 255, 255), (x_start, y_start, menu_width, menu_height), 2)

        mouse_pos = pygame.mouse.get_pos()
        for i, opt in enumerate(options):
            opt_x = x_start + i * 100 + 10
            opt_y = y_start + 20
            rect = pygame.Rect(opt_x, opt_y, 90, 120)
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (100, 100, 100), rect)
            if opt != 'Knight':
                screen.blit(img[color + opt[0]], (opt_x, opt_y))
            else:
                screen.blit(img[color + 'N'], (opt_x, opt_y))

            font = pygame.font.SysFont("Arial", 18)
            text_surface = font.render(opt, True, (255, 255, 255))
            screen.blit(text_surface, (opt_x + 20, opt_y + 90))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                for i in range(4):
                    if x_start + i * 100 < mx < x_start + (i + 1) * 100:
                        return options[i]


def draw_status_bar(screen, board):
    game_status = board.check_end_game()
    if game_status == 'checkmate':
        text = "Checkmate! End game"
        color = (255, 0, 0)
        border = (255, 255, 255)
    elif game_status == 'stalemate':
        text = "Stalemate! Draw"
        color = (200, 200, 200)
        border = (255, 255, 255)
    else:
        if board.white_to_move:
            text = "White to move"
            color = (255, 255, 255)
            border = (0, 0, 0)
        else:
            text = "Black to move"
            color = (0, 0, 0)
            border = (100, 100, 100)

    pygame.draw.rect(screen, color, (0, 0, WIDTH, STATUS_BAR_HEIGHT))
    pygame.draw.rect(screen, border, (0, 0, WIDTH, STATUS_BAR_HEIGHT), 2)
    font = pygame.font.SysFont("Arial", 14)
    text_surface = font.render(text, True, border)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, STATUS_BAR_HEIGHT // 2))
    screen.blit(text_surface, text_rect)
