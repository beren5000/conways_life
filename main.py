from life.game import Life
from life.boards import Board
from life.renderer import Renderer


def run_life(game_board=None):
    if not game_board:
        game_board = Board("SetBoard", 60, 60, auto_generate=True)
    game_of_life = Life(game_board)
    cycle = ""
    while cycle == "":
        print(game_of_life.get_board())
        game_of_life.cycle()
        cycle = input("cycle")
    print("the end")


def run_renderer_life(game_board=None):
    if not game_board:
        game_board = Board("SetBoard", 20, 20, auto_generate=True)
    game_of_life = Life(game_board)
    renderer_game = Renderer(game_of_life, width=800, height=800)
    renderer_game.run()


if __name__ == '__main__':
    # a_board = Board(10, 10)
    # a_board.set_status(5, 5, Board.Status.ALIVE)
    # run_life(a_board)
    # run_life()
    run_renderer_life()
