# 这是我在嵩天老师的弹球源代码的基础上，用oop重写了一边。加入了挡板移动功能，算是个游戏了游戏
# 此游戏是一个很好的开发框架，以后用pygame写游戏可以在此基础上开发
import pygame
import sys


# 可采用单例模式
class Ball:
    width = 80
    height = 80
    # speed[0]是小球的横向速度，speed[1]是小球的纵向速度
    speed = [2, 2]
    # x,y表示小球的x，y坐标
    # x, y = 0, 0
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

    def judge(self, block,info):
        # if self.position[0] < 0 | self.position[0] + self.width > Game.width:
        if self.ballrect.left < 0 or self.ballrect.right > Game.width:
            self.speed[0] = -self.speed[0]
        if self.ballrect.top < 0 :
            self.speed[1] = -self.speed[1]

        if self.ballrect.bottom > Game.height - Block.height:
            # 小球撞上了挡板

            if block.x < self.x + self.width/2 < block.x+block.width:
                self.speed[1] = -self.speed[1]
                info.score += 1
                Game.fps += 10
            else:
                # 小球没有撞上挡板
                print("gameOver")
                return False
        return True



class Info:
    score = 0
    gameover_img = pygame.image.load("pic/gameover.png")

    # def draw_background_img(self,screen):
    #     for x in xrange(width / background_img.get_width() + 1):
    #         for y in xrange(height / background_img.get_height() + 1):
    #             screen.blit(background_img, (x * 100, y * 100))
    def draw_text(self, text, screen):
        font = pygame.font.Font("fonts/MONACO.TTF", 24)
        survivedtext = font.render(str(text), True, (0, 0, 0))
        textRect = survivedtext.get_rect()
        textRect.topleft = [10, 10]
        screen.blit(survivedtext, textRect)

# 单例模式
class Game:
    # 记录此类的第一个对象
    instance = None
    width = 1000
    height = 700
    background_color = [255, 255, 255]
    iconPath = "./pic/icon.jpeg"
    caption = "Pygame壁球"
    screen = None
    fps = 60
    fclock = None
    runing = True
    """
    __init__()是在给对象属性赋值时被调用,而__new__()是在给对象分配空间时就调用了，比__new__()更早
    单例模式的实现需要重写__new__()方法
    """

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, ball, block,info):
        self.ball = ball
        self.block = block
        self.info = info
        pygame.init()
        pygame.display.set_icon(pygame.image.load(self.iconPath))
        # self.screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)
        self.screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)
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
        elif event.type == pygame.MOUSEMOTION:
            # 鼠标移动则挡板移动
            self.block.move(event)
        # 屏幕大小改变
        elif event.type == pygame.VIDEORESIZE:
            self.width, self.height = event.size[0], event.size[1]
            self.screen = pygame.display.set_mode([self.width, self.height], pygame.RESIZABLE)

    def draw(self):
        if not self.runing:
            gameover_sufface = pygame.transform.scale(self.info.gameover_img, (self.width, self.height))
            gameover_rect = gameover_sufface.get_rect()
            # self.screen.blit(self.info.gameover_img, (0,0))
            self.screen.blit(gameover_sufface, gameover_rect)
            return

        self.screen.fill(self.background_color)
        # 画弹球
        self.screen.blit(self.ball.ballSufface, self.ball.ballrect)
        # 画挡板
        # pygame.draw.rect(self.screen, self.block.color, self.block.blockrect, 0)
        # pygame.draw.rect(self.screen, self.block.color, [self.block.x, self.block.y, self.block.width, self.block.height])
        pygame.draw.rect(self.screen, self.block.color, self.block.blockrect)
        self.info.draw_text('score:'+str(self.info.score),self.screen )


    def run(self):
        while True:

            for event in pygame.event.get():
                self.eventProcess(event)
            if self.runing:
                self.ball.move()
                self.runing = self.ball.judge(self.block,self.info)
                self.draw()
                # pygame.display.flip()是更新所有画面，效率比更新部分画面的update()低
                pygame.display.update()
            self.fclock.tick(self.fps)

class Block:
    width = 200
    height = 3
    color = [0, 0, 0]
    x, y = Game.width/2, Game.height-height
    blockrect = []
    def __init__(self):
        # self.x, self.y = Game.width/2, Game.height-Block.height
        self.blockrect = [self.x, self.y, self.width, self.height]

        # 这里的event是鼠标移动事件
    def move(self, event):
        self.x = event.pos[0] - self.width/2
        # 挡板的y是不会发生变化的
        self.blockrect[0] = self.x
        # self.blockrect = self.blockrect.move(event.pos[0] - self.blockrect.left, 0)

def main():
    ball = Ball()
    block = Block()
    info = Info()
    game = Game(ball, block, info)
    game.run()



if __name__ == '__main__':
    main()
