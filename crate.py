import random

from constats import *


class Crate(pygame.sprite.Sprite):
    def __init__(self, crates, tank1, tank2):
        pygame.sprite.Sprite.__init__(self)

        self.image = CRATE_IMG
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        good_place = False
        while not good_place:
            self.rect.center = (90 + (TILE_SIZE + 20) * random.randint(0, 7), 120 + TILE_SIZE / 2 + (TILE_SIZE + 20) * random.randint(0, 3))
            for i in crates:
                if self.rect.colliderect(i.rect):
                    break
            else:
                if not self.rect.colliderect(tank1.rect) and not self.rect.colliderect(tank2.rect):
                    break

    def update(self):
        sc.blit(self.image, self.rect)
