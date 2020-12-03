import argparse
import sudoku.programs as progs
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="The Sudoku solver is designed to solve sudoku problems")
    
    def show_help(args):
        parser.print_help()
    
    parser.set_defaults(func=show_help)

    programs = parser.add_subparsers()
    
    progs.solve.parser(programs.add_parser("solve", help="Solve a given string representing a sudoku board"))
    progs.file_solve.parser(programs.add_parser("file-solve", help="Solve all the boards in a given file"))

    args = parser.parse_args()
    args.func(args)