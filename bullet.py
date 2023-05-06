from constats import *


class Bullet:
    def __init__(self, x: int, y: int, vec: tuple, speed=4):
        self.x, self.y = x, y

        self.r = 3
        self.speed = speed
        self.vec = (vec[0] * (self.speed / ((vec[0] ** 2 + vec[1] ** 2) ** (1 / 2))),
                    vec[1] * (self.speed / ((vec[0] ** 2 + vec[1] ** 2) ** (1 / 2))))

        self.x += self.vec[0] * 11
        self.y += self.vec[1] * 11

        self.wall_bounces = 0

        self.image = pygame.Surface((self.r, self.r))
        self.image.fill(WHITE)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, walls):
        time_steps = self.speed * 10  # this is to prevent some bugs like the bullet getting into a wall from a inner corner
        for i in range(time_steps):
            vec_copy = (self.vec[0] / time_steps, self.vec[1] / time_steps)
            self.x += vec_copy[0]
            x_collided = False
            for w in walls:
                if w.rect.collidepoint((self.x, self.y)):
                    self.vec = (-self.vec[0], self.vec[1])
                    if w.rect.center[0] >= self.x:
                        self.x = w.rect.left
                    else:
                        self.x = w.rect.right
                    x_collided = True
                    self.wall_bounces += 1
                    break
            self.x -= vec_copy[0]

            self.y += vec_copy[1]
            if not x_collided:
                for w in walls:
                    if w.rect.collidepoint((self.x, self.y)):
                        self.vec = (self.vec[0], -self.vec[1])
                        self.wall_bounces += 1
                        break

            self.y -= vec_copy[1]

            self.x += self.vec[0] / time_steps
            self.y += self.vec[1] / time_steps

        if self.wall_bounces >= BULLET_BOUNCES:
            return 'kill'

        pygame.draw.circle(sc, WHITE, (self.x, self.y), self.r)
