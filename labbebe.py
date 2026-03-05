import time
import timeit
import random
import pygame
screen=pygame.display.set_mode((375, 625))
n=25 #строк
m=15 #столбцов
x=0
y=0
mas = [
    [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,1,1,1,0,1,1,1,1,1,1],
    [0,1,1,1,1,1,0,1,0,1,0,0,0,0,1],
    [0,0,0,0,0,1,0,1,0,1,0,1,1,1,1],
    [1,1,1,0,0,1,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,0,1,0,0,0,1,0,1,0,0,1],
    [1,0,1,0,0,1,0,1,1,1,0,0,0,0,0],
    [1,1,1,0,1,1,0,1,0,1,0,1,1,1,0],
    [0,0,1,0,0,1,1,1,0,1,0,1,0,1,0],
    [0,0,1,0,0,0,0,0,0,1,0,1,0,1,1],
    [0,1,1,1,1,1,1,1,1,1,0,1,0,1,0],
    [0,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
    [0,1,0,1,1,1,1,1,1,1,1,1,0,1,0],
    [0,1,1,1,0,0,0,0,0,0,0,0,0,1,0],
    [1,1,0,0,0,0,0,1,0,0,0,0,0,1,0],
    [0,0,0,1,0,1,1,0,0,0,0,0,0,1,0],
    [1,1,1,1,0,1,0,0,1,1,1,1,1,1,0],
    [1,0,0,0,1,1,1,0,1,0,0,0,0,0,0],
    [0,0,1,0,1,0,1,0,1,0,1,1,1,1,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,1,1,1],
    [1,0,1,0,1,1,1,1,0,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,1,0,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,0,1,0,1,1,1],
    [1,0,1,1,1,1,1,1,1,1,1,0,1,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,0,1,1,1,0],



]
size=25
stena=pygame.image.load("stena.png")
doroga=pygame.image.load("doroga.png")
utka=pygame.image.load("utkalab.png")
while 1:


    for i in range(0,n):
        for j in range(0,m):
            if mas[i][j] == 1:
                screen.blit(doroga,(j*size,i*size))
            if mas[i][j] == 0:
                screen.blit(stena,(j*size,i*size))

    for i in range(0,n):
        for j in range(0,m):
            if mas[i][j]==1:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            y += 25
                            if y>625:
                                y=600
                        if event.key==pygame.K_UP:
                            y-=25
                            if y<0:
                                y=0
                        if event.key==pygame.K_LEFT:
                            x-=25
                            if x<0:
                                x=0

                        if event.key==pygame.K_RIGHT:
                            x+=25
                            if x > 375:
                                x=350
            else:
                y+=0
    screen.blit(utka, (x, y))
    pygame.display.update()