import game
import gamemode
import options
from button import Btn, draw_buttons
from constats import *

buttons = [Btn((WIN_X / 2, 280, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Play'),
           Btn((WIN_X / 2, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Options'),
           Btn((WIN_X / 2, 580, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Quit')]
title = menu_title_font.render('Tank battle', True, WHITE)
title_pos = title.get_rect()
title_pos.center = (WIN_X/2, 100)


def draw():
    sc.fill(BLACK)

    sc.blit(title, title_pos)

    draw_buttons(buttons)

    pygame.display.update()


def start():
    pygame.init()

    while True:
        pygame.display.set_caption('Menu')
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
                        if btn.text == 'Play':
                            gamemode.start()
                            break
                        elif btn.text == 'Options':
                            options.start()
                            break
                        elif btn.text == 'Quit':
                            return

        draw()
