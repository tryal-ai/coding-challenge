# Sudoku Coding Challenge
This coding challenge is part of the application process for the Tryal.AI 2021 Summer Internship program. It is provided open source, to allow candidates to see the challenge before beginning the application process and assess whether or not they should spend time on previous stages, given that this challenge is ahead.

## Introduction
Sudoku is a fairly straight-forward newspaper puzzle in which a 9x9 grid is filled in with some numbers, ranging from 1 to 9. The objective of the puzzle is to fill in the rest of the grid, such that each row, column and 3 x 3 box (starting from the top left corner, from left to right non-overlapping), does not contain any of the numbers 1 to 9 more than once.

In this challenge, a set of test sudoku boards are available in the `test/sudoku.txt` file. Each line represents a board, going from left to right, top to bottom, with unknown values being represented by 0 (given that 0 is of course an invalid value in sudoku).

There are three sections here that need to be completed, we label them part 1, 2 and 3 although this by no means is the order you should complete these tasks in.

## Part 1 - Solve a board
When the command `python ./__main__.py solve 0173820183782783...` is run, it takes a board as a series of 81 numeric characters. You need to:

1. Solve the problem efficiently, without using an external library that solves sudoku puzzles (although you may use external libraries for any computational processing you wish to do)

2. print the sudoku board to the command line e.g. using `print(board)` 

3. return it at the end of the program using the `Board` class provided

You can find a preconfigured file at `sudoku/programs/solve.py` 

## Part 2 - Solve multiple boards, loaded from a file
When the command `python ./__main__.py file-solve test/sudoku.txt` runs, it takes a file, with a series of boards (one per line) and reads them, you need to:

1. Solve each board efficiently, without using an external library that solves sudoku puzzles (although you may use external libraries for any computational processing you wish to do)

2. return them as an array of boards, in the order they came from file originally

You can find a preconfigured file at `sudoku/programs/file_solve.py`

## Part 3 - Check a boards
When the command `python ./__main__.py validate 127847487182378263...` runs, it takes a **completed** board as a series of 81 numeric characters, you need to:

1. Check if the board is valid (i.e. there's no mistakes in it) without using an external library that checks the correctness of the board

2. Print any errors that exist in the board, in a way that's meaningful to someone reading them and helps them see where they went wrong

3. return `True` if the board is valid and `False` if the board is not

No preconfigured file has been provided for this. You will need to make the appropriate modifications yourself in order to include this program

# What we're looking for

1. Relatively efficient code. Your code should solve sudoku puzzles in a reasonable amount of time

2. Well written code. Your code should be easy for us to understand, even without comments

3. Conformant code. Your code should aim to style itself on the code already in the repo, such that it's almost impossible to tell where yours begin and ours ends

4. self-reliant code. Your code should not overly depend on external dependencies. Whilst external libraries are powerful tools that make life easier, make sure you're not using a sledgehammer to hammer a nail