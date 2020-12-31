import pygame

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

points=[[10,20],[30,40],[20,50]]
pygame.draw.polygon(screen,[0,0,0],points,1)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()