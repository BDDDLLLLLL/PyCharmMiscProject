import time
import timeit

import pygame
screen=pygame.display.set_mode((500, 664))
u=pygame.image.load("utka4.png")
c=pygame.image.load("вания.jpg")
v=pygame.image.load("ная1.png")
l=pygame.image.load("utka3.png")
vc=pygame.image.load("Бqqия.jpg")
a=100
b=100
q=-100
d=0
g=-1000
t=-1000
x1=0
y1=0
x2=-1000
y2=-1000
wer= True
r= True
r1= True
q1=-200
d1=400
while 1:
    if wer== False:
        time.sleep(2)
        pygame.quit()

    if r:
        if q<500:
            if q >= -200:
               q+=1
        if q>=500:
            q=-150
            d+=152
        if d>=664:
            d=32

    if r1:
        if q1 < 500:
            if q1 >= -300:
                q1 += 1
        if q1 >= 500:
            q1 = -200
            d1 += 102
        if d1 >= 664:
            d1 = 43


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if pygame.K_LEFT == event.key:
                a-=50

                if a<-200:
                    a=520


            if pygame.K_RIGHT == event.key:
                a+=50

                if a>520:
                    a=-200


            if pygame.K_UP == event.key:
                b-=50

                if b<-200:
                    b=694


            if pygame.K_DOWN == event.key:
                b+=50

                if b > 694:
                    b=-200
                    q=q+100
                    d=d+100


    m1=pygame.mask.from_surface(u)
    m2 = pygame.mask.from_surface(v)
    of=(q-a,d-b)
    if m1.overlap(m2,of):
        a=-1000
        b=-1000
        q=-1000
        d=-1000
        g=100
        t=100
        x1=-1000
        y1=-1000
        x2=0
        y2=0
        wer= False


    screen.blit(c, (x1, y1))
    screen.blit(vc,(x2,y2))
    screen.blit(v,(q,d))
    screen.blit(v, (q1, d1))
    screen.blit(u,(a,b))
    screen.blit(l,(g,t))

    pygame.display.update()

    '''if a>500:
        a=0
        b=0
        if a < 0:
            a=0
            b=0
    if b>664:
        b=0
        a=0
        if b<0:
            b=0
            a=0
    pygame.draw.rect(screen, (0,0,0), (0,0,1000,900))'''