import pygame
screen = pygame.display.set_mode((400, 400))


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


class Arrow(pygame.sprite.Sprite):
    image = load_image('arrow.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Arrow.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        pygame.mouse.set_visible(False)
        self.rect.x, self.rect.y = pygame.mouse.get_pos()


def main():
    pygame.init()
    pygame.display.set_caption('Свой курсор мыши')

    all_sprites = pygame.sprite.Group()
    Arrow(all_sprites)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('black'))

        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
            all_sprites.update()

        pygame.display.flip()
        clock.tick(500)
    pygame.quit()


if __name__ == '__main__':
    main()