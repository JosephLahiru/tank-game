import pygame

from constats import *


class Btn:
    def __init__(self, center_pos: tuple, text: str, second_line: str = None):
        self.rect = pygame.Rect(center_pos[0] - center_pos[2] / 2, center_pos[1] - center_pos[3] / 2, center_pos[2], center_pos[3])
        self.text = text
        self.rendered_text = menu_btn_font.render(text, True, BLACK)

        self.text2 = second_line
        if self.text2 is not None:
            self.rendered_text2 = menu_btn_font2.render(self.text2, True, BLACK)

    def draw(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(sc, BTN_HOVER_COLOR, self.rect, border_radius=5)
        else:
            pygame.draw.rect(sc, BTN_COLOR, self.rect, border_radius=5)

        if self.text2 is not None:
            sc.blit(self.rendered_text, (self.rect.center[0] - self.rendered_text.get_width() / 2, self.rect.center[1] - self.rendered_text.get_height() / 2 - 15))
            sc.blit(self.rendered_text2, (self.rect.center[0] - self.rendered_text2.get_width() / 2, self.rect.center[1] - self.rendered_text2.get_height() / 2 + 25))
        else:
            sc.blit(self.rendered_text, (self.rect.center[0] - self.rendered_text.get_width() / 2, self.rect.center[1] - self.rendered_text.get_height() / 2 + 5))

    def change_text(self, text: str = None, text2: str = None):
        if text is not None:
            self.text = text
            self.rendered_text = menu_btn_font.render(text, True, BLACK)
        if text2 is not None:
            self.text2 = text2
            self.rendered_text2 = menu_btn_font2.render(text2, True, BLACK)


def draw_buttons(btns_list):
    for btn in btns_list:
        btn.draw()
