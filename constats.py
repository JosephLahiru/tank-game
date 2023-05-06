import pygame, sys
import time

from settings import Settings

# basic
FPS = 60
WIN_X, WIN_Y = 1204, 712
clock = pygame.time.Clock()
sc = pygame.display.set_mode([WIN_X, WIN_Y])

# fonts
pygame.font.init()
FONT_PATH = './wargate_font.otf'

menu_btn_font = pygame.font.Font(FONT_PATH, 50)
menu_btn_font2 = pygame.font.Font(FONT_PATH, 30)
menu_title_font = pygame.font.Font(FONT_PATH, 80)
menu_title_font2 = pygame.font.Font(FONT_PATH, 35)

# sizes
MENU_BTN_SIZE = (250, 90)
TILE_SIZE = 128

WALL_WIDTH = 20
WALL_LENGTH = TILE_SIZE + 20

# colors
BTN_COLOR = (255, 255, 255)
BTN_HOVER_COLOR = (100, 100, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (80, 80, 232)
RED = (177, 29, 29)

GROUD_COLOR = (45, 45, 45)
WALL_COLOR = (150, 150, 150)

############################################
BULLET_BOUNCES = 10
LIMITED_GAME_MODE_WIN_SCORE = 10

CRATE_IMG = pygame.transform.smoothscale_by(pygame.image.load('./assets/crate.png').convert(), 1 / 6)
settings = Settings()
