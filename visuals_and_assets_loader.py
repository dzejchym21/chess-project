import pygame
from constaints import *
from pygame import Rect

def draw_board(scr):
    colors = [LIGHT_SQUARE, DARK_SQUARE]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[(row + col) % 2]
            pygame.draw.rect(scr, color, Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(scr, b, images_dict):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = b.board[row][col]
            if piece != 0:
                img_key = piece.image_name
                img = images_dict[img_key]
                scr.blit(img, (col*SQ_SIZE, row*SQ_SIZE))


def highlight_square(scr, sq_selected):
    if sq_selected != ():
        r, c = sq_selected
        s = pygame.Surface((SQ_SIZE, SQ_SIZE))
        s.set_alpha(100)
        s.fill(pygame.Color('yellow'))
        scr.blit(s, (c*SQ_SIZE, r*SQ_SIZE))

#This function loads all graphics and put them into images dictionary
def load_images():
    images = {}
    pieces = ["logo", "wP", "bP"]
    for piece in pieces:
        full_path = f"assets/{piece}.png"
        img = pygame.image.load(full_path)
        images[piece] = pygame.transform.smoothscale(img, (SQ_SIZE, SQ_SIZE))

    return images