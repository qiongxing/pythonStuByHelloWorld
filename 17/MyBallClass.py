import pygame

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location):
        pygame.sprite.Sprite.__init__(self)
        self.image =pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top=location


size =width,height=640,480
screen =pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "./images/huaji.png"
balls = []
for row in range(3):
    for column in range(3):
        location =[column *180+10,row*180 +10]
        ball =MyBallClass(img_file,location)
        balls.append(ball)

for ball in balls:
    screen.blit(ball.image,ball.rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()