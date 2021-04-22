# sudoku solver by Matthew Barbattini

import numpy as np
import timeit


"""
prints the board with the usual outlines on the 3x3 grids
"""
def print_board(board):
	print("-"*23)
	for i in range(9):
		for j in range(9):
			# vertical line for the 3x3 grids
			if j % 3 == 2:
				if board[i][j] != None:
					print(str(board[i][j]), end=" | ")
				else:
					print("_", end=" | ")
			# no lines in between, within a grid
			else:
				if board[i][j] != None:
					print(str(board[i][j]), end=" ")
				else:
					print("_", end=" ")

		if (i % 3 == 2):
			print("\n" + "-"*23)
		else:
			print("\n")


"""
Finds an empty cell in the grid so that we can place a number there.
"""
def find_empty(grid):
	for i in range(9):
		for j in range(9):
			# empty
			if grid[i][j] == 0:
				return i, j
	
	# all cells are full in the grid
	else:
		return False


"""
Tests whether the number is valid based on the 3 rules of sudoku.
"""
def valid(grid, row_pos, col_pos, test_number):

	# check the row
	for i in range(len(grid[0])):
		if grid[row_pos][i] == test_number and col_pos != i:
			return False

	# check the column
	for i in range(len(grid[0])):
		if grid[i][col_pos] == test_number and row_pos != i:
			return False

	# check the box
	box_x = col_pos // 3
	box_y = row_pos // 3

	for i in range(box_y*3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if grid[i][j] == test_number and i != row_pos and j != col_pos:
				return False
	
	return True


"""
Main algorithm. Uses backtracking and recursion. Returns true if complete
"""
def solve(grid):

	# if there are no more empty cells, then the sol is complete
	if find_empty(grid) == False: 
		return True
	else:
		row, col = find_empty(grid)

	# loop through number 1-9
	for i in range(1,10):

		# test if this is a valid sol
		if valid(grid, row, col, i):
			# assign the number
			grid[row][col] = i
			
			if solve(grid):
				return True
		
			# if we reach the end without finding a valid solution, reset it back to 0, move on to the next number
			grid[row][col] = 0

	# if we go through all recursion steps with all numbers, no solution
	return False


def main():
	# initialize the board
# 	board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]

	board = []
	for i in range(9):
		board.append([0] * 9)

	# start by filling the board with a random set of numbers
	for i in range(9):
		for j in range(9):
			rand_int = np.random.randint(0,10)
			rand_index = np.random.randint(1, 10)
			if rand_index < 2:
				board[i][j] = rand_int

	print_board(board)

	start = timeit.timeit()

	solution = solve(board)
	if solution:
		print('The puzzle has been completed.')
	else:
		print('There is no solution.')

	end = timeit.timeit()

	print_board(board)

	print(end - start)


if __name__ == '__main__':
	main()