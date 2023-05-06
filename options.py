import controls
import settings
from button import Btn, draw_buttons
from constats import *

buttons = [Btn((WIN_X / 2 - 220, 280, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Player 1'),
           Btn((WIN_X / 2 + 220, 280, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Player 2'),
           Btn((WIN_X / 2 - 140, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Sound on' if settings.sound else 'Sound off'),
           Btn((WIN_X / 2 + 140, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Music on' if settings.music else 'Music off'),
           Btn((WIN_X / 2 + 350, 580, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Reset'),
           Btn((WIN_X / 2, 580, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Back')]

control_text = menu_title_font2.render('Controls', True, WHITE)
control_text_pos = control_text.get_rect()
control_text_pos.center = (WIN_X / 2, 280)

title = menu_title_font.render('Options', True, WHITE)
title_pos = title.get_rect()
title_pos.center = (WIN_X / 2, 100)


def draw():
    sc.fill(BLACK)

    sc.blit(title, title_pos)
    sc.blit(control_text, control_text_pos)

    draw_buttons(buttons)

    pygame.display.update()


def start():
    pygame.display.set_caption('Options')

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
                        elif btn.text == 'Reset':
                            settings.reset()
                            buttons[2] = Btn((WIN_X / 2 - 140, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Sound on' if settings.sound else 'Sound off')
                            buttons[3] = Btn((WIN_X / 2 + 140, 410, MENU_BTN_SIZE[0], MENU_BTN_SIZE[1]), 'Music on' if settings.music else 'Music off')

                        elif btn.text.find('Sound') != -1:
                            settings.sound = not settings.sound
                            if btn.text.find('on') != -1:
                                btn.change_text('Sound off')
                            elif btn.text.find('off') != -1:
                                btn.change_text('Sound on')

                        elif btn.text.find('Music') != -1:
                            settings.music = not settings.music
                            if btn.text.find('on') != -1:
                                btn.change_text('Music off')
                            elif btn.text.find('off') != -1:
                                btn.change_text('Music on')

                        elif btn.text == 'Player 1':
                            controls.start(1)
                            break

                        elif btn.text == 'Player 2':
                            controls.start(2)
                            break
        draw()
