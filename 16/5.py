# 16-6
import pygame,sys,random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    width =random.randint(0,250);height =random.randint(0,100)
    top =random.randint(0,400);left =random.randint(0,500)
    color_name =random.choice(THECOLORS.keys())
    color = THECOLORS[color_name]
    line_width = random.randint(1,3)
    pygame.draw.rect(screen,color,[left,top,width,height],line_width)
    pygame.display.flip()
    pygame.time.delay(30)

running = True
while running:
    # pygame.display.flip()
    # pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

#16-9
# import pygame, sys
# pygame.init()
# dots = [[221, 432], [225, 331], [133, 342], [141, 310],
# [51, 230], [74, 217], [58, 153], [114, 164],
# [123, 135], [176, 190], [159, 77], [193, 93],
# [230, 28], [267, 93], [301, 77], [284, 190],
# [327, 135], [336, 164], [402, 153], [386, 217],
# [409, 230], [319, 310], [327, 342], [233, 331],
# [237, 432]]

# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
# pygame.draw.lines(screen,[0,0,0],True,dots,2)
# pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()