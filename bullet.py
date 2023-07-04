import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,4,7)
        self.color = "red"
        self.speed = 2
        self.rect.centerx = gun.rect.centerx
        self.rect.bottom = gun.rect.top
        self.y = float(self.rect.y)

    def add_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.y -= self.speed
        self.rect.y = self.y