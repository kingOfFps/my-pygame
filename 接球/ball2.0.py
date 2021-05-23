# 这是我在嵩天老师的弹球源代码的基础上，用oop重写了一边
# 这这是一个动画，不能算是游戏
import pygame, sys


def RGBChannel(a):
    return 0 if a < 0 else (255 if a > 255 else int(a))

# 可采用单例模式
class Ball:
    width = 80
    height = 80
    # speed[0]是小球的横向速度，speed[1]是小球的纵向速度
    speed = [2, 2]
    # x,y表示小球的x，y坐标
    x, y = 0, 0
    # 小球图片路径
    picPath = "./pic/ball.png"
    # 小球的sufface对象(sufface是pygame的对象，通过pygame的加载图片的函数返回)
    ballSufface = None
    # 小球的rect对象(rect是pygame的对象，由sufface得到)
    ballrect = None

    def move(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        # self.ballrect = self.ballrect.move(self.position[0], self.position[1])
        self.ballrect = self.ballrect.move(self.speed)
        print("ball (x,y) = ({0},{1})".format(self.x, self.y))

    def judge(self):
        # if self.position[0] < 0 | self.position[0] + self.width > Game.width:
        if self.ballrect.left < 0 or self.ballrect.right > Game.width:
            self.speed[0] = -self.speed[0]

        if self.ballrect.top < 0 or self.ballrect.bottom > Game.height:
            self.speed[1] = -self.speed[1]



# 单例模式
class Game:
    # 记录此类的第一个对象
    instance = None
    width = 1366
    height = 768
    background_color = [255, 255, 255]
    iconPath = "./pic/icon.jpeg"
    caption = "Pygame壁球"
    screen = None
    fps = 60
    fclock = None
    """
    __init__()是在给对象属性赋值时被调用,而__new__()是在给对象分配空间时就调用了，比__new__()更早
    单例模式的实现需要重写__new__()方法
    """

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, ball):
        self.ball = ball
        pygame.init()
        pygame.display.set_icon(pygame.image.load(self.iconPath))
        # self.screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)
        self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
        pygame.display.set_caption(self.caption)
        self.ball.ballSufface = pygame.transform.scale(pygame.image.load(ball.picPath), (ball.width, ball.height))
        self.ball.ballrect = self.ball.ballSufface.get_rect()
        self.fclock = pygame.time.Clock()
        # bgcolor = pygame.Color("black") 可以通过这种方式获取颜色

    # TODO() 鼠标移动带动挡板
    def eventProcess(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 全屏幕需要按esc退出
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        # 屏幕大小改变
        elif event.type == pygame.VIDEORESIZE:
            self.width, self.height = event.size[0], event.size[1]
            self.screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)

    def run(self):
        while True:
            for event in pygame.event.get():
                self.eventProcess(event)

            self.ball.move()
            self.ball.judge()

            self.screen.fill(self.background_color)
            self.screen.blit(self.ball.ballSufface, self.ball.ballrect)
            # pygame.display.flip()是更新所有画面，效率比更新部分画面的update()低
            pygame.display.update()
            self.fclock.tick(self.fps)


def main():
    ball = Ball()
    game = Game(ball)
    game.run()


if __name__ == '__main__':
    main()
