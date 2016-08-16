import random
import copy

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

def isWinner(board, letter):
	#naive approach to check if the computer/player assigned the given letter won or not
	#this will be checked everytime after the computer or player makes a move
	#returns a boolean value
	return ((board[1] == board[2] == board[3] == letter) or (board[4] == board[5] == board[6] == letter) or
	(board[7] == board[8] == board[9] == letter) or (board[1] == board[4] == board[7] == letter) or
	(board[2] == board[5] == board[8] == letter) or (board[3] == board[6] == board[9] == letter) or
	(board[1] == board[5] == board[9] == letter) or (board[3] == board[5] == board[7] == letter))


def getBoardCopy(board):
	duplicateBoard = []
	duplicateBoard = copy.deepcopy(board)
	return duplicateBoard


def isSpaceFree(board, move):
	#the function checks for free space at the location if its free or not
	#it returns a boolean value
	if board[move] == 'X' or board[move] == 'O':
		return False
	else:
		return True


def getPlayerMove(board):
	#the function is for player to let in their moves
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split(' ') or not isSpaceFree(board, move):
		print('What is your next move? (1-9)')
		move input()
	return int(move)
