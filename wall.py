from constats import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, vertical: bool = False):
        pygame.sprite.Sprite.__init__(self)

        if vertical:
            self.rect = pygame.Rect(x * (TILE_SIZE + WALL_WIDTH), y * (TILE_SIZE + WALL_WIDTH) + 100, WALL_WIDTH, WALL_LENGTH + WALL_WIDTH)
        else:
            self.rect = pygame.Rect(x * (TILE_SIZE + WALL_WIDTH), y * (TILE_SIZE + WALL_WIDTH) + 100, WALL_LENGTH, WALL_WIDTH)

        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.fill(WALL_COLOR)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        pygame.draw.rect(sc, WALL_COLOR, self.rect)
