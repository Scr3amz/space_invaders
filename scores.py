import pygame.font

class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = "white"
        self.font = pygame.font.SysFont("Roboto", 80)
        self.image_score()

    def image_score(self):
        self.score = self.font.render(str(self.stats.score),True, self.text_color)
        self.score_rect = self.score.get_rect()
        self.score_rect.top = 20
        self.score_rect.right = self.screen_rect.right - 20

    def show_scores(self):
        self.screen.blit( self.score, self.score_rect)
