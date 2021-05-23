# Unit PYG05: Pygame Wall Ball Game Version 9
# 这是嵩天老师的弹球源代码
import pygame, sys

pygame.init()
icon = pygame.image.load("pic/icon.jpeg")
pygame.display.set_icon(icon)
size = width, height = 600, 400
speed = [1,1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.set_caption("Pygame壁球")
ball = pygame.image.load("pic/ball.png")
ball = pygame.transform.scale(ball, (100, 100))
ballrect = ball.get_rect()

fps = 300
fclock = pygame.time.Clock()
still = False
bgcolor = pygame.Color("black")

def RGBChannel(a):
    return 0 if a<0 else (255 if a>255 else int(a))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1)* int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1]) - 1) * int(speed[1] / abs(speed[1]))
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0] - ballrect.left, event.pos[1] - ballrect.top)
    if pygame.display.get_active() and not still:
        ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0  or ballrect.right >width:
        speed[0] = - speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = - speed[0]
    if ballrect.top < 0  or ballrect.bottom > height:
        speed[1] = - speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = - speed[1]

    bgcolor.r = RGBChannel(ballrect.left*255/width)
    bgcolor.g = RGBChannel(ballrect.top*255/height)
    bgcolor.b = RGBChannel(min(speed[0],speed[1])*255/max(speed[0],speed[1],1))

    screen.fill(bgcolor)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)