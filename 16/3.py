import pygame,sys
pygame.init()
screen =pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball =pygame.image.load("./16_10+_ball/huaji.png")
x=50
y=50
x_speed =5
y_speed =8

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(5)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90],0)
    x += x_speed
    y+= y_speed
    if x>screen.get_width() - 90 or x< 0:
        x_speed =- x_speed
    if y>screen.get_height() - 90 or y< 0:
        y_speed =- y_speed
    screen.blit(my_ball,[x,y])
    pygame.display.flip()
pygame.quit()