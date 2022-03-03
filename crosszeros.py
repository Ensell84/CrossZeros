import pygame
from enum import Enum

CELL_SIZE = 60
HEIGHT = 3
WIDTH = 3
FPS = 60


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Player Class. Contains type of cells and name.
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.type = cell_type


class GameField:

    def __init__(self):
        self.height = HEIGHT
        self.width = WIDTH
        self.cells = [[Cell.VOID] * self.height for i in range(self.width)]


class GameFieldView:
    """
    Game field widget, who draws him in window and finds out place of click
    """

    def __init__(self, field: GameField, screen):
        # upload pics of cells
        # draw field
        self.field = field
        self.screen = screen
        self.height = field.height * CELL_SIZE
        self.width = field.width * CELL_SIZE

    def draw(self):
        for i in range(WIDTH + 1):
            pygame.draw.line(self.screen, (0, 0, 0), [30 + i * CELL_SIZE, 30], [30 + i * CELL_SIZE, self.height + 30], 2)

        for i in range(HEIGHT + 1):
            pygame.draw.line(self.screen, (0, 0, 0), [30, 30 + i * CELL_SIZE], [self.width + 30, 30 + i * CELL_SIZE], 2)

    def check_coords_correct(self, x, y):
        if 30 < x < self.width + 30 and 30 < y < self.height + 30:
            return True

    def get_coords(self, x, y):
        return (x-30)//CELL_SIZE, (y-30)//CELL_SIZE



class GameRoundManager:
    """
    Manager of game. Runs all processes. + Draws Cells.
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        if self.field.cells[i][j] == Cell.VOID:
            self.field.cells[i][j] = player.type
            self._current_player = len(self._players) - self._current_player - 1
        print(f"click_handled, {i, j}")
        print(self.field.cells)


class GameWindow:
    """
    Contains Field Widget
    and Game Round Manager.
    """

    def __init__(self):
        # pygame init
        pygame.init()

        # Window
        self._width = WIDTH * CELL_SIZE + 60
        self._height = HEIGHT * CELL_SIZE + 60
        self._title = "Crosses & Zeroes"
        self._screen = pygame.display.set_mode([self._width, self._height])
        pygame.display.set_caption(self._title)
        self._screen.fill((255, 255, 255))

        player1 = Player("1", Cell.CROSS)
        player2 = Player("2", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field, self._screen)

    def mainloop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self._field_widget.check_coords_correct(x,y):
                        i, j = self._field_widget.get_coords(x,y)
                        self._game_manager.handle_click(i, j)
            self._field_widget.draw()
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.mainloop()
    print("Game Over!")


if __name__ == "__main__":
    main()
