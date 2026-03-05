import time
import timeit
import random
import pygame
pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode((500, 664))
u=pygame.image.load("utka4.png")
c=pygame.image.load("вания.jpg")
v=pygame.image.load("ная1.png")
v1=pygame.image.load("ная11.png")
v2=pygame.image.load("ная11.png")
font = pygame.font.SysFont("Arial", 32)
score = 0
a=100
b=100
q=100
d=0
g=-1000
t=-1000
x1=0
y1=0
r= True
r1= True
r2 = True
r3 = True
q1=300
d1=400
q2=200
d2=200
q3=150
d3=450
while 1:

    if r:
        d += 5
        if d >= 664:
            d = -200
            q = random.randint(0,450)


    if r2:
        d2 += 5
        if d2 >= 664:
            d2 = -200
            q2 = random.randint(0,450)

    if r1:
        d1 += 5
        if d1 >= 664:
            d1 = -200
            q1= random.randint(0,450)

    if r3:
        d3 += 5
        if d3 >= 664:
            d3 = -200
            q3= random.randint(0,450)



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if pygame.K_LEFT == event.key:
                a-=50

                if a<-200:
                    a=520


            if pygame.K_RIGHT == event.key:
                a+=50

                if a>520:
                    a=-200

    m1=pygame.mask.from_surface(u)
    m2 = pygame.mask.from_surface(v)
    m3=pygame.mask.from_surface(v)
    m4=pygame.mask.from_surface(v1)
    of1=(q-a,d-464)
    of2=(q1-a,d1-464)
    of3=(q2-a,d2-464)
    of4=(q3-a,d3-464)
    if m1.overlap(m2, of1):
        d=-300
        q= random.randint(0,450)
        score +=1

    if m1.overlap(m2, of2):
        d1=-300
        q1= random.randint(0,450)
        score +=1

    if m1.overlap(m2, of3):
        d2=-300
        q2= random.randint(0,450)
        score -=1

    if m1.overlap(m2, of4):
        d3=-300
        q3= random.randint(0,450)
        score -=1


    score_text = font.render(f"Score: {score}", True, (255, 255, 255))




    screen.blit(c, (x1, y1))
    screen.blit(v,(q,d))
    screen.blit(v, (q1, d1))
    screen.blit(v1, (q2, d2))
    screen.blit(v2, (q3, d3))
    screen.blit(u,(a,464))
    screen.blit(score_text, (20, 20))
    pygame.display.update()
    clock.tick(60)

'''mas =['q','w','e','r','t','y']
len(mas) 
 -6-5-4-3-2-1 0 1 2 3 4 5
  q w e r t y q w e r t y

mas[i]

mas=[
    [0],
    [],
    
]
if mas[i,j]==1:'''
