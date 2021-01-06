import pygame,sys
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([640,480])
pygame.time.delay(1000)

splat =pygame.mixer.Sound("../assets/sounds/splat.wav")
splat.play()

running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()