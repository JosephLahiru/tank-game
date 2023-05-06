import math

import end
from border_wall import BorderWall
from bullet import Bullet
from constats import *
from crate import Crate
from maze import generate_maze
from tank import Tank
from wall import Wall


def get_time(start_time):
    seconds = round(time.time() - start_time)
    minutes = math.floor(seconds / 60)
    seconds -= minutes * 60
    if seconds < 10:
        return f'{minutes}:0{seconds}'
    return f'{minutes}:{seconds}'


def draw(tank1, tank2, walls, bullets, crates, start_time):
    sc.fill(GROUD_COLOR)

    game_time = menu_title_font.render(get_time(start_time), True, WHITE)
    sc.blit(game_time, (WIN_X / 2 - game_time.get_width() / 2, 15))

    tank1_score = menu_title_font.render(str(tank1.score), True, BLUE)
    sc.blit(tank1_score, (30, 15))

    tank2_score = menu_title_font.render(str(tank2.score), True, RED)
    sc.blit(tank2_score, (WIN_X - 30 - tank2_score.get_width(), 15))

    for b in bullets:
        if b.update(walls) == 'kill':
            bullets.remove(b)

    tank1.update(walls, crates)
    tank2.update(walls, crates)

    walls.update()
    crates.update()

    pygame.display.update()


def start(game_type):
    pygame.display.set_caption('Game')

    tank1 = Tank(1)
    tank2 = Tank(2)

    bullets = []
    crates = pygame.sprite.Group()
    walls = pygame.sprite.Group()

    for wall in generate_maze():
        if wall[0][0] == wall[1][0]:  # has same X, so the wall must be horizontal
            walls.add(Wall(wall[1][0], wall[1][1]))
        else:  # vertical
            walls.add(Wall(wall[1][0], wall[1][1], True))

    walls.add(BorderWall(1))
    walls.add(BorderWall(2))
    walls.add(BorderWall(3))
    walls.add(BorderWall(4))

    start_time = time.time()
    crate_last_created = time.time()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                elif event.key == pygame.key.key_code(settings.player[tank1.number][4]):
                    shoot(tank1, bullets)
                elif event.key == pygame.key.key_code(settings.player[tank2.number][4]):
                    shoot(tank2, bullets)

        mask1 = pygame.mask.from_surface(tank1.rotated_img)
        mask2 = pygame.mask.from_surface(tank2.rotated_img)
        for b in bullets:
            if mask1.overlap(b.mask, (b.x - tank1.rotated_rect.x, b.y - tank1.rotated_rect.y)):
                bullets.remove(b)
                tank1.hp -= 1
                if tank1.hp == 0:
                    tank2.score += 1
                    tank1.respawn()

            if mask2.overlap(b.mask, (b.x - tank2.rotated_rect.x, b.y - tank2.rotated_rect.y)):
                bullets.remove(b)
                tank2.hp -= 1
                if tank2.hp == 0:
                    tank1.score += 1
                    tank2.respawn()

        if game_type == 'limited':
            if tank1.score >= LIMITED_GAME_MODE_WIN_SCORE:
                end.start('Blue')
                return
            elif tank2.score >= LIMITED_GAME_MODE_WIN_SCORE:
                end.start('Red')
                return

        if 8 - tank1.lvl - tank2.lvl > 0 and math.floor(time.time() - crate_last_created) == 10:
            crates.add(Crate(crates, tank1, tank2))
            crate_last_created = time.time()

        for t in [tank1, tank2]:
            mask = pygame.mask.from_surface(t.rotated_img)
            for i in crates:
                if mask.overlap(i.mask, (i.rect[0] - t.rotated_rect.x, i.rect[1] - t.rotated_rect.y)):
                    crates.remove(i)
                    t.lvl += 1
                    if t.lvl == 1:
                        t.image = t.lvl1
                    elif t.lvl == 2:
                        t.image = t.lvl2
                    elif t.lvl == 3:
                        t.image = t.lvl3
                        t.hp = 3

        print(tank1.hp)

        draw(tank1, tank2, walls, bullets, crates, start_time)


def shoot(tank, bullets):
    if tank.lvl == 0:
        bullets.append(Bullet(tank.rotated_rect.center[0], tank.rotated_rect.center[1], tank.vector))
    elif tank.lvl == 1:
        bullets.append(Bullet(tank.rotated_rect.center[0], tank.rotated_rect.center[1], tank.vector, 5))
    elif tank.lvl == 2:
        vector = (tank.vector[0] * (tank.speed / ((tank.vector[0] ** 2 + tank.vector[1] ** 2) ** (1 / 2))),
                  tank.vector[1] * (tank.speed / ((tank.vector[0] ** 2 + tank.vector[1] ** 2) ** (1 / 2))))
        vector = (- vector[1] * 1.5, vector[0]*1.5)

        bullets.append(Bullet(tank.rotated_rect.center[0] + vector[0], tank.rotated_rect.center[1] + vector[1], tank.vector, 5))
        bullets.append(Bullet(tank.rotated_rect.center[0] - vector[0], tank.rotated_rect.center[1] - vector[1], tank.vector, 5))
    else:
        vector = (tank.vector[0] * (tank.speed / ((tank.vector[0] ** 2 + tank.vector[1] ** 2) ** (1 / 2))),
                  tank.vector[1] * (tank.speed / ((tank.vector[0] ** 2 + tank.vector[1] ** 2) ** (1 / 2))))
        vector = (- vector[1] * 1.5, vector[0] * 1.5)

        bullets.append(Bullet(tank.rotated_rect.center[0] + vector[0], tank.rotated_rect.center[1] + vector[1], tank.vector, 6))
        bullets.append(Bullet(tank.rotated_rect.center[0] - vector[0], tank.rotated_rect.center[1] - vector[1], tank.vector, 6))

