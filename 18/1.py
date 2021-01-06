# 动手1，动手2都在当前项目
import pygame,sys,random
from pygame.locals import *

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed

    def move(self):
        global score,score_font,score_surf,lives
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right >screen.get_width():
            self.speed[0] = -self.speed[0]

        if self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
            score += 1
            score_surf =score_font.render(str(score),1,(0,0,0))
        
        # if self.rect.bottom >=screen.get_rect().bottom :
        #     lives -= 1
        #     pygame.time.delay(2000)
        #     myBall.rect.topleft =[50,50]

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self,location=[0,0]):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,20])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location

pygame.init()
screen =pygame.display.set_mode([640,480])
clock = pygame.time.Clock()
ball_speed = [5,2]
myBall = MyBallClass('../images/wackyball.bmp',ball_speed,[50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle =MyPaddleClass([270,400])
score = 0
lives = 2
done = False
score_font = pygame.font.Font(None,50)
score_surf = score_font.render(str(score),1,(0,0,0))
score_pos =[10,10]

running = True
while running:
    clock.tick(120)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx =event.pos[0]

    if pygame.sprite.spritecollide(paddle,ballGroup,False):
        if myBall.speed[1] >0:
            #生成随机速率
            myBall.speed= [random.randint(1,5),random.randint(1,5)]
            myBall.speed[1] = -myBall.speed[1]

    myBall.move()

    if not done:
        screen.blit(myBall.image,myBall.rect)
        screen.blit(paddle.image,paddle.rect)
        screen.blit(score_surf,score_pos)
        for i in range(lives):
            width = screen.get_width()
            screen.blit(myBall.image,[width - 40 * i,20])
        pygame.display.flip()

    if myBall.rect.top >=screen.get_rect().bottom:
        lives -= 1
        if lives == 0:
            final_txt1 = "游戏结束"
            final_txt2 = "分数"+str(score)
            ft1_font = pygame.font.Font(None,70)
            ft1_surf =ft1_font.render(final_txt1,1,(0,0,0))
            ft2_font = pygame.font.Font(None,50)
            ft2_surf =ft2_font.render(final_txt2,1,(0,0,0))
            screen.blit(ft1_surf,[screen.get_width()/2 - ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf,[screen.get_width()/2 - ft2_surf.get_width()/2,200])
            pygame.display.flip()
            done = True
        else :
            pygame.time.delay(2000)
            myBall.rect.topleft =[50,50]
            myBall.speed = ball_speed
 
    

pygame.quit()
