import pygame,sys
pygame.init()
screen =pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball =pygame.image.load("beach_ball.png")
x=50
y=50
screen.blit(my_ball,[x,y])
pygame.display.flip()

for i in range(1,100):
    pygame.time.delay(20)
    # 覆盖之前的图像
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x+=5
    screen.blit(my_ball,[x,y])
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()