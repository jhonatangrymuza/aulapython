

num = 9
turn = "X"
theBoard = [1, 2, 3,
            4, 5, 6,
            7, 8, 9]

def printBoard():

    
    print(" %s | %s | %s " % (str(theBoard[0]), str(theBoard[1]), str(theBoard[2])))
    print("-- + - + -- ")
    print(" %s | %s | %s " % (str(theBoard[3]), str(theBoard[4]), str(theBoard[5])))
    print("-- + - + -- ")
    print(" %s | %s | %s " % (str(theBoard[6]), str(theBoard[7]), str(theBoard[8])))


def makeMove():
    global theBoard
    global turn
    global num
    move = int(input("Jogador %s qual é seu movimento: " % (turn)))
    if move < 1 or move > 9:
        input("Movimento inválido! [press any key]")
    else:
        theBoard[move-1] = turn
        num =  num - 1 
        if(turn == "X"):
            turn = "O"
        else:
            turn = "X"
def getWin():
    win = False
    for a, b, c in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if theBoard[a] == theBoard[b] == theBoard[c]:
            win = True
            break
    return win
        
# main
printBoard()
while (getWin() == False) and (num > 0):
    makeMove()
    printBoard()
