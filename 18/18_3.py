import pygame,sys
pygame.init()
screen =pygame.display.set_mode([640,480])
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])

clock= pygame.time.Clock()
class Ball(pygame.sprite.Sprite):
    def __init__(self,image_file,speed,location):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(image_file)
        self.rect=self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed =speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or self.rect.right >= screen.get_rect().right:
            self.speed[0] =-self.speed[0]
        newpos =self.rect.move(self.speed)
        self.rect =newpos

my_ball =Ball('../images/beach_ball.png',[10,0],[20,20])
pygame.time.set_timer(pygame.USEREVENT,1000)
direction = 1
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 定时器任务
        elif event.type ==pygame.USEREVENT:
            # 更改中心y坐标
            my_ball.rect.centery =my_ball.rect.centery + (30*direction)
            if my_ball.rect.top <= 0 or \
                my_ball.rect.bottom >= screen.get_rect().bottom:
                direction =- direction
    
    clock.tick(60)
    screen.blit(background,(0,0))
    my_ball.move()
    screen.blit(my_ball.image,my_ball.rect)
    pygame.display.flip()

pygame.quit()