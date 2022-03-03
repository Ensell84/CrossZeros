import pygame
from enum import Enum

CELL_SIZE = 50
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
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.height for i in range(self.width)]


class GameFieldView:
    """
    Game field widget, who draws him in window and finds out place of click
    """

    def __init__(self, field: GameField):
        # upload pics of cells
        # draw field
        self.field = field
        self.height = field.height * CELL_SIZE
        self.width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True
        # TODO self.height and width

    def get_coords(self, x, y):
        return 0, 0
        # TODO calculate


class GameRoundManager:
    """
    Manager of game. Runs all processes.
    """

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        print(f"click_handled, {i, j}")


class GameWindow:
    """
    Contains Field Widget
    and Game Round Manager.
    """

    def __init__(self):
        # pygame init
        pygame.init()

        # Window
        self._width = 300
        self._height = 400
        self._title = "Crosses & Zeroes"
        self._screen = pygame.display.set_mode([self._width, self._height])
        pygame.display.set_caption(self._title)

        player1 = Player("Петя", Cell.CROSS)
        player2 = Player("Вася", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

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
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.mainloop()
    print("Game Over!")


if __name__ == "__main__":
    main()