import numpy as np
import pygame
import pygame_gui as ui
from pygame_gui.elements import UIButton, UITextEntryLine, UILabel

pygame.init()

# ~~ Variables
PIX_PER_UNIT = 0.1
tile_size = 30
screen_w = 1200
screen_h = 880 
GRAVITATIONAL_CONSTANT = 6.7

screen = pygame.display.set_mode((screen_w, screen_h))
manager = ui.UIManager((screen_w, screen_h))

circle_texture = pygame.image.load("texture.png").convert_alpha()
# Formulas


# UI
UILabel(relative_rect=pygame.Rect((10, 10), (100, 30)), text="Mass:", manager=manager)
mass_input = UITextEntryLine(relative_rect=pygame.Rect((120, 10), (100, 30)), manager=manager)
mass_input.set_allowed_characters('numbers')

UILabel(relative_rect=pygame.Rect((10, 40), (100, 30)), text="Radius:", manager=manager)
radius_input = UITextEntryLine(relative_rect=pygame.Rect((120, 40), (100, 30)), manager=manager)
radius_input.set_allowed_characters("numbers")

UILabel(relative_rect=pygame.Rect((10, 80), (100, 30)), text="Velocity X:", manager=manager)
vel_x_input = UITextEntryLine(relative_rect=pygame.Rect((120, 80), (100, 30)), manager=manager)
vel_x_input.set_allowed_characters("numbers")

UILabel(relative_rect=pygame.Rect((10, 110), (100, 30)), text="Velocity Y:", manager=manager)
vel_y_input = UITextEntryLine(relative_rect=pygame.Rect((120, 110), (100, 30)), manager=manager)
vel_y_input.set_allowed_characters("numbers")




#Classes
class Body:
    def __init__(self, mass : float, radius : float, vel: float, pos: np.array, accel: np.array):
        self.mass = mass
        self.radius = radius
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, float)  
        self.accel = np.zeros(2, float)
        
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (80,80,80),
             self.pos.astype(int),
            int(self.radius)
        )
        
    def update(self, dt):
        self.vel = self.vel + self.accel
        self.pos = self.pos + dt
        
class Sattelite:
    def __init__(self, accel):
        self.accel = accel


# Buttons
create_button = UIButton(
    relative_rect=pygame.Rect((10, 160), (210, 40)),
    text='Create Body',
    manager=manager
)

create_sattelite = UIButton(
    relative_rect=pygame.Rect((10,200), (210, 40)),
    text="Create sattelite",
    manager=manager
)


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
    
    
    

# SIM state
bodies = []
running = True
clock = pygame.time.Clock()
placing = False
#Temp States
t_mass = None
t_radius = None
t_accel = None
t_x_vel = None
t_y_vel = None

while running:
    
    time_delta = clock.tick(60)/1000
    draw_grid(tile_size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        manager.process_events(event)
        
        if placing:
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                new_body = Body(t_mass,
                                t_radius,
                                t_vel,
                                pygame.mouse.get_pos(),
                                t_accel
                                )
                bodies.append(new_body)
                
                placing = False
        
        
        if event.type == ui.UI_BUTTON_PRESSED:
            if event.ui_element == create_button:
                try:
                    t_mass = float(mass_input.get_text())
                    t_radius = float(int(radius_input.get_text()) * PIX_PER_UNIT)
                    t_vel = np.array([float(vel_x_input.get_text()), float(vel_y_input.get_text())])
                    
                except ValueError:
                    print("Fields need numbers")
                    continue
                placing = True
                
    if placing:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(
            screen,
            (70,70,70),
            mouse_pos,
            int(t_radius),
            5
        )
        
        # F = G((m_1 + m_2) / r^2) 
    for m_body in bodies:
        for sub_body in bodies:
            if m_body == sub_body:
                continue
            diff = m_body.pos - sub_body.pos
            dist = np.linalg.norm(diff)
            
            
            total_mass  =m_body.mass + sub_body.mass
            
            force_magn = GRAVITATIONAL_CONSTANT * (total_mass / (dist * dist))
            force_vect = force_magn * (diff / dist)
            
            

    for body in bodies:
        body.draw(screen)
                
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()
    
    
    
pygame.quit()