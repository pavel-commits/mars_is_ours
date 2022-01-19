import pygame

pygame.init()
pygame.display.set_caption('Машинка')
screen = pygame.display.set_mode((600, 95))


def load_image(name, colorkey=False, scale=False):
    try:
        image = pygame.image.load(f'data/{name}')
        if colorkey:
            image.set_colorkey(image.convert().get_at((0, 0)))
        else:
            image = image.convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except FileNotFoundError:
        print('Файл не найден')


class Car(pygame.sprite.Sprite):
    image_right = load_image('car2.png')
    image_left = pygame.transform.flip(image_right, True, False)
    image = image_right
    right = True

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        if self.right:
            self.rect.x += 1
            if self.rect[0] + self.rect[2] == 599:
                self.right = False
                self.image = self.image_left
        else:
            self.rect.x -= 1
            if self.rect[0] == 1:
                self.right = True
                self.image = self.image_right


screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
Car(all_sprites)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(70)

pygame.quit()