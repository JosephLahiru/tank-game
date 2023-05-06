import gamemode
from button import Btn, draw_buttons
from constats import *

buttons = [Btn((WIN_X / 2, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Play again'),
           Btn((WIN_X / 2, 580, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Quit')]
title = menu_title_font.render('Game over', True, WHITE)
title_pos = title.get_rect()
title_pos.center = (WIN_X / 2, 100)


def draw(title2, title2_pos):
    sc.fill(BLACK)

    sc.blit(title, title_pos)
    sc.blit(title2, title2_pos)

    draw_buttons(buttons)

    pygame.display.update()


def start(color_won):
    title2 = menu_title_font.render(color_won + ' has won!', True, BLUE if color_won == 'Blue' else RED)
    title2_pos = title2.get_rect()
    title2_pos.center = (WIN_X / 2, 180)

    pygame.display.set_caption('Game over')

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
                        if btn.text == 'Quit':
                            sys.exit()
                        elif btn.text == 'Play again':
                            gamemode.start()
                            break

        draw(title2, title2_pos)
