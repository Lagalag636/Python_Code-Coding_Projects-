import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pygame Example')
text_color = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.draw.circle(screen, GREEN, (400, 300), 75) #(place, color, (x, y), radius)
pygame.draw.line(screen, BLUE, (700, 100), (700, 500), 5) #(place, color, (x-start, y-start), (x-end, y-end), width)
pygame.draw.ellipse(screen, BLUE, (380, 50, 200, 100)) #(place, color, #rect#(x, y, length, width), width=0 for fill or number for thick line)
pygame.draw.polygon(screen, GREEN, [(200, 350), (200, 450), (250, 450), (250, 550), (200, 350)])  #(surface, color, pointlist, width=0 for fill or number for thick line)
pygame.draw.arc(screen, RED, (100, 100, 200, 200), 0, 180, 5) #Arc from 0 to 180 degrees #(place, color, #rect#(x, y, length, width), start angle, stop angle, width)
points = [(300, 500), (400, 450), (500, 500), (600, 400), (700, 500)] #pointlist
pygame.draw.lines(screen, BLUE, False, points, 3)  #(place, color, whether lines are open or closed, pointlist, width)

print("I work, I promise...")