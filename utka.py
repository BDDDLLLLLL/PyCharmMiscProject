import pygame
screen=pygame.display.set_mode((500, 664))
u=pygame.image.load("utka2.png")
b=pygame.image.load("вания.jpg")
v=pygame.image.load("ная.png")
x=200
y=190
s=-100
t=0
q=-200
p=400
l=150
n=True
m=True
r=True
o=True
z=True
while 1:
    pygame.draw.rect(screen, (0,0,0), (0,0,1000,900))
    screen.blit(b, (0, 0))
    screen.blit(v,(s,t))
    screen.blit(v, (q, p))
    #pygame.draw.rect(screen, (250,250,0), (0,0,300,300))
    #pygame.draw.circle(screen, (0,0,0),(10,100), 50,100)
    #pygame.draw.circle(screen, (0,0,0),(200,300), 50,100)
    #pygame.draw.circle(screen, (0,0,0),(200,150), 50,100)
    #pygame.draw.circle(screen, (0,250,0),(500,650), 300,500)
    #pygame.draw.circle(screen, (250,100,100),(250,350), 50,100)
    #pygame.draw.circle(screen, (250,100,100),(350,350), 50,100)
    #pygame.draw.polygon(screen, (250,100,100),[[200,370], [300,450],[400,370],[200,350]])
    if n:
        if x<300:
            x=x+1
            if x ==300:
                n=False
    else:
        if x>0:
            x-=1
            if x==0:
                n=True
    if m:
        if y<464:
            y=y+1
            if y ==464:
                m=False
    else:
        if y>0:
            y-=1
            if y==0:
                m=True
    if r:
        if s<500:
            if s >= -200:
               s+=1
        if s>=500:
            s=-150
            t+=152
        if t>=664:
            t=32

    if o:
        if q < 500:
            if q >= -300:
                q += 1
        if q >= 500:
            q = -200
            p += 102
        if p >= 664:
            p = 43
    screen.blit(u,(x,y))
    pygame.display.update()
