# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:29:16 2022

@author: Gabrielle
"""

import pygame, sys

#-- initializing-------
pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

#------Surfaces--------
test_surface = pygame.Surface((100, 200))
test_surface.fill((255, 255, 255))
x_pos = 200
y_pos = 250

#---- Rectangles ------
#test_rect = pygame.Rect(100, 200, 100, 100)
test_rect = test_surface.get_rect(topright = (x_pos, y_pos))

#--- Colors -----
White = (255, 255, 255)
Pink = (254, 200, 216) #pastel peach color: https://www.schemecolor.com/pastel-color-tones.php
Blue = (0,0,250)
Mint_green = (152,255,152)
Coral = (255, 64, 64)

#def draw_window():
    #filling screen with color. pass a tuple with 1 for red, 1 green and 1 fo rblue
    # I liek this: #b3bad4, and this (254, 200, 216) pastel pink
    
    #pygame.display.update() #hav eto call to update our display

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #draw_window()
    screen.fill((Mint_green))
    
    #draw rectangle
    #pygame.draw.rect(screen, pygame.Color('black'), test_rect)
    #test_rect.right += 1
    
    #display surface
    #x_pos +=1
    #y_pos += 1 
    #screen.blit(test_surface,(x_pos, y_pos))
    screen.blit(test_surface,test_rect)
    
    #draw all our elements
    pygame.display.update()
    clock.tick(60) #game will never go faster than 60 fps, standarddized 
    
    






















































