from cgi import test
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((950,536))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Fonts/28_Days_Later.ttf", 50)

background_surface = pygame.image.load("Graphics/Ocean_fish_background.png")
ground_surface = pygame.image.load("Graphics/Ground_Surface.png")
text_surface = test_font.render("My game", False, "Blue")

whale_surface = pygame.image.load("Graphics/docker_logo.png")
whale_x_pos = 1000


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(background_surface,(0,0))
    screen.blit(ground_surface,(0,450))
    screen.blit(text_surface,(400,50))
    whale_x_pos -= 7
        
    if whale_x_pos <= -300:
         whale_x_pos = 1000

    screen.blit(whale_surface,(whale_x_pos,250))
    
    pygame.display.update()
    clock.tick(60)