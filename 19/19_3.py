import pygame,sys

pygame.init()
pygame.mixer.init()
screen =pygame.display.set_mode([640,480])
pygame.time.delay(1000)

pygame.mixer.music.load("../assets/sounds/bg_music.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play()

splat = pygame.mixer.Sound("splat.wav")
splat.set_volume(0.50)
splat.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()