# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:31:29 2022

@author: Gabrielle
"""

import pygame, sys, random
from pygame.math import Vector2

#--- Snake----
class SNAKE:        
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        #self.tail = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        
        #---head
        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        
		#---tail
        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
        
        #---body
        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()
        
        #---curving body
        self.body_tr = pygame.image.load('Graphics/body_topright.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_topleft.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_bottomright.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bottomleft.png').convert_alpha()
        
        #--- sound
        self.crunch_sound = pygame.mixer.Sound('Graphics/Sound_crunch.wav')
        
    def draw_snake(self):
        #for block in self.body:
            #-----create a rect
            #x_snake = int(block.x * cell_size)
            #y_snake = int(block.y * cell_size)
            #block_rect = pygame.Rect(x_snake, y_snake, cell_size, cell_size)
            #---draw a rectangle
            #pygame.draw.rect(screen, (183, 111, 122), block_rect)
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            #---1. We still need a rect for the positioning
            x_snake = int(block.x * cell_size)
            y_snake = int(block.y * cell_size)
            block_rect = pygame.Rect(x_snake, y_snake, cell_size, cell_size)
            
            #---2. what direction is the face heading
            if index == 0:
                screen.blit(self.head, block_rect)
                
            elif index == len(self.body)-1:
                screen.blit(self.tail, block_rect)
                
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                if previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y ==-1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                        
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x ==  -1:
                        screen.blit(self.body_bl, block_rect)
                        
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y ==-1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                        
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x ==  1:
                        screen.blit(self.body_br, block_rect)
            #else:
                #pygame.draw.rect(screen, (152,255,152), block_rect)
    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down  

    
    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] #0 -> n
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] #0 -> n-1
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
        
    def add_block(self):
        self.new_block = True
        
    def play_crunch_sound(self):
        self.crunch_sound.play()
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        
            
#--- Fruit-----
class FRUIT:        
    #create an x and y position
    #draw a square
    def __init__(self):
        self.randomize()
        
    def draw_fruit(self):
        #draw a rectangle
        #fruit_rect = pygame.Rect(x,y,w,h)
        x_fruit = int(self.pos.x * cell_size)
        y_fruit = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(x_fruit,y_fruit,cell_size, cell_size)
        #pygame.draw.rect(screen, (222,22,41), fruit_rect)
        screen.blit(apple, fruit_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)
        
# ----Main -----
class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.draw_grass() #draw grass
        self.fruit.draw_fruit() #draw fruit
        self.snake.draw_snake() #draw snake
        self.draw_score()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            #print("snack")
            #reposition fruit
            self.fruit.randomize()
            #add another block to the snake
            self.snake.add_block()
            #add sound to eating apple
            self.snake.play_crunch_sound()
            
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            
    def check_fail(self):
        #check if snake is outside of screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
            
        #check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
        
    def game_over(self):
        #pygame.quit()
        #sys.exit()
        self.snake.reset()
        
        
    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 ==0: 
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size,row * cell_size,cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
    
    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top,apple_rect.width + score_rect.width+ 6,apple_rect.height)
        
        pygame.draw.rect(screen,(152,255,152), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen,(56, 74, 12), bg_rect, 2)
#-- initializing-------
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Graphics/VT323-Regular.ttf', 25)

#--- Color Palette -----
White = (255, 255, 255)
Pink = (254, 200, 216) #pastel peach color: https://www.schemecolor.com/pastel-color-tones.php
Blue = (0,0,250)
Mint_green = (152,255,152)
Coral = (255, 64, 64)
Apple_Red = (222,22,41)
Shit_green =(126, 166, 114)
Lilac = (244, 218, 250)

#---Make Objects----
#fruit = FRUIT()
#snake = SNAKE()

#--- Timer -----
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #this event will be triggered every 150 milliseconds

#--- state our main class -----
main_game = MAIN()

#----Event Loop-------
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == SCREEN_UPDATE:
           # snake.move_snake()
           main_game.update()
           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                    
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
                    
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                    
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            
    #draw_window()
    screen.fill((Shit_green))
    
    #draw fruit
    #fruit.draw_fruit()
    
    #draw snake
    #snake.draw_snake()
    
    #draw elements in main game
    main_game.draw_elements()
    #draw all our elements
    pygame.display.update()
    clock.tick(60) #game will never go faster than 60 fps, standarddized 
    