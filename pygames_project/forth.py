from random import randrange
import pygame
screen = pygame.display.set_mode((500, 500))


def load_image(name, colorkey=False, scale=False):
    try:
        image = pygame.image.load(f'data/{name}')

        if colorkey:
            image = image.convert()
            image.set_colorkey(image.get_at((0, 0)))
        else:
            image = image.convert_alpha()

        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except FileNotFoundError:
        print('Файл не найден')


class Bomb(pygame.sprite.Sprite):
    image = load_image('bomb.png')
    image_boom = load_image("boom.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.x = randrange(500 - 50)
        self.rect.y = randrange(500 - 51)

    def update(self, *args):

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom
            print(self.rect)


def main():
    pygame.init()
    pygame.display.set_caption('Boom them all')

    all_sprites = pygame.sprite.Group()

    running = True

    for i in range(20):
        Bomb(all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update(event)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()