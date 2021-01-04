import pygame
from random import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top=location
        self.speed =speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left <0 or self.rect.right >width:
            self.speed[0] = -self.speed[0]

        if self.rect.top <0 or self.rect.bottom >height:
            self.speed[1] = -self.speed[1]

def animate(group):
    screen.fill([255,255,255])
    for ball in group:
          ball.move()
    for ball in group:
        # 删除精灵
        group.remove(ball)
        # 检测是否碰撞
        if pygame.sprite.spritecollide(ball,group,False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        # 添加回原组中
        group.add(ball)
        screen.blit(ball.image,ball.rect)
    pygame.display.flip()
    pygame.time.delay(50)


size =width,height=640,480
screen =pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "./images/huaji.png"
group = pygame.sprite.Group()
for row in range(2):
    for column in range(2):
        location =[column *180+10,row*180 +10]
        speed = [choice([-5,5]),choice([-5,5])]
        ball =MyBallClass(img_file,location,speed)
        group.add(ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animate(group)
  
pygame.quit()