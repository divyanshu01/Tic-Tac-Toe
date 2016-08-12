import random

def drawBoard(board):
	# This function prints out the board that it was passed.
  	# "board" is a list of 10 strings representing the board (ignore index 0)
  	print('   |   |')
  	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  	print('   |   |')
  	print('-----------')
  	print('   |   |')
  	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  	print('   |   |')
  	print('-----------')
  	print('   |   |')
  	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  	print('   |   |')

def inputPlayerLetter():
	#inputs the the letter for the player and returns a list of characters assigned to player ans the computer
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want \'X\' or \'O\'?')
		letter = input().upper()
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	#decides who will go first at the beginning of the game
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'
		
def playAgain():
	#returns True if the player wants to play the game again else returns False
	print('Do you want to play again? yes or no?')
	if input().upper == 'YES':
		return True
	else:
		return False

def makeMove(board, letter, move):
	board[move] == letter
