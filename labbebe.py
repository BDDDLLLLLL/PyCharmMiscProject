import random
import pygame
screen=pygame.display.set_mode((375, 625))

#kol 12x25
n=25 #строк
m=15 #столбцов
x=0
y=0
fx=True
fy=True
x1=-1
y1=-1
xkol=187
ykol=312
x2=0
y2=0
count=0
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
svinka=pygame.image.load("becon.png")
kol=pygame.image.load("shavermasvokzala.png")
uchebnick=pygame.image.load("shaslik.png")

while 1:

    for i in range(0,n):
        for j in range(0,m):
            if mas[i][j] == 1:
                screen.blit(doroga,(j*size,i*size))
            if mas[i][j] == 0:
                screen.blit(stena,(j*size,i*size))



    for event in pygame.event.get():

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

    if fx:
        xkol=xkol+0.07
        if xkol>=375-12:
            fx=False
    else:
        xkol=xkol-0.07
        if xkol<=0:
            fx=True

    if fy:
        ykol=ykol+0.07
        if ykol>=625-25:
            fy=False
    else:
        ykol=ykol-0.07
        if ykol<=0:
            fy=True

    if pygame.mask.from_surface(kol).overlap(pygame.mask.from_surface(svinka), (x - xkol, y - ykol)):
        count-=1
        print(count)
        xkol=random.randint(0,375-12)
        ykol = random.randint(0, 625-25)


   # m1 = pygame.mask.from_surface(pizza)
  #  m2 = pygame.mask.from_surface()
   # of1 = (x1 - x, y1 - y)
   # if m1.overlap(m2, of1):
   #     print("you lost")
    screen.blit(svinka, (x, y))
    screen.blit(kol, (int(xkol), int(ykol)))
    screen.blit(uchebnick, (x2,y2))
    pygame.display.update()