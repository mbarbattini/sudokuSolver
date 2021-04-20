# sudoku solver by Matthew Barbattini

import numpy as np
import timeit

# initialize the board
board = []
for i in range(9):
	board.append([0] * 9)

# start by filling the board with a random set of numbers
for i in range(9):
	for j in range(9):
		rand_int = np.random.randint(0,10)
		rand_index = np.random.randint(1, 10)
		if rand_index < 5:
			board[i][j] = rand_int



# prints the board with the usual outlines on the 3x3 grids
def print_board():
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



# creates a 2D array of a 3x3 subgrid from the board, passes in a 2D array
def create_subgrid(grid, x_pos: int, y_pos: int):
	subgrid = [[0,0,0],[0,0,0],[0,0,0]]
	for i in range(0,3,1):
		for j in range(0,3,1):
			subgrid[i][j] = grid[i+3*x_pos-3][j+3*y_pos-3]

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
		num = grid[row_num - 1][j]
		if num != 0:
			number_dict[num] += 1
		# if the number has a frequency greater than 1, return false
	for i in range(len(number_dict)):
		if number_dict[i] > 1:
			return False
	return True





#checks if the column is valid
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
		num = grid[i][col_num - 1]
		if num != 0:
			number_dict[num] += 1
	# if the number has a frequency greater than 1, return false
	for i in range(len(number_dict)):
		if number_dict[i] > 1:
			return False
	return True




# checks if the 3x3 subgrid has more than 1 of each number in it
def check_subgrid(_subgrid):
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
	for i in range(len(_subgrid)):
		for j in range(len(_subgrid[0])):
			num = _subgrid[i][j]
			if num != 0:
				number_dict[num] += 1
	# if the number has a frequency greater than 1, return false
	for i in range(len(number_dict)):
		if number_dict[i] > 1:
			return False
	return True







def main():
	print_board()

	# sub = create_subgrid(board,1,2)
	#print(sub)
	#print(check_subgrid(sub))

	print(column_check(board, 4))
	print(row_check(board, 2))


	# start = timeit.timeit()
	#print(check_subgrid(grid))
	# end = timeit.timeit()
	# print(end - start)





if __name__ == '__main__':
	main()