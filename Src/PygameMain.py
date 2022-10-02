from cgi import test
from tkinter import BOTTOM
import pygame
from sys import exit

# DODAŁEŚ stronę tytułu i jej elementy !!

def display_score():
    current_time =  int(pygame.time.get_ticks() / 3000 - start_time / 3000)
    score_surface = test_font.render(f'Score: {current_time}',False, "#f74c00")
    score_recetangle = score_surface.get_rect(center = (475,50))
    screen.blit(score_surface,score_recetangle)

pygame.init()
screen = pygame.display.set_mode((950,536))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Fonts/MinecraftTen-VGORe.ttf", 50)
game_active = True
start_time = 0

background_surface = pygame.image.load("Graphics/Ocean_fish_background.png").convert()
ground_surface = pygame.image.load("Graphics/Ground_Surface.png").convert()

title_surface = test_font.render("Crab Game", False, "#00b1e3")
title_rectangle = title_surface.get_rect(center = (475,100))

player_surface = pygame.image.load("Graphics/Rust_Crab.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,424))
player_rectangle.update(100,0,125,50)

player_icon = pygame.image.load("Graphics/crab_static.png").convert_alpha()
player_icon = pygame.transform.scale(player_icon,(340,200))
player_icon_rectangle = player_icon.get_rect(center = (460,280))
  
enemy_surface = pygame.image.load("Graphics/docker_logo.png").convert_alpha()
enemy_rectangle = enemy_surface.get_rect(midbottom = (1000,450))

gravity_value = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >= 405:
                gravity_value = -20
            if game_active == False and event.key == pygame.K_BACKSPACE:
                enemy_rectangle.left = 1000
                game_active = True
                start_time = pygame.time.get_ticks()
                
    if game_active:
        screen.blit(background_surface,(0,0))
        screen.blit(ground_surface,(0,450))
        
            #pygame.draw.line(screen,"Gold",(0,0),pygame.mouse.get_pos(),10)

        screen.blit(player_surface,player_rectangle)
        
        gravity_value += 1
        player_rectangle.y += gravity_value;
        
        if player_rectangle.bottom >= 424:
            player_rectangle.bottom = 424  
            
        enemy_rectangle.x -= 8
            
        if enemy_rectangle.right <= -5:
            enemy_rectangle.left = 1000
            
        if enemy_rectangle.colliderect(player_rectangle):
            game_active = False
        
        display_score()
        screen.blit(enemy_surface,enemy_rectangle)
    else:
        screen.fill("#02638a")
        screen.blit(player_icon,player_icon_rectangle)
        screen.blit(title_surface,title_rectangle)
        display_score()

    pygame.display.update()
    clock.tick(60)