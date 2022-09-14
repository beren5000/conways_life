import numpy as np

from life.boards.cell_status import CellStatus


class NumpyBoard:
    Status = CellStatus

    def __init__(self, width: int = 50, height: int = 50, auto_generate=False):
        self.width = width
        self.height = height
        if auto_generate:
            self._BOARD = self.generate_random_board()
        else:
            self._BOARD = np.full((width, height), self.Status.DEAD, dtype=self.Status)

    def _validate_position(self, x, y):
        if x > self.width or y > self.height:
            raise ValueError(
                f" 'X'={x} or 'Y'={y} greater than width={self.width} or height={self.height} respectively"
            )

    def im_alive(self, x: int, y: int) -> bool:
        return self._BOARD[x, y] is self.Status.ALIVE

    def get_status(self, x: int, y: int) -> Status:
        return self._BOARD[x, y]

    def set_status(self, x: int, y: int, status: Status):
        self._validate_position(x, y)
        self._BOARD[x, y] = status

    def _look_around(self, x, y) -> list:
        step = 1
        positions = [(a, b) for a in range(x-1, x+step+1, step) for b in range(y-1, y+step+1, step)]
        positions = list(filter(
            lambda point: 0 <= point[0] < self.width and 0 <= point[1] < self.height and point != (x, y),
            positions
        ))
        return positions

    def get_around(self, x, y) -> list:
        cells = list()
        positions = self._look_around(x, y)
        for p1, p2 in positions:
            cells.append(self._BOARD[p1, p2])
        return cells

    def generate_random_board(self):
        return np.random.choice([self.Status.DEAD, self.Status.ALIVE], size=(self.width, self.height))

    def __str__(self):
        resp = "|"
        with np.nditer(self._BOARD, flags=['multi_index', 'refs_ok'], op_flags=['readonly']) as it:
            for i in it:
                to_print = i.item()
                if to_print == self.Status.DEAD:
                    to_print = " "
                else:
                    to_print = to_print.value
                resp += f"\t{str(to_print)}"
                if it.multi_index[1] == self.width-1:
                    resp += "\t|\n|"
        return resp

    def __iter__(self):
        with np.nditer(self._BOARD, flags=['multi_index', 'refs_ok'], op_flags=['readonly']) as it:
            for i in it:
                yield {
                    "status": i.item(),
                    "index": it.multi_index
                }
