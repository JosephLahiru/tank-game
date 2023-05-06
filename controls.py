from button import Btn, draw_buttons
from constats import *

title = menu_title_font.render('Controls', True, WHITE)
title_pos = title.get_rect()
title_pos.center = (WIN_X / 2, 100)


def draw(title2, title2_pos, buttons):
    sc.fill(BLACK)

    sc.blit(title, title_pos)
    sc.blit(title2, title2_pos)

    draw_buttons(buttons)

    pygame.display.update()


def start(player_number):
    buttons = [Btn((WIN_X / 2 - 40, 280, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Forward', settings.player[player_number][0]),
               Btn((WIN_X / 2 - 40, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Backward', settings.player[player_number][1]),
               Btn((WIN_X / 2 - 280 - 40, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Left', settings.player[player_number][2]),
               Btn((WIN_X / 2 + 280 - 40, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Right', settings.player[player_number][3]),
               Btn((WIN_X / 2 + 280 + 40, 250, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Shoot', settings.player[player_number][4]),
               Btn((WIN_X / 2, 580, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Back')]

    pygame.display.set_caption('Controls')
    title2 = menu_title_font2.render('Player ' + str(player_number), True, WHITE)
    title2_pos = title2.get_rect()
    title2_pos.center = (WIN_X / 2, 150)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings.save()
                    return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.rect.collidepoint(pygame.mouse.get_pos()):
                        # click_sound.play()
                        if btn.text == 'Back':
                            settings.save()
                            return
                        else:
                            key_set = False
                            while not key_set:
                                for e in pygame.event.get():
                                    if e.type == pygame.KEYDOWN:
                                        settings.player[player_number][buttons.index(btn)] = pygame.key.name(e.key)
                                        btn.change_text(text2=pygame.key.name(e.key))

                                        key_set = True
                                        break

        draw(title2, title2_pos, buttons)
