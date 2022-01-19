import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        x_mouse, y_mouse = mouse_pos
        a = int((x_mouse - self.left) // self.cell_size)
        b = int((y_mouse - self.top) // self.cell_size)
        if 0 <= a < self.width and 0 <= b < self.height:
            return a, b
        return None

    def on_click(self, cell_coords):
        return cell_coords

    def get_click(self, mouse_pos):
        return self.on_click(self.get_cell(mouse_pos))


class Lines(Board):
    def __init__(self, width, height):
        super(Lines, self).__init__(width, height)

    def render(self, screen):
        super(Lines, self).render(screen)
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j]:
                    pygame.draw.rect(screen, (100, 255, 100),
                                     (self.left + j * self.cell_size,
                                      self.top + i * self.cell_size,
                                      self.cell_size, self.cell_size))



    def drawcircles(self, cell):
        if cell is None:
            return
        x_cell, y_cell = cell
        if self.board[y_cell][x_cell] == 0:
            if 1 in [i for j in self.board for i in j]:
                x1, y1, x2, y2 = 0, 0, 0, 0
                pass
                # self.has_path(self, x1, y1, x2, y2)
            else:
                self.board[y_cell][x_cell] = 1

        elif self.board[y_cell][x_cell] == 1:
            self.board[y_cell][x_cell] = 2

        elif self.board[y_cell][x_cell] == 2:
            self.board[y_cell][x_cell] = 1

    def has_path(self, x1, y1, x2, y2):
        pass


pygame.init()
screen = pygame.display.set_mode((400, 400))
board = Lines(10, 10)
board.set_view(5, 5, 39)
board.render(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            board.drawcircles(board.get_click(pos))
    board.render(screen)
    pygame.display.flip()
pygame.quit()

