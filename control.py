import pygame, sys, time

from bullet import Bullet
from ufo import Ufo

def events(gun,screen,bg, bullets, ufos,scores,stats, health):
    screen.blit(bg,(0,0))
    scores.show_scores()
    health.show_health()
    for b in bullets.sprites():
        b.add_bullet()
    gun.add_gun()
    ufos.draw(screen)
    ufos.update()
    collisions = pygame.sprite.groupcollide(bullets, ufos, True, True)

    if collisions:
        for i in collisions.values():
            stats.score += 10 * len(i)
        scores.image_score()

    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                gun.move_right = True
            if e.key == pygame.K_a:
                gun.move_left = True
            if e.key == pygame.K_w:
                gun.move_up = True
            if e.key == pygame.K_s:
                gun.move_down = True
            if e.key == pygame.K_SPACE:
                b = Bullet(screen, gun)
                bullets.add(b)
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                gun.move_right = False
            if e.key == pygame.K_a:
                gun.move_left = False
            if e.key == pygame.K_w:
                gun.move_up = False
            if e.key == pygame.K_s:
                gun.move_down = False


def remove_bullets(bullets):
    for b in bullets.copy():
        if b.rect.bottom <= 0:
            bullets.remove(b)

def ufo_army(screen, ufos):
    ufo = Ufo(screen)
    ufo_width = ufo.rect.width
    distance_between_ufos = 5
    screen_width = screen.get_width()
    ufo_x = int(screen_width/(ufo_width + distance_between_ufos)) - 2
    ufo_height = ufo.rect.height
    # screen_height = screen.get_height()
    ufo_y = 3

    for line in range(ufo_y):
        for u in range(ufo_x):
            ufo = Ufo(screen)
            ufo.x = ufo_width + (ufo_width+distance_between_ufos) * u
            ufo.y = ufo_height + (ufo_height + distance_between_ufos) * line
            ufo.rect.x = ufo.x
            ufo.rect.y = ufo.y
            ufos.add(ufo)

def gun_kill(stats, screen, gun, ufos, bullets, health):

    if stats.gun_health == 0:

        sys.exit()


    if pygame.sprite.spritecollideany(gun, ufos):
        #
        stats.gun_health -= 1
        health.image_health()
        ufos.empty()
        bullets.empty()
        ufo_army(screen, ufos)
        gun.create_gun()
        time.sleep(3)