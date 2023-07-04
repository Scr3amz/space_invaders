import pygame

class Ufo(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Ufo, self).__init__()
        self.screen = screen
        ufo_image = pygame.image.load("image/ufo(1).png")
        ufo_image = pygame.transform.scale(ufo_image, (40,40))
        self.image = ufo_image
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def add_ufo(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0.03
        self.rect.y = self.y
        