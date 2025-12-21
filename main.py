import numpy as np
import pygame

#Classes
class Body:
    def __init__(self, mass, radius, accel):
        self.mass = mass
        self.radius = radius
        self.accel = accel
class Button:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect.topleft = (x,y)
    def draw(self):
        screen.blit(self.image, self.rect.x, self.rect.y)
# Colors
bg = (20,20,20)
grid = (30,30,30)

#Functions 
def draw_grid(tile_size):
    screen.fill(bg)
    
    for x in range(tile_size, screen_w, tile_size):
        pygame.draw.line(screen, grid, (x, 0), (x, screen_h), 2)
    for y in range(tile_size, screen_h, tile_size):
        pygame.draw.line(screen, grid, (0,y), (screen_w, y), 2)
    
# ~~ Variables
create_r = pygame.image.load("Create_body.png").convert_alpha

tile_size = 30
    
#Pygame
pygame.init()
screen_w = 1120
screen_h = 880
screen = pygame.display.set_mode((screen_w, screen_h))

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    draw_grid(tile_size)
    
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    pygame.display.update()
pygame.quit()