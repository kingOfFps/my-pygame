from Fighter import Fighter
from Info import Info
from Enemy import Enemy
class Bullet:
    width = 5
    height = 15
    # 子弹自由y方向的速度
    speedx = 0
    speedy = -10
    speedup = 4
    # color = "#ff0000"
    color = [255, 0, 0]
    bullets = []
    num = 3

    def __init__(self):
        pass

    def create(self, event):
        # rect1 = rect2 = rect3 =None
        bullet = None
        # 1发子弹
        if Enemy.num < 5:

            bullet = {"rect": [event.pos[0]+Fighter.width/2, event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
        # 2发子弹
        elif 5 <= Enemy.num < 7:
            bullet = {"rect": [event.pos[0], event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
            bullet = {"rect": [event.pos[0]+Fighter.width, event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
        # 3发子弹
        elif 7 <= Enemy.num<= 8:
            bullet = {"rect": [event.pos[0], event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
            bullet = {"rect": [event.pos[0]+Fighter.width/2, event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
            bullet = {"rect": [event.pos[0]+Fighter.width, event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
        # 3发散射子弹
        elif 9 < Enemy.num<= 10:
            bullet = {"rect": [event.pos[0], event.pos[1], self.width, self.height],
                      "speedx": self.speedx-2, "speedy": self.speedy}
            self.bullets.append(bullet)
            bullet = {"rect": [event.pos[0]+Fighter.width/2, event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)
            bullet = {"rect": [event.pos[0]+Fighter.width, event.pos[1], self.width, self.height],
                      "speedx": self.speedx+2, "speedy": self.speedy}
            self.bullets.append(bullet)

        # 5发散射子弹
        else:

            bullet = {"rect": [event.pos[0], event.pos[1], self.width, self.height],
                      "speedx": self.speedx-4, "speedy": self.speedy}
            self.bullets.append(bullet)

            bullet = {"rect": [event.pos[0]+Fighter.width/4, event.pos[1], self.width, self.height],
                      "speedx": self.speedx-2, "speedy": self.speedy}
            self.bullets.append(bullet)

            bullet = {"rect": [event.pos[0]+Fighter.width/2, event.pos[1], self.width, self.height],
                      "speedx": self.speedx, "speedy": self.speedy}
            self.bullets.append(bullet)

            bullet = {"rect": [event.pos[0] +Fighter.width*3/4, event.pos[1], self.width, self.height],
                      "speedx": self.speedx+2, "speedy": self.speedy}
            self.bullets.append(bullet)

            bullet = {"rect": [event.pos[0]+Fighter.width, event.pos[1], self.width, self.height],
                      "speedx": self.speedx+4, "speedy": self.speedy}
            self.bullets.append(bullet)
            print('shoot')

    def move(self):
        for bullet in self.bullets:
            bullet["rect"][0] += bullet["speedx"]
            bullet["rect"][1] += bullet["speedy"]

    # enemys是保存敌机位置的列表,也就是Enemy.enemys
    def judge(self, enemys):
        for bullet in self.bullets:
            for enemy in enemys:
                # 子弹射中敌机
                if enemy["x"]<bullet["rect"][0] and bullet["rect"][0]+self.width<enemy["x"]+ Enemy.width and enemy["y"] + Enemy.height >bullet["rect"][1]:
                    Info.score += 1
                    self.bullets.remove(bullet)
                    enemys.remove(enemy)
                    if Info.score % Enemy.kill_to_upgrade_num == 0:
                        # 每打死kill_to_upgrade_num个敌人，屏幕就会多一个敌人
                        Enemy.num += 1
                        Enemy.kill_to_upgrade_num *= 2
                    return
            # 子弹射出屏幕时，需要把他重列表移除
            if bullet["rect"][1] < 0:
                # 敌人移动到屏幕底部
                self.bullets.remove(bullet)
