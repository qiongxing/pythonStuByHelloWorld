# import random
# secret = random.randint(1,99)
# guess=0
# tries = 0
# print "神秘数字"
# print "在1-99之间,6次机会"
# while guess != secret and tries < 6:
#     guess = input("请输入数字")
#     if guess < secret:
#         print "太小了"
#     elif guess >secret :
#         print "太大了"
#     tries += 1
# if  guess == secret:
#         print "猜对了",secret
# else:
#         print "没有机会了"
#         print "神秘数字为",secret

import pygame,sys,random

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode([100,100])
pygame.time.delay(1000)
secret = random.randint(1,99)
guess=0
tries = 0
ahoy=pygame.mixer.Sound("../assets/sounds/Ahoy.wav")
ahoy.set_volume(0.5)
avastGotIt=pygame.mixer.Sound("../assets/sounds/AvastGotIt.wav")
avastGotIt.set_volume(0.5)
nomore=pygame.mixer.Sound("../assets/sounds/NoMore.wav")
nomore.set_volume(0.5)
tooHigh=pygame.mixer.Sound("../assets/sounds/TooHigh.wav")
tooHigh.set_volume(0.5)
tooLow=pygame.mixer.Sound("../assets/sounds/TooLow.wav")
tooLow.set_volume(0.5)
whatYerGuess=pygame.mixer.Sound("../assets/sounds/WhatYerGuess.wav")
whatYerGuess.set_volume(0.5)

print "神秘数字"
print "在1-99之间,6次机会"
ahoy.play()
pygame.time.delay(8000)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    while guess != secret and tries < 6:
        whatYerGuess.play()
        guess = input("请输入数字")
        if guess < secret:
            print "太小了"
            tooLow.play()
            pygame.time.delay(2200)
        elif guess >secret :
            tooHigh.play()
            print "太大了"
            pygame.time.delay(1800)
        tries += 1
    if  guess == secret:
        print "猜对了",secret
        avastGotIt.play()
        pygame.time.delay(3200)
        running=False
    else:
        print "没有机会了"
        print "神秘数字为",secret
        nomore.play()
        running = False

pygame.quit()
