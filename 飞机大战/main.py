"""
为了防止模块相互依赖，运行是报错：most likely due to a circular import
我们需要吧系统窗口的width，height转移到Info中，否则Game，Fighter相互导入，相互依赖了
"""
import pygame
import sys
from Fighter import Fighter
from Bullet import Bullet
from Info import Info
from Enemy import Enemy


class Game:
    # 记录此类的第一个对象
    instance = None
    # 此背景色和战斗机的一样
    background_color = [201, 202, 207]
    iconPath = "./pic/icon.jpeg"
    caption = "飞机大战"
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

    def __init__(self, fighter, info, enemy, bullet):
        self.fighter = fighter
        self.info = info
        self.enemy = enemy
        self.bullet = bullet
        pygame.init()
        pygame.display.set_icon(pygame.image.load(self.iconPath))
        self.screen = pygame.display.set_mode([self.info.width, self.info.height], pygame.RESIZABLE)
        pygame.display.set_caption(self.caption)
        self.fclock = pygame.time.Clock()


    def eventProcess(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 全屏幕需要按esc退出
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            # 鼠标移动则战斗机移动
            self.fighter.move(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.bullet.create(event)
        # 屏幕大小改变
        elif event.type == pygame.VIDEORESIZE:
            self.info.width, self.info.height = event.size[0], event.size[1]
            self.screen = pygame.display.set_mode([self.info.width, self.info.height], pygame.RESIZABLE)

    def draw(self):
        if not self.runing:
            gameover_surface = pygame.transform.scale(self.info.gameover_img, (self.info.width, self.info.height))
            gameover_rect = gameover_surface.get_rect()
            self.screen.blit(gameover_surface, gameover_rect)
            return

        self.screen.fill(self.background_color)
        # 画战斗机
        self.screen.blit(self.fighter.surface, self.fighter.rect)
        self.info.draw_text('score:'+str(self.info.score), self.screen)
        # 画所有的敌机
        for enemy in self.enemy.enemys:
            self.screen.blit(enemy["surface"], enemy["rect"])
            # print("({0},{1})".format(enemy["x"], enemy["y"]))

        # blt是一个字典，详情见Bullet.create()
        for blt in self.bullet.bullets:
            pygame.draw.rect(self.screen, self.bullet.color, blt["rect"])

    def run(self):
        while True:
            for event in pygame.event.get():
                self.eventProcess(event)
            if self.runing:

                # self.runing = self.fighter.judge(self.info)
                self.enemy.create()
                self.enemy.move()
                self.bullet.move()
                self.enemy.judge(self.info)
                self.bullet.judge(self.enemy.enemys)
                self.draw()
                # pygame.display.flip()是更新所有画面，效率比更新部分画面的update()低
                pygame.display.update()
            self.fclock.tick(self.fps)

def main():
    fighter = Fighter()
    info = Info()
    enemy = Enemy()
    bullet = Bullet()
    game = Game(fighter, info, enemy, bullet)
    game.run()

if __name__ == '__main__':
    main()