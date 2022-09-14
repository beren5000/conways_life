from copy import deepcopy
from life.boards import CellStatus


class Life:

    def __init__(self, board):
        self._BOARD = board

    def death_or_alive(self, x, y):
        status = self._BOARD.get_status(x, y)
        cells_alive_around = self._BOARD.get_around(x, y).count(CellStatus.ALIVE)
        if (status == CellStatus.ALIVE) and (cells_alive_around <= 1):  # solitude
            return CellStatus.DEAD
        if (status == CellStatus.ALIVE) and cells_alive_around >= 4:  # overpopulation
            return CellStatus.DEAD
        if (status == CellStatus.ALIVE) and cells_alive_around in [2, 3]:  # good one
            return CellStatus.ALIVE
        if (status == CellStatus.DEAD) and cells_alive_around == 3:  # born
            return CellStatus.ALIVE
        return status

    def cycle(self):
        temp_board = deepcopy(self._BOARD)
        for h in range(self._BOARD.height):
            for w in range(self._BOARD.width):
                status = self.death_or_alive(w, h)
                temp_board.set_status(w, h, status)
        del self._BOARD
        self._BOARD = temp_board
        del temp_board

    def get_board(self):
        return self._BOARD
