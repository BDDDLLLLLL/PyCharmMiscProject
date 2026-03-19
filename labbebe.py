import time
import timeit
import random
import pygame
screen=pygame.display.set_mode((375, 625))


n=25 #строк
m=15 #столбцов
x=0
y=0
r1= True
x1=-1
y1=-1
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

timerrr= 2
size=25
stena=pygame.image.load("stena.png")
doroga=pygame.image.load("doroga.png")
pizza=pygame.image.load("pizza.png")
ch=pygame.image.load("chillguy.png")
my_time = pygame.time.set_timer(timerrr,5000,10)

while 1:


    for i in range(0,n):
        for j in range(0,m):
            if mas[i][j] == 1:
                screen.blit(doroga,(j*size,i*size))
            if mas[i][j] == 0:
                screen.blit(stena,(j*size,i*size))



    for event in pygame.event.get():
                    if event.type == timerrr:
                        print("timer!")
                        x1=0
                        y1=0
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            if y < 625-25:
                                if mas[y//25+1][x//25] == 1:
                                    y += 25

                        if event.key==pygame.K_UP:
                            if y > 0:
                                if mas[y//25-1][x//25] == 1:
                                    y-=25
                        if event.key==pygame.K_LEFT:
                            if x > 0:
                                if mas[y//25][x//25-1]==1:
                                    x-=25


                        if event.key==pygame.K_RIGHT:
                            if x < 375-25:
                                if mas[y//25][x//25+1] == 1:
                                    x+=25

                    else:
                        y+=0

    if x1>-10:
        x1+=1
        y1+=1
        if x1>400:
            y1=600
            x1-=1
            y1-=1
            if y1>625:
                y1=-10
                x1-=1
                y1-=1
                if y1<-10:
                    y1=200
                    y1+=1
                    x1+=1


    print(x1,y1)
    m1 = pygame.mask.from_surface(pizza)
    m2 = pygame.mask.from_surface(ch)
    of1 = (x1 - x, y1 - y)
    if m1.overlap(m2, of1):
        print("you lost")
    screen.blit(pizza, (x, y))
    screen.blit(ch,(x1,y1))
    pygame.display.update()