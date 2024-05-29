import pygame
import sys
import random
from creere.un_patrat import *
from viata.toate_patratele import *
from creere.alte_functii import*

pygame.init()
width=500
height=500
screen=pygame.display.set_mode((width,height))

nr_patrate=10
patrate=creaza(nr_patrate,width,height)

timp=0
ok=1
rect=pygame.Rect(0,0,500,500)
clock = pygame.time.Clock()
generatie=0
while True:
    #Creaza generatiile
    pygame.display.set_caption("generatia"+str(generatie))
    if generatie==0:
         patrate=creaza(nr_patrate,width,height)
    else:
         patrate=next(nr_patrate,width,height)
         if patrate==0:
            ok=3
    #Daca nu au mai ramas specii
    while ok==3:
        font = pygame.font.Font(None, 30)
        pygame.draw.rect(screen, (225,225,225), (0, 0, width, height))
        text_surface = font.render("in generatia "+str(generatie)+" nu a mai rezistat", True, (0,0,0))
        text_rect = text_surface.get_rect(center=pygame.Rect(0, 0, width, height).center)
        screen.blit(text_surface, text_rect)
        pygame.display.flip() 
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
    #Se misca speciile pe ecran  
    timp=800
    if(ok==1):
        while timp:
            screen.fill((0, 0, 0))
            for i in range(0,nr_patrate):
                font = pygame.font.Font(None, 120)
                pygame.draw.rect(screen, patrate[i].color, (patrate[i].x, patrate[i].y, patrate[i].size, patrate[i].size))
                text_surface = font.render(str(i), True, (0,0,0))
                text_rect = text_surface.get_rect(center=pygame.Rect(patrate[i].x,patrate[i].y,patrate[i].size,patrate[i].size).center)
                screen.blit(text_surface, text_rect)

            LUME(patrate,nr_patrate,width,height)

            timp-=1
            pygame.display.flip() 
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            ok=0


    #Se salveaza speciile ramase in viata
    with open("biblioteca.txt","w") as fisier:
        i=0
        while i<nr_patrate:
            if patrate[i].x>width/2:
                fisier.write(str(patrate[i].muve_impuls))
                fisier.write("\n")
            i+=1
    #Ecranul de trecere la urmatoarea generatie
    while ok==0:
        screen.fill((225,225,225))
        pygame.draw.rect(screen,(225,225,225,50),rect)
        pygame.display.flip() 
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                if rect.collidepoint(mouse_pos):
                    ok=1
                    generatie+=1

