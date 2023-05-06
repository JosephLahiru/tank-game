import math
import random

from constats import *


class Tank(pygame.sprite.Sprite):
    def __init__(self, player_number: int):
        pygame.sprite.Sprite.__init__(self)

        self.number = player_number
        if player_number == 1:
            self.lvl0 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_blue.png').convert_alpha(), 1 / 6)
            self.lvl1 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_blue_thick.png').convert_alpha(), 1 / 6)
            self.lvl2 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_blue_double.png').convert_alpha(), 1 / 6)
            self.lvl3 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_blue_power.png').convert_alpha(), 1 / 6)
            self.vector = (1, 0)
            self.image = self.lvl0
            self.rect = self.image.get_rect()
            self.rect.center = (90, 185)

        elif player_number == 2:
            self.lvl0 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_red.png').convert_alpha(), 1 / 6)
            self.lvl1 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_red_thick.png').convert_alpha(), 1 / 6)
            self.lvl2 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_red_double.png').convert_alpha(), 1 / 6)
            self.lvl3 = pygame.transform.smoothscale_by(pygame.image.load('./assets/tank_red_power.png').convert_alpha(), 1 / 6)
            self.vector = (-1, 0)
            self.image = self.lvl0
            self.rect = self.image.get_rect()
            self.rect.center = (1115, 630)
        else:
            raise Exception('Tanks other than 1, 2 are not supported yet.')

        self.angle = 0
        self.rotated_rect = self.rect
        self.rotated_img = self.image

        self.x, self.y, self.w, self.h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
        self.speed = 3

        self.alive = True
        self.score = 0

        self.lvl = 0
        self.hp = 1

    def update(self, walls, crates):
        vertical_vec = (0, 1)
        try:  # angle between two vectors. (https://mathsathome.com/wp-content/uploads/2021/12/how-to-find-the-angle-between-two-vectors.png)
            self.angle = math.degrees(math.acos((self.vector[0] * vertical_vec[0] + self.vector[1] * vertical_vec[1]) / (
                    (self.vector[0] ** 2 + self.vector[1] ** 2) ** (1 / 2) * (vertical_vec[0] ** 2 + vertical_vec[1] ** 2) ** (1 / 2))))
            self.angle -= 180
        except ZeroDivisionError:
            self.angle = 0

        if self.vector[0] < 0:
            self.angle = - self.angle

        # https://math.stackexchange.com/questions/897723/how-to-resize-a-vector-to-a-specific-length
        self.vector = (self.vector[0] * (self.speed / ((self.vector[0] ** 2 + self.vector[1] ** 2) ** (1 / 2))),
                       self.vector[1] * (self.speed / ((self.vector[0] ** 2 + self.vector[1] ** 2) ** (1 / 2))))
        # calculate the vector towards target.rect with the length of speed.

        self.handle_keypresses(walls)

        self.rotated_img = pygame.transform.rotate(self.image, self.angle)  # rotate the image
        self.rotated_rect = self.rotated_img.get_rect()  # get the size and pos
        self.rotated_rect.center = (self.rect.x + self.w / 2, self.rect.y + self.h / 2)  # position it into the center
        sc.blit(self.rotated_img, self.rotated_rect)  # draw to screen

    def handle_keypresses(self, walls):
        events = pygame.key.get_pressed()
        if events[pygame.key.key_code(settings.player[self.number][0])]:  # W
            self.move(walls)
        if events[pygame.key.key_code(settings.player[self.number][1])]:  # S
            self.move(walls, True)
        if events[pygame.key.key_code(settings.player[self.number][2])]:  # A
            self.rotate(-0.05, walls)
        if events[pygame.key.key_code(settings.player[self.number][3])]:  # D
            self.rotate(0.05, walls)
        if events[pygame.key.key_code(settings.player[self.number][4])]:  # Shoot
            pass

    def rotate_vector(self, angle: float):
        # https://stackoverflow.com/questions/14607640/rotating-a-vector-in-3d-space
        new_x = self.vector[0] * math.cos(angle) - self.vector[1] * math.sin(angle)
        new_y = self.vector[0] * math.sin(angle) + self.vector[1] * math.cos(angle)
        self.vector = (new_x, new_y)

    def move(self, walls, backwards: bool = False):
        can_move = True
        overlap = self.get_collide_point(walls)
        if overlap:
            vector = ((self.rotated_rect.x + overlap[0]) - self.rotated_rect.center[0], (self.rotated_rect.y + overlap[1]) - self.rotated_rect.center[1])
            angle = math.degrees(
                math.acos((self.vector[0] * vector[0] + self.vector[1] * vector[1]) / (  # calculate angle between the collision point and the driving direction
                        (self.vector[0] ** 2 + self.vector[1] ** 2) ** (1 / 2) * (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2))))
            if not backwards:
                if abs(angle) < 90:
                    can_move = False
            else:
                if abs(angle) > 90:
                    can_move = False
        if can_move:
            if not backwards:
                self.x = self.x + self.vector[0]
                self.y = self.y + self.vector[1]

            else:
                self.x = self.x - self.vector[0] / 2
                self.y = self.y - self.vector[1] / 2
            self.rect = pygame.Rect(self.x, self.y, self.rotated_rect.w, self.rotated_rect.h)

    def rotate(self, angle, walls):
        collide_point = self.get_collide_point(walls)
        if collide_point:
            vector = ((self.rotated_rect.x + collide_point[0]) - self.rotated_rect.center[0], (self.rotated_rect.y + collide_point[1]) - self.rotated_rect.center[1])
            angle1 = math.degrees(math.acos((self.vector[0] * vector[0] + self.vector[1] * vector[1]) / (  # calculate angle between the collision point and the driving direction
                    (self.vector[0] ** 2 + self.vector[1] ** 2) ** (1 / 2) * (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2))))
            self.rotate_vector(angle)
            angle2 = math.degrees(
                math.acos((self.vector[0] * vector[0] + self.vector[1] * vector[1]) / (  # calculate angle between the collision point and the new driving direction
                        (self.vector[0] ** 2 + self.vector[1] ** 2) ** (1 / 2) * (vector[0] ** 2 + vector[1] ** 2) ** (1 / 2))))

            if angle1 < 90:  # collide point is on the front of the tank
                if angle1 > angle2:  # if we are rotating away from the collide point
                    self.rotate_vector(-1 * angle)
            else:
                if angle1 < angle2:
                    self.rotate_vector(-1 * angle)

        else:
            self.rotate_vector(angle)

    def get_collide_point(self, walls):
        mask = pygame.mask.from_surface(self.rotated_img)
        for i in walls:
            offset_x = i.rect[0] - self.rotated_rect.x
            offset_y = i.rect[1] - self.rotated_rect.y

            point = mask.overlap(i.mask, (offset_x, offset_y))
            if point:
                return point
        return None

    def respawn(self):
        self.rect.center = (90 + (TILE_SIZE + 20) * random.randint(0, 7), 120 + TILE_SIZE / 2 + (TILE_SIZE + 20) * random.randint(0, 3))
        self.lvl = 0
        self.image = self.lvl0
        self.x, self.y, self.w, self.h = self.rect.x, self.rect.y, self.rect.w, self.rect.h
        self.hp = 1
