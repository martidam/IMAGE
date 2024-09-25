import pygame
pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

'''Write your code between this'''
CENTER = (300, 300)
RADIUS = 100
START = (100, 100)
END = (500, 500)
pygame.draw.line(display_surface, RED , START, END )


pygame.draw.circle(display_surface, RED , CENTER, RADIUS)


X = 100
Y = 400
WIDTH = 75
HEIGHT = 150
rect = pygame.Rect (X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, RED, rect)

X = 400
Y = 100
WIDTH = 75
HEIGHT = 150
rect = pygame.Rect (X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, RED, rect)

X = 400
Y = 100
WIDTH = 10
HEIGHT = 200
rect = pygame.Rect (X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, RED, rect)
X = 420
Y = 100
WIDTH = 10
HEIGHT = 200
rect = pygame.Rect (X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, RED, rect)

X = 440
Y = 100
WIDTH = 10
HEIGHT = 200
rect = pygame.Rect (X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, RED, rect)

X = 460
Y = 100
WIDTH = 10
HEIGHT = 200
rect = pygame.Rect (X, Y, WIDTH, HEIGHT)
pygame.draw.rect(display_surface, RED, rect)


'''And this'''

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()