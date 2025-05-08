import math
import sys
import pygame
import time

pygame.init()
pygame.display.set_caption("Turkey Attempt")

width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
ellipse_surface0 = pygame.Surface((width, height))
ellipse_surface1 = pygame.Surface((width, height))
ellipse_surface2 = pygame.Surface((width, height))
ellipse_surface3 = pygame.Surface((width, height))

screen.fill((170, 170, 170))
ellipse_surface0.fill((170, 170, 170))
pygame.display.flip()

clock = pygame.time.Clock()
font = pygame.font.SysFont("Georgia", 20)

pygame.mouse.set_visible(True)
pygame.mouse.set_pos((width // 2, height // 2))

RED = (255, 0, 0)
MID_GRAY = (170, 170, 170)
BLUE = (0, 0, 255)
PURPLE = (210, 0, 210)

while True:
    #pygame.draw.ellipse(ellipse_surface, PURPLE, (width // 2 - 50, height // 2 - 25, 100, 50))
    pygame.draw.ellipse(ellipse_surface0, PURPLE, (400, 200, 50, 100)) #(place, color, #rect#(x, y, length, width), width=0 for fill or number for thick line)
    #pygame.draw.ellipse(ellipse_surface, PURPLE, (width // 2 - 50, height // 2 - 25, 100, 50))
    #pygame.draw.ellipse(ellipse_surface, PURPLE, (width // 2 - 50, height // 2 - 25, 100, 50))

    pygame.transform.rotate(ellipse_surface0, 90)

    screen.blit(ellipse_surface0, (0, 0))
    pygame.draw.circle(screen, PURPLE, (width / 2, height / 2), 150)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    clock.tick(60)  # Limits frame rate to 60 FPS
