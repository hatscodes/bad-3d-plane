import pygame

pygame.init()

#colors
white = (255,255,255)
black= (0,0,0)
#window bullshit
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("'3d'")
#misc
clock = pygame.time.Clock()
run=True

#cube corners
#corner 1
Cx1 = 10
Cy1 = 150
#corner 2 
Cx2 = 150
Cy2 = 150
#corner 3
Cx3 = 150
Cy3 = 10
#corner 4
Cx4 = 10
Cy4 = 10

while run:
    plane = [
        [Cx1,Cy1], #corner 1
        [Cx2,Cy2], #corner 2
        [Cx3,Cy3], #corner 3
        [Cx4,Cy4] #corner 4
    ]
    
    screen.fill(black)

    #load and draw objects
    pygame.draw.aalines(screen,white,True,plane,2)
    
    #viewport controls
    key = pygame.key.get_pressed()

    if key[pygame.K_s] == True:
        Cx1 += 1
        Cy1 -= 1

        Cx2 -= 1
        Cy2 -= 1

        Cx3 -= 1
        Cy3 += 1

        Cx4 += 1
        Cy4 += 1
    elif key[pygame.K_w] == True:
        Cx1 += -1
        Cy1 -= -1

        Cx2 -= -1
        Cy2 -= -1

        Cx3 -= -1
        Cy3 += -1

        Cx4 += -1
        Cy4 += -1
    elif key[pygame.K_a] == True:
        Cx1 += -1
        Cy1 -= -1

        Cx2 -= 1
        #Cy2 -= -1

        Cx3 -= 1
        #Cy3 += -1

        Cx4 += -1
        Cy4 += -1
        pass
    elif key[pygame.K_d] == True:
        Cx1 += 1
        #Cy1 -= -1

        Cx2 += 1
        Cy2 += 1

        Cx3 += 1
        Cy3 -= 1

        Cx4 += 1
        #Cy4 += -1
        pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock.tick(30)
    pygame.display.update()