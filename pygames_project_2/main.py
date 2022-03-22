import pygame

SCREEN_SIZE = width, length = 800, 400


def xs(x):
    return width // 2 + x


def ys(y):
    return length // 2 - y


pygame.init()
pygame.display.set_caption('Тир')
screen = pygame.display.set_mode(SCREEN_SIZE)

pos = xs(0)
angle = -1

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            print(pos)

    if pos == 10 or pos == 790:
        angle = -angle
    pos += angle

    screen.fill('grey')
    pygame.draw.circle(screen, 'blue', (xs(0), ys(0)), 200)
    pygame.draw.circle(screen, 'yellow', (xs(0), ys(0)), 140)
    pygame.draw.circle(screen, 'green', (xs(0), ys(0)), 100)
    pygame.draw.circle(screen, 'brown', (xs(0), ys(0)), 60)
    pygame.draw.circle(screen, 'pink', (xs(0), ys(0)), 40)
    pygame.draw.circle(screen, 'red', (xs(0), ys(0)), 20)

    pygame.draw.circle(screen, 'black', (pos, ys(0)), 10)
    pygame.display.flip()
    clock.tick(500)
pygame.quit()
