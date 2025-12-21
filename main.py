import numpy as np
import pygame

pygame.init()

# ~~ Variables

tile_size = 30
screen_w = 1120
screen_h = 880
screen = pygame.display.set_mode((screen_w, screen_h))

#Classes
class Body:
    def __init__(self, mass : float, radius : float, accel: float):
        self.mass = mass
        self.radius = radius
        self.accel = accel
        
class Button:
    def __init__(self, x: int, y: int, image: pygame.Surface, Scale: float):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * Scale), int(height * Scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        image.set_alpha(0.75)
        
    def draw(self):
        #Click
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.image.set_alpha(255)
        else:
            self.image.set_alpha(180)
            
        screen.blit(self.image, (self.rect.x, self.rect.y))


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
    
    
#++ Variables
create_r = pygame.image.load("Create_body.png").convert_alpha()
create_g = pygame.image.load("Create_body_g.png").convert_alpha()

#Pygame
running = True
clock = pygame.time.Clock()
Create_button = Button(-2, 10, create_r, 1)


while running:
    clock.tick(60)
    draw_grid(tile_size)
    Create_button.draw()
    
    
    
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    pygame.display.update()
pygame.quit()