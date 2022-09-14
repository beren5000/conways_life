from life.boards.npboard import NumpyBoard
from life.boards.setboard import SetBoard
from life.boards.cell_status import CellStatus

boards = {
    SetBoard.__name__: SetBoard,
    NumpyBoard.__name__: NumpyBoard
}


def Board(board_type: str, *args, **kwargs):
    if board_type not in boards:
        raise ValueError(f"{board_type} Not a Valid Board")
    return boards[board_type](*args, **kwargs)
