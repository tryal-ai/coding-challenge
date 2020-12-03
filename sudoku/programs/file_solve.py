from argparse import ArgumentParser

def program(args):

    # Your code here (Part 2)

    pass


def parser(init : ArgumentParser):
    init.add_argument("file", type=str, help="The file path to the file containing the boards to solve")
    init.set_defaults(func=program)