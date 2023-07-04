import pygame

class Gun():
    gun_image = pygame.image.load("image/space-invaders.png")
    gun_image = pygame.transform.scale(gun_image, (100,100))

    
    def __init__(self, screen):
        self.screen = screen
        gun_image = pygame.image.load("image/space-invaders.png")
        gun_image = pygame.transform.scale(gun_image, (75,75))
        self.image = gun_image
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.speed = 2
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
    
    def add_gun(self):
        self.screen.blit(self.image, self.rect)

    def move_update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= self.speed
        if self.move_up and self.rect.top > self.screen_rect.bottom/(1.5) :      
            self.rect.centery -= self.speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:           
            self.rect.centery += self.speed
        
    def create_gun(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


