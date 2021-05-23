import pygame
class Info:
    width = 1200
    height = 700
    score = 0
    gameover_img = pygame.image.load("./pic/gameover.png")

    def draw_text(self, text, screen):
        font = pygame.font.Font("fonts/MONACO.TTF", 24)
        survivedtext = font.render(str(text), True, (0, 0, 0))
        textRect = survivedtext.get_rect()
        textRect.topleft = [10, 10]
        screen.blit(survivedtext, textRect)