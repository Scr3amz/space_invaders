import pygame.font

class Health():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = "red"
        self.font = pygame.font.SysFont("Roboto", 80)
        self.image_health()

    def image_health(self):
        self.health = self.font.render(str(self.stats.gun_health), True, self.text_color)
        self.health_rect = self.health.get_rect()
        self.health_rect.left = 40
        self.health_rect.top = 20

    def show_health(self):
        self.screen.blit(self.health, self.health_rect)
