# sudoku solver by Matthew Barbattini

import numpy as np

# initialize the board
board = []
for i in range(9):
	board.append([0] * 9)

# start by filling the board with a random set of numbers
for i in range(9):
	for j in range(9):
		rand_int = np.random.randint(0,10)
		rand_index = np.random.randint(1, 10)
		if rand_index < 3:
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


# dict for each number 1-9 and their frequency
number_dict = {
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


# checks if the 3x3 subgrid has more than 1 of each number in it
def check_subgrid(_subgrid):
	# loop through all 9 positions and update each number's frequency
	for i in range(3):
		for j in range(3):
			num = _subgrid[i][j]
			number_dict[num] += 1
	# if the number has a frequency greater than 1, return false
	for i in range(9):
		if number_dict[i] > 1:
			return False
	return True







def main():
	print_board()






if __name__ == '__main__':
	main()