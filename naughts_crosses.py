# Naughts and Crosses - Version 2.2
# Alternate between two players.
# Allow column selection
# - Validate it's a valid column
# - Add counter to column
# - - Validate to ensure not taller than permitted.

COLUMNS = 6
ROWS = 5

playerTurn = 1
playerCounters = { 1 : "O", 2 : "X" }
board = { }
isWon = False

def getPlayerCounter():
    global playerTurn
    global playerCounters

    return playerCounters[playerTurn]

def prepareBoard():
    global board
    global COLUMNS

    for x in range(COLUMNS):
        board[x+1] = []

    return board

def nextTurn():
    global playerTurn

    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1

def guardAgainstInvalidColumn(column):
    global COLUMNS

    if column < 0:
        return False

    if column > COLUMNS:
        return False

    return True

def guardAgainstColumnOverflow(column):
    global ROWS
    global board

    if not guardAgainstInvalidColumn(column):
        return False

    if len(board[column]) + 1 > ROWS:
        return False

    return True

def inputColumnSelection():
    try:
        col = int(input("Enter the column (1-6)"))

        if not guardAgainstInvalidColumn(col):
            raise ValueError

        if not guardAgainstColumnOverflow(col):
            raise OverflowError

        return col
    except ValueError:
        print("Your input wasn't valid.")

        return inputColumnSelection()
    except OverflowError:
        print("This column is full.")

        return inputColumnSelection()

def addCounter(column):
    global board
    global playerTurn
    global playerCounters

    board[column].append(getPlayerCounter())

prepareBoard()

while not isWon:
    print("Player %d, it's your turn! You are %s" % (playerTurn, getPlayerCounter()))

    print(board)

    col = inputColumnSelection()

    addCounter(col)

    print("\n=====NEXT PLAYER=====\n")
    nextTurn()

