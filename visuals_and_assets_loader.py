import pygame
from constaints import *
from pygame import Rect

def draw_board(scr):
    colors = [LIGHT_SQUARE, DARK_SQUARE]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[(row + col) % 2]
            pygame.draw.rect(scr, color, Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def load_images():
    images = {}
    pieces = ["logo"]
    for piece in pieces:
        full_path = f"assets/{piece}.png"
        img = pygame.image.load(full_path)
        images[piece] = img

    return images