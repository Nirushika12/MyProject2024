board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

currentPlayer= "X"
winner = None
gameRunning = True

# print the game board
def printBoard(board):
    print(board[0] + "  |  "+ board[1] + "  |  " + board[2])
    print("----------------")
    print(board[3] + "  |  "+ board[4] + "  |  " + board[5])
    print("----------------")
    print(board[6] + "  |  "+ board[7] + "  |  " + board[8])
printBoard(board)
    
# player input
def playerInput(board):
    while True:
        try:
            inp = int(input(f"Player {currentPlayer} enter a number 1-9: "))
            if inp >=1 and inp <=9:
                if board[inp-1] == "-":
                    board[inp-1] = currentPlayer
                    break
                else:
                    print("Spot already taken, try again!")
            else:
                print("Invalid number, please enter a number between range 1 to 9.")
        except ValueError:
            print("Invalid input, please enter a number.")
            
# check for win or tie
def checkHorizontal(board):
    global winner
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            winner = board[i]
            return True
    return False
    
def checkRow(board):
    global winner
    for i in range(3):
        if board[i] == board [i+3] == board[i+6] and board[i] != "-":
            winner = board[i]
            return True
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False
        
def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        return True
    return False
        
# switch turns playing 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    if checkWin():
        gameRunning = False # game will end once there is a winner
    else:
        checkTie(board)
        if gameRunning:  # switch player only when the game is still running 
            switchPlayer()