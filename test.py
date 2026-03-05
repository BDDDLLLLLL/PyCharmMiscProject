import pygame


class person:
    x=0
    y=0
    img=""
    def __init__(self,dx,y,way):
        self.x = dx
        self.y =y
        self.img = pygame.image.load(way)
        self.live =9
        


duck = person(50,50,"C:/Users/dolgushinabv.29/PycharmProjects/PyCharmMiscProject/utka1.png")
cat = person(100,100,"")

screen = pygame.display.set_mode((500,500))

while 1:

    screen.blit(duck.img, (duck.x,duck.y))
    pygame.display.update()

        
    
    
