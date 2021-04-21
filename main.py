# sudoku solver by Matthew Barbattini

import numpy as np
import timeit




# prints the board with the usual outlines on the 3x3 grids
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
creates a 2D array of a 3x3 subgrid from the board, passes in a 2D array
x_pos and y_pos range from 0-8, they are the position of the cell we want a subgrid for
"""
def create_subgrid(grid, x_pos: int, y_pos: int):
	scaled_x_pos = x_pos // 3 + 1
	scaled_y_pos = y_pos // 3 + 1
	subgrid = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(0,3,1):
		for j in range(0,3,1):
			subgrid[i][j] = grid[i+3*scaled_x_pos-3][j+3*scaled_y_pos-3]

	return subgrid


# checks if the row is valid
def row_check(grid, row_num: int):
	# dict for each number 1-9 and their frequency
	number_dict = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0
	}
	for j in range(9):
		num = grid[row_num][j]
		if num != 0:
			number_dict[num] += 1
		# if the number has a frequency greater than 1, return false
	for i in range(len(number_dict)):
		if number_dict[i] > 1:
			return False
	return True




"""
#checks if the column is valid
"""
def column_check(grid, col_num):
	# dict for each number 1-9 and their frequency
	number_dict = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0
	}
	for i in range(9):
		num = grid[i][col_num ]
		if num != 0:
			number_dict[num] += 1
	# if the number has a frequency greater than 1, return false
	for i in range(len(number_dict)):
		if number_dict[i] > 1:
			return False
	return True



"""
checks if the 3x3 subgrid has more than 1 of each number in it
"""
def check_subgrid(subgrid):
	# dict for each number 1-9 and their frequency
	number_dict = {
		0: 0,
		1: 0,
		2: 0,
		3: 0,
		4: 0,
		5: 0,
		6: 0,
		7: 0,
		8: 0,
		9: 0
	}
	# loop through all 9 positions and update each number's frequency
	for i in range(len(subgrid)):
		for j in range(len(subgrid[0])):
			num = subgrid[i][j]
			if num != 0:
				number_dict[num] += 1
	# if the number has a frequency greater than 1, return false
	for i in range(len(number_dict)):
		if number_dict[i] > 1:
			return False
	return True


"""
Finds an empty cell in the grid so that we can place a number there
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


def valid(grid, test_number, row, col):
	subgrid = create_subgrid(grid, row, col)




"""
Main algorithm. Uses backtracking and recursion. Returns true if complete
"""
def solve(grid):

	# if there are no more empty cells, then the sol is complete
	if find_empty(grid) == False: 
		return True

	# loop through number 1-9
	for i in range(1,10):
		# start by finding an empty cell
		row, col = find_empty(grid)

		# # create the 3x3 subgrid where the current cell is
		# subgrid = create_subgrid(grid, row, col)

		# test if this is a valid sol
		if valid(grid, i, row, col):
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
	board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
	# for i in range(9):
	# 	board.append([0] * 9)

	# # start by filling the board with a random set of numbers
	# for i in range(9):
	# 	for j in range(9):
	# 		rand_int = np.random.randint(0,10)
	# 		rand_index = np.random.randint(1, 10)
	# 		if rand_index < 2:
	# 			board[i][j] = rand_int



	print_board(board)

	# 0-8
	#print(create_subgrid(board, 3, 3))

	solution = solve(board)
	if solution:
		print('The puzzle has been completed.')
	else:
		print('There is no solution.')


	# sub = create_subgrid(board,1,2)
	#print(sub)
	#print(check_subgrid(sub))

	#print(column_check(board, 4))
	#print(row_check(board, 2))


	# start = timeit.timeit()
	#print(check_subgrid(grid))
	# end = timeit.timeit()
	# print(end - start)







if __name__ == '__main__':
	main()