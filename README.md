# Sudoku Solver by Matthew Barbattini

This is a sudoku solver in Python. The program creates a random 9x9 board and prints it on the command line, with the typical outlines on the 3x3 grids. 

The algorithm uses backtracking and recursion to find a solution to the board. It first finds empty space, places a number there, and tests if the row rule, the column rule, and the subgrid rule is valid.
If it is, it places the number there and moves on recursivley to another empty space. If the attempt is invalid, then the algorithm moves backward in the binary tree and tries again.

Inspired by Tech With Tim on Youtube: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
