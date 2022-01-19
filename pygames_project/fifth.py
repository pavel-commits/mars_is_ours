import pygame

screen = pygame.display.set_mode((600, 300))


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


class GameOver(pygame.sprite.Sprite):
    image = load_image('gameover.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = GameOver.image
        self.rect = self.image.get_rect()
        self.rect.x = -self.rect[2]
        self.rect.y = 0

    def update(self):
        if self.rect.x < 0:
            self.rect.x += 1


def main():
    pygame.init()
    pygame.display.set_caption('Game over')

    all_sprites = pygame.sprite.Group()
    GameOver(all_sprites)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color('blue'))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(500)
    pygame.quit()


if __name__ == '__main__':
    main()