# Naughts and Crosses - Version 3.1
# Alternate between two players.
# Allow column selection
# - Validate it's a valid column
# - Add counter to column
# - - Validate to ensure not taller than permitted.
# - Check for a winner, vertically
# - Check for a winner, horizontally

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

def drawBoard():
    global board
    global COLUMNS
    global ROWS

    print('| 1 | 2 | 3 | 4 | 5 | 6 |')
    print('-------------------------')

    for row in range(ROWS):
        rowHeight = ROWS - row
        currentRow = '|'
        for col in range(1, COLUMNS + 1):
            if len(board[col]) < rowHeight:
                currentRow += '   |'
            elif board[col][rowHeight - 1] == 'O':
                currentRow += ' O |'
            elif board[col][rowHeight - 1] == 'X':
                currentRow += ' X |'

        print(currentRow)
        print('-------------------------')

def nextTurn():
    global playerTurn

    print("\n=====NEXT PLAYER=====\n")

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

def hasWinnerVertically():
    global board
    global playerCounters

    lastValue = ''
    inlineCount = 0

    for col in board.keys():
        for row in board[col]:
            if row != lastValue:
                lastValue = row
                inlineCount = 1
            else:
                inlineCount += 1

            if inlineCount >= 4:
                return True

        lastValue = ''
        inlineCount = 0

    return False

def hasWinnerHorizontally():
    global board
    global playerCounters
    global ROWS
    global COLUMNS

    lastValue = ''
    inlineCount = 0

    for row in range(ROWS):
        for col in range(1, COLUMNS + 1):
            if len(board[col]) < row + 1:
                lastValue = ''
                inlineCount = 0
                continue

            if board[col][row] != lastValue:
                lastValue = board[col][row]
                inlineCount = 1
            else:
                inlineCount += 1

            if inlineCount >= 4:
                return True

        lastValue = ''
        inlineCount = 0

    return False

def hasWinnerDiagonally():
    global board
    global playerCounters
    global ROWS
    global COLUMNS

    for col in range(1, COLUMNS + 1):
        # | If the column is empty then it can just be skipped.
        rowsHigh = len(board[col])
        if not rowsHigh > 0:
            continue

        for row in range(rowsHigh):
            if findFourDiagonally(col, row, 1, 'right') or findFourDiagonally(col, row ,1, 'left'):
                return True
    return False

# | findFourDiagonally()
# |-----------------------------------------------------------------------
# | Function which searches for matching values around a given space in
# | the board. To be called to check for a diagonal winning move.
# |---------------------------------------------------------
def findFourDiagonally(col, row, count, direction):
    global board

    if count == 4:
        return True

    value = board[col][row]
    newRow = row + 1

    if direction == 'right':
        newCol = col + 1

    if direction == 'left':
        newCol = col - 1

    try:
        newValue = board[newCol][newRow]
    except (IndexError, KeyError):
        return False

    if newValue == value:
        return findFourDiagonally(newCol, newRow, count+1, direction)

def hasWinner():
    if hasWinnerVertically():
        return True

    if hasWinnerHorizontally():
        return True

    if hasWinnerDiagonally():
        return True

    return False

def isDraw():
    return False

def getWinner():
    return "U"

prepareBoard()

while not hasWinner() and not isDraw():
    print("Player %d, it's your turn! You are %s" % (playerTurn, getPlayerCounter()))

    drawBoard()

    col = inputColumnSelection()

    addCounter(col)

    nextTurn()

drawBoard()
if hasWinner():
    print("Player %s has won the game!" % (getWinner()))
else:
    print("It was a draw - nobody won!")
