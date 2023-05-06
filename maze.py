import random
from pprint import pprint


def generate_maze(rows: int = 4, columns: int = 8):
    scheme = [[' ' for _ in range(columns)] for __ in range(rows)]
    points_with_free_neigbours = []

    def recursive(bod: tuple):
        scheme[bod[1]][bod[0]] = 'X'

        neighbours = get_neighbours(bod)

        if neighbours:
            if len(neighbours) > 1:
                points_with_free_neigbours.append(bod)

            next_point = random.choice(neighbours)
            try:
                walls.remove((bod, next_point))
            except ValueError:
                walls.remove((next_point, bod))
            recursive(next_point)
        else:
            if points_with_free_neigbours:
                next_point = random.choice(points_with_free_neigbours)
                points_with_free_neigbours.remove(next_point)
                recursive(next_point)

    def get_neighbours(point):
        result = []
        possible = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
        for p in possible:
            if 0 <= p[0] < len(scheme[0]) and 0 <= p[1] < len(scheme):
                if scheme[p[1]][p[0]] == ' ':
                    result.append(p)

        return result

    walls = []
    for y in range(rows):
        for x in range(columns):
            if x < columns - 1:
                walls.append(((x, y), (x + 1, y)))
            if y < rows - 1:
                walls.append(((x, y), (x, y + 1)))

    recursive((0, 0))

    return walls
