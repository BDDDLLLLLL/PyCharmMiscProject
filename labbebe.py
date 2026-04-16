import random
import pygame
screen=pygame.display.set_mode((375, 625))
pygame.font.init()
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
x2 = 200
y2 = 150
count=0
coincon=True
okcon=False

per = True
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
exit=pygame.image.load("exit.png")
coin=pygame.image.load("coin.png")
svinka=pygame.image.load("becon.png")
kol=pygame.image.load("kol.png")
zayaz=pygame.image.load("shavermasvokzala.png")
devochka=pygame.image.load('devochka.png')
malchik=pygame.image.load('malchik.png')
bgchoose=pygame.image.load('bgchoose.png')
mask=pygame.image.load('mouse.png')
win=pygame.image.load('win.png')
notwin=pygame.image.load('notwin.png')
ok=pygame.image.load('ok.png')

zayazch=pygame.image.load("shavermasvokzalach.png")
devochkach=pygame.image.load('devochkach.png')
malchikch=pygame.image.load('malchikch.png')
svinkach=pygame.image.load("beconch.png")

while 1:

    while per:
        xp = 95
        yv = 205
        xl = 375-95-50
        yn = 205+xl-xp

        screen.blit(bgchoose, (0, 0))
        screen.blit(svinkach, (xp, yv))
        screen.blit(zayazch, (xp, yn))
        screen.blit(devochkach, (xl, yv))
        screen.blit(malchikch, (xl, yn))
        pygame.display.update()
        for event in pygame.event.get():
            xb, yb = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and per:
                xb, yb = event.pos
                screen.blit(mask, (xb, yb))

                if pygame.mask.from_surface(mask).overlap(pygame.mask.from_surface(svinkach), (xp - xb, yv - yb)):
                    pizza = svinka
                    per = False
                if pygame.mask.from_surface(mask).overlap(pygame.mask.from_surface(devochkach), (xl - xb, yv - yb)):
                    pizza = devochka
                    per = False
                if pygame.mask.from_surface(mask).overlap(pygame.mask.from_surface(zayazch), (xp - xb, yn - yb)):
                    pizza = zayaz
                    per = False
                if pygame.mask.from_surface(mask).overlap(pygame.mask.from_surface(malchikch), (xl - xb, yn - yb)):
                    pizza = malchik
                    per = False



    for i in range(0,n):
        for j in range(0,m):
            if mas[i][j] == 1:
                screen.blit(doroga,(j*size,i*size))
            if mas[i][j] == 0:
                screen.blit(stena,(j*size,i*size))
    screen.blit(pygame.font.SysFont("Arial", 50).render('очки: ' + str(count), 0, (0, 0, 0), None), (10, 570))


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

    if pygame.mask.from_surface(kol).overlap(pygame.mask.from_surface(pizza), (x - xkol, y - ykol)):
        count-=1
        print(count)
        xkol=random.randint(0,375-12)
        ykol = random.randint(0, 625-25)
    if pygame.mask.from_surface(coin).overlap(pygame.mask.from_surface(pizza), (x - x2, y - y2)):
            count += 1
            print(count)

            while coincon:

                if coincon:
                    x2 = 25 * random.randint(0,14)
                    y2 = 25 * random.randint(0, 14)
                    if mas[y2 // 25][x2 // 25 ] == 1:
                        coincon = False

    coincon = True

    screen.blit(coin, (x2, y2))
    screen.blit(kol, (int(xkol), int(ykol)))


    screen.blit(pizza, (x, y))
    screen.blit(exit, (300, 600))
    if pygame.mask.from_surface(exit).overlap(pygame.mask.from_surface(pizza), (x - 300, y - 600)):
        okcon = True
        if count<2:
            if okcon:
                screen.blit(notwin, (0, 0))
                screen.blit(ok, (0, 0))
                for event in pygame.event.get():
                    xb, yb = pygame.mouse.get_pos()

                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and per:
                        xb, yb = event.pos
                        screen.blit(mask, (xb, yb))

                        if pygame.mask.from_surface(mask).overlap(pygame.mask.from_surface(ok), (xb,yb)):
                            okcon=False
                            x = 600
        else:
            screen.blit(win, (0, 0))



    pygame.display.update()