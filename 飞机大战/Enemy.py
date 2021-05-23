import random
from Info import Info
import pygame

class Enemy:
    width = 66
    height = 54
    speedx = 2
    speedy = 1
    speed = []
    picPath = "./pic/enemy.png"
    enemys = []
    kill_to_upgrade_num = 3
    num = 3

    def init(self):
        # self.surface = pygame.transform.scale(pygame.image.load(self.picPath), (self.width, self.height))
        # self.rect = self.surface.get_rect()
        pass

    def create(self):
        # 没有这种写法：self.enemys.length
        if len(self.enemys) >= self.num:
            # 敌军数量大于大等于指定数量，不用产生
            return
        temp = self.num - len(self.enemys)
        x = speedx = enemy = surface = rect = None
        for i in range(temp):
            speedx = random.randint(-self.speedx, self.speedx)
            speedy = random.randint(1, self.speedy)

            surface = pygame.transform.scale(pygame.image.load(self.picPath), (self.width, self.height))
            rect = surface.get_rect()
            rect.x = random.randint(0, Info.width-self.width)
            rect.y = 0
            enemy = {"x": rect.x, "y": 0, "speedx": speedx, "speedy": speedy,
                     "surface": surface, "rect": rect}
            self.enemys.append(enemy)



    def move(self):
        # 默认浅拷贝
        for enemy in self.enemys:
            enemy["x"] += enemy["speedx"]
            enemy["y"] += enemy["speedy"]
            enemy["rect"] = enemy["rect"].move([enemy["speedx"], enemy["speedy"]])


    def judge(self, info):
        for enemy in self.enemys:
            # 敌军碰到左右屏幕
            if enemy["x"] < 0 or enemy["x"] + self.width > Info.width:
                enemy["speedx"] = -enemy["speedx"]
            if enemy["y"] > Info.height:
                # 敌人移动到屏幕底部
                self.enemys.remove(enemy)

                # 让敌人逃脱，扣1分
                if Info.score > 0:
                    Info.score -= 1


