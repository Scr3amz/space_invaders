import pygame, control

from pygame.sprite import Group
from gun import Gun
from stats import Stats
from scores import Scores
from health import Health

def run():
    pygame.init()
    width = 1300
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Космические захватчики")
    bg = pygame.image.load("image/space_bg.jpg").convert()
    bg = pygame.transform.scale(bg, (width, height))
    gun = Gun(screen)
    bullets = Group()
    ufos = Group()
    control.ufo_army(screen,ufos)
    stats = Stats()
    scores = Scores(screen, stats)
    health = Health(screen, stats)


    while True:
        control.events(gun,screen,bg, bullets, ufos, scores, stats, health)
        bullets.update()
        gun.move_update()
        control.remove_bullets(bullets)
        control.gun_kill(stats, screen, gun, ufos, bullets , health)
        
run()