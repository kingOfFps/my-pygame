import pygame
from Info import Info
# 16:45
class Fighter:
    width = 60
    height = 60
    x, y = Info.width/2, Info.height-height
    picPath = "./pic/fighter.jfif"
    surface = None
    rect = None

    def __init__(self):
        self.surface = pygame.transform.scale(pygame.image.load(self.picPath), (self.width, self.height))
        self.rect = self.surface.get_rect()

    def move(self, event):
        self.x = event.pos[0] - self.width/2
        self.y = event.pos[1] - self.height/2
        self.rect = self.rect.move(event.pos[0] - self.rect.left, event.pos[1] - self.rect.top)

    def judge(self):
        pass


