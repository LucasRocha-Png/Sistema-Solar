"""
Created by: Lucas Rocha

At: 25/11/2022 - 13:00
"""

import pygame
  
pygame.init()

screen = pygame.display.set_mode((300, 300)) # x - y
  
pygame.display.set_caption('Lucas Rocha')
 
background_colour = (0, 0, 0) #RGB (255, 255, 255)
  
  
clock = pygame.time.Clock()
  
running = True
while running:
    screen.fill(background_colour)
    
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
            
    
    pygame.draw.rect(screen, (255, 255, 255), [10, 10, 100, 100], 0) #Tela, cor,[pos_x, pos_y, size_x, size_y], 0 = fill | 0 > = Linewidth 
    
    pygame.display.update()        