from constats import *


class BorderWall(pygame.sprite.Sprite):
    def __init__(self, num: int):
        pygame.sprite.Sprite.__init__(self)

        if num == 1:
            self.rect = pygame.Rect(0, 100, WIN_X, WALL_WIDTH)
        elif num == 2:
            self.rect = pygame.Rect(0, 100, WALL_WIDTH, WIN_Y)
        elif num == 3:
            self.rect = pygame.Rect(WIN_X - WALL_WIDTH, 100, WALL_WIDTH, WIN_Y)
        elif num == 4:
            self.rect = pygame.Rect(0, WIN_Y - WALL_WIDTH, WIN_X, WALL_WIDTH)

        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(WALL_COLOR)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        pygame.draw.rect(sc, WALL_COLOR, self.rect)
