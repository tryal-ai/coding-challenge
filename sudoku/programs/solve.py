from sudoku.lib.Board import Board
from argparse import ArgumentParser

def program(args):
    board = Board(args.board)

    # Your code here (Part 1)

    return board


def parser(init : ArgumentParser):
    init.add_argument("board", type=str, help="A string of the board going left to right, top to bottom, with 0 representing unknown values")
    init.set_defaults(func=program)