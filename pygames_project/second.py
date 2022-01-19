import pygame

pygame.init()
pygame.display.set_caption('Герой двигается!')
screen = pygame.display.set_mode((300, 300))


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


class Hero(pygame.sprite.Sprite):
    image = load_image('creature.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Hero.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 10
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 10
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 10
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 10


screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
Hero(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()