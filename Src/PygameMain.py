from cgi import test
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((950,536))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Fonts/MinecraftTen-VGORe.ttf", 50)

background_surface = pygame.image.load("Graphics/Ocean_fish_background.png").convert()
ground_surface = pygame.image.load("Graphics/Ground_Surface.png").convert()
text_surface = test_font.render("Score:", False, "#007697")


text_rectangle = text_surface.get_rect(midbottom = (475,100))
player_surface = pygame.image.load("Graphics/Rust_Crab.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,461))
player_rectangle.update(100,0,40,30)
   
enemy_surface = pygame.image.load("Graphics/docker_logo.png").convert_alpha()

enemy_rectangle = enemy_surface.get_rect(midbottom = (1000,450))
gravity_value = 0

while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gravity_value = -20
                
    screen.blit(background_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    
    pygame.draw.rect(screen,"#005484",text_rectangle)
    pygame.draw.rect(screen,"#005484",text_rectangle,15)
    
    #pygame.draw.line(screen,"Gold",(0,0),pygame.mouse.get_pos(),10)
    
    screen.blit(text_surface,text_rectangle)
    
    
    screen.blit(player_surface,player_rectangle)
    gravity_value += 1
    player_rectangle.y += gravity_value;
    
    if player_rectangle.bottom >= 405:
        player_rectangle.bottom = 405  
        gravity_value = 0;
    
    enemy_rectangle.x -= 8
        
    if enemy_rectangle.x <= -300:
         enemy_rectangle.x = 1000
         
    if player_rectangle.colliderect(enemy_rectangle):
       pygame.time.wait(5000)
         
    screen.blit(enemy_surface,enemy_rectangle)
    
    
    pygame.display.update()
    clock.tick(60)