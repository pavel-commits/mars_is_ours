import pygame
from functions import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)

    def update(self, *arg):
        if arg[0] == 'x':
            self.rect.x += arg[1] * tile_width
        elif arg[0] == 'y':
            self.rect.y += arg[1] * tile_height


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))



def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    return new_player, x, y




import pygame
from math import sin, cos, pi

SCREEN_SIZE = width, length = 1000, 1000
N = 9


def xs(x):
    return width // 2 + x


def ys(y):
    return length // 2 - y


def draw_sun(screen, angle_1, angle_2, angle_3, angle_sun):
    screen.fill('grey')
    pygame.draw.circle(screen, 'yellow', (xs(0), ys(0)), 50)

    for i in range(N):
        pygame.draw.line(screen, 'yellow',
                         (xs(50 * cos((i * pi * 2 / N) + (pi * angle_sun / 180))),
                          ys(50 * sin((i * pi * 2 / N) + (pi * angle_sun / 180)))),
                         (xs(125 * cos((i * pi * 2 / N) + (pi * angle_sun / 180))),
                          ys(125 * sin((i * pi * 2 / N) + (pi * angle_sun / 180)))), 10)

    pygame.draw.circle(screen, 'black', (xs(0), ys(0)), 200, 1)
    pygame.draw.circle(screen, 'black', (xs(0), ys(0)), 300, 1)
    pygame.draw.circle(screen, 'black', (xs(0), ys(0)), 420, 1)

    pygame.draw.circle(screen, 'red', (xs(200 * cos(angle_1 * pi / 180)),
                                       ys(200 * sin(angle_1 * pi / 180))), 30)

    pygame.draw.circle(screen, 'green', (xs(420 * cos(angle_2 * pi / 180)),
                                         ys(420 * sin(angle_2 * pi / 180))), 50)

    pygame.draw.circle(screen, 'blue', (xs(300 * cos(angle_3 * pi / 180)),
                                        ys(300 * sin(angle_3 * pi / 180))), 30)

    pygame.draw.circle(screen, 'blue', (xs(300 * cos(angle_3 * pi / 180)),
                                        ys(300 * sin(angle_3 * pi / 180))), 60, 3)


pygame.init()
pygame.display.set_caption('Мой проект')
screen = pygame.display.set_mode(SCREEN_SIZE)
angle_sun = 0
angle_1 = 51
angle_2 = 240
angle_3 = 300
clock = pygame.time.Clock()
action = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if action:
                action = False
            else:
                action = True

    if action:
        angle_sun += 3
        angle_1 -= 2
        angle_2 -= 2
        angle_3 += 2

    draw_sun(screen, angle_1, angle_2, angle_3, angle_sun)

    pygame.display.flip()
    clock.tick(10)
pygame.quit()
