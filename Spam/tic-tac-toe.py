import sys
import random

class TicTacToe:
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def __init__(self):
        pass

    def __str__(self):
        return "Tic-Tac_Toe Object"
    
    def start(self):
        print("Play Tic-Tac-Toe!")
        self.userMove()
    
    def userMove(self):
        self.printBoard()
        move = input("Where do you move?")
        self.handleUserMove(move)

    def validator(self):
        if self.checkWinner(1):
            print('You Win!')
            self.printBoard()
            sys.exit()
        if self.checkWinner(2):
            print('You Lose!')
            self.printBoard()            
            sys.exit()

    def handleUserMove(self, move):
        match move:
            case 'top left':
                self.board[0][0] = 1
            case 'top mid':
                self.board[0][1] = 1
            case 'top right':
                self.board[0][2] = 1
            case 'center left':
                self.board[1][0] = 1
            case 'center mid':
                self.board[1][1] = 1
            case 'center right':
                self.board[1][2] = 1
            case 'bottom left':
                self.board[2][0] = 1
            case 'bottom mid':
                self.board[2][1] = 1
            case 'bottom right':
                self.board[2][2] = 1
            case _:
                print('Not a valid move, try again (type "help" for valdi moves)')
                self.handleUserMove(self, move)
        self.validator()
        self.handleAIMove()

    def handleAIMove(self):
        print('___CPU___')
        # really bad AI logic lol
        valid = False
        x = None
        y = None
        while not valid:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y] == 0:
                 self.board[x][y] = 2
                 self.validator()
                 self.userMove()

    def checkWinner(self, player):
        # Check rows and columns
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False
            
    def printBoard(self):
        for column in self.board:
            for num in column:
                if num == 0: 
                    print('□,', end = " ")
                if num == 1: 
                    print('X,', end = " ")
                if num == 2: 
                    print('O,', end = " ")
            print('')

# Run the game
ttt = TicTacToe()
ttt.start()

