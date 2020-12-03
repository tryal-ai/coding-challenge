class Board:
    def __init__(self, board : str):
        if len(board) != 81:
            raise ValueError("The length of the Sudoku string to initialise the board is incorrect")
        self.data = [int(c) for c in board]
    
    @staticmethod
    def read_from_file(file : str):
        with open(file, 'r') as f:
            return [Board(line) for line in f]

    def get_cell_value(self, x : int, y : int):
        position = y * 9 + x
        return self.data[position]

    def set_cell_value(self, x : int, y : int, val : int):
        position = y * 9 + x
        self.data[position] = val

    def __str__(self):
        out = ""
        for y in range(0, 9):
            for x in range(0, 9):
                out += str(self.data[y * 9 + x])
                if x == 2 or x == 5:
                    out += "|"
            out += "\n"
            if y == 2 or y == 5:
                out += ("-" * 11) + "\n"
        return out