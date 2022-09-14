from life.boards.cell_status import CellStatus


class SetBoard(set):
    Status = CellStatus

    def __init__(self, width: int = 50, height: int = 50, auto_generate=False, *args, **kwargs):
        super(SetBoard, self).__init__(*args, **kwargs)
        self.width = width
        self.height = height
        if auto_generate:
            self.generate_random_board()

    def _validate_position(self, x, y):
        if x > self.width or y > self.height:
            raise ValueError(
                f" 'X'={x} or 'Y'={y} greater than width={self.width} or height={self.height} respectively"
            )

    def im_alive(self, x: int, y: int) -> bool:
        return True if (x, y) in self else False

    def get_status(self, x: int, y: int) -> Status:
        if self.__contains__((x, y)):
            return self.Status.ALIVE
        return self.Status.DEAD

    def set_status(self, x: int, y: int, status: Status):
        if status == self.Status.ALIVE:
            self.add((x, y))
        if self.__contains__((x, y)) and status == self.Status.DEAD:
            self.remove((x, y))

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
            cells.append(self.get_status(p1, p2))
        return cells

    def generate_random_board(self):
        from random import randrange
        for i in range(randrange(100)):
            self.set_status(*(lambda: (randrange(self.width), randrange(self.height)))(), self.Status.ALIVE)

    def __str__(self):
        resp = "|"
        for x in range(self.width):
            for y in range(self.height):
                to_print = self.get_status(x, y)
                if to_print is self.Status.ALIVE:
                    resp += f"\t{str(to_print.value)}"
                if to_print is self.Status.DEAD:
                    resp += f"\t "
                if y == self.height-1:
                    resp += f"\t|\n"
        return resp

    def __iter__(self):
        for x in range(self.width):
            for y in range(self.height):
                yield {
                    "status": self.get_status(x, y),
                    "index": (x,y)
                }
