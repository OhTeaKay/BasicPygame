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
text_surface = test_font.render("Score", False, "Blue")


text_rectangle = text_surface.get_rect(midbottom = (475,100))
player_surface = pygame.image.load("Graphics/Rust_Crab.png").convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,461))

enemy_surface = pygame.image.load("Graphics/docker_logo.png").convert_alpha()

enemy_rectangle = enemy_surface.get_rect(midbottom = (1000,450))


while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rectangle.collidepoint(event.pos):
                #print("Collision")
                
    screen.blit(background_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    
    pygame.draw.rect(screen,"Grey",text_rectangle)
    pygame.draw.rect(screen,"Grey",text_rectangle,5)
    
    #pygame.draw.line(screen,"Gold",(0,0),pygame.mouse.get_pos(),10)
    
    screen.blit(text_surface,text_rectangle)
    screen.blit(player_surface,player_rectangle)
    
    enemy_rectangle.x -= 8
        
    if enemy_rectangle.x <= -300:
         enemy_rectangle.x = 1000
         
    #if player_rectangle.colliderect(enemy_rectangle):
    #   break
         
    screen.blit(enemy_surface,enemy_rectangle)
    
    pygame.display.update()
    clock.tick(60)