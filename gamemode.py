import game
import options
from button import Btn, draw_buttons
from constats import *

buttons = [Btn((WIN_X / 2 - 180, 280, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'To ' + str(LIMITED_GAME_MODE_WIN_SCORE)),
           Btn((WIN_X / 2 + 180, 280, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Unlimited')]
title = menu_title_font.render('Choose gamemode', True, WHITE)
title_pos = title.get_rect()
title_pos.center = (WIN_X / 2, 100)


def draw():
    sc.fill(BLACK)

    sc.blit(title, title_pos)

    draw_buttons(buttons)

    pygame.display.update()


def start():
    pygame.display.set_caption('Choose gamemode')

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.rect.collidepoint(pygame.mouse.get_pos()):
                        # click_sound.play()
                        if btn.text.find('To') != -1:
                            game.start('limited')
                            break
                        elif btn.text == 'Unlimited':
                            game.start('unlimited')
                            break

        draw()
