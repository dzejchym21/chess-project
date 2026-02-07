import pygame
from constaints import *
from visuals_and_assets_loader import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGES = load_images()
pygame.display.set_caption('Chess Game')
pygame.display.set_icon(IMAGES['logo'])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_board(screen)
    pygame.display.update()