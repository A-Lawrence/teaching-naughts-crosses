# Naughts and Crosses - Version 2
# Alternate between two players.
# Allow column selection
# - Validate it's a valid column

COLUMNS = 6

playerTurn = 1
isWon = False

def nextTurn():
    global playerTurn

    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1

def validateColumn(column):
    global COLUMNS

    if column < 0:
        return False

    if column > COLUMNS:
        return False

    return True

def inputColumnSelection():
    try:
        col = int(input("Enter the column (1-6)"))

        if not validateColumn(col):
            raise ValueError
    except ValueError:
        print("Your input wasn't valid.")

        return inputColumnSelection()

while not isWon:
    print("Player %d, it's your turn!" % (playerTurn))

    col = inputColumnSelection()

    print("\n=====NEXT PLAYER=====\n")
    nextTurn()

