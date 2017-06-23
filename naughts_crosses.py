# Naughts and Crosses - Version 1
# Alternate between two players.

playerTurn = 1
isWon = False

def nextTurn():
    global playerTurn

    if playerTurn == 1:
        playerTurn = 2
    else:
        playerTurn = 1

while not isWon:
    print("Player %d, it's your turn!" % (playerTurn))
    input("Press <enter> to take your turn.")

    nextTurn()

