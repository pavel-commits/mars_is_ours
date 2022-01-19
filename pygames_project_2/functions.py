def load_image(name, colorkey=False, scale=False):
    import pygame
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