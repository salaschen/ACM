'''
Google Code Jam 2019 Round 1C - Bacterial Tactics (Practice)
Date: 03/Jun/2019
Author: Ruowei Chen
Note: 
    1) We can store available horizontal move and vertical move in two different sets.
    2) Use dictionary to store the available moves.
    3) Seems alpha-beta prunning is needed.
    4) 1 is Becca and 0 is Terry.
    5) 06/Jul: so busy with my studies finally have time to tackle this
    problem. I'll try to do it in a brute-force fashion first because the 
    *optimized* version gives WA.
    6) 07/Jul: tested makeMove function. Simple case passed on the test server,
    while the large case is TLE, which is expected for this simple brute-force
    algorithm. It's just a bit disappointed that I should have got this during
    the competition. 
    7) 07/Jul: clean up useless code.
'''

# common function
# board -> board
# move -> ['V' | 'H'] (vertical or horizontal move)
# moveR, moveC -> coordinates of the move, 0-index.
# return True if the move is legal, False otherwise. 
def isLegalMove(board, move, moveR, moveC):
    R = len(board) ; 
    C = len(board[0]) ; 
    if not 0 <= moveR < R:
        return False ; 
    if not 0 <= moveC < C:
        return False ; 
    
    deltaX, deltaY = 1,0 ; 
    if move == 'H':
        deltaX, deltaY = 0,1 ; 

    x, y = moveR, moveC ; 
    if board[x][y] != '.':
        return False ; 

    while 0 <= x < R and 0 <= y < C:
        if board[x][y] == '#': # spread into the radioactive material
            return False ; 
        if board[x][y] != '.':
            break ; 
        x, y = x + deltaX, y + deltaY ; 

    deltaX, deltaY = -1 * deltaX, -1 * deltaY ; 
    x, y = moveR, moveC ; 
    while 0 <= x < R and 0 <= y < C:
        if board[x][y] == '#': # spread into the radioactive material
            return False ; 
        if board[x][y] != '.':
            break ; 
        x, y = x + deltaX, y + deltaY ; 

    # all tests pass
    return True ; 

def makeMove(board, move, moveR, moveC, player):
    R, C = len(board), len(board[0]) ;
    deltaX, deltaY = 1, 0 ; 
    if move == 'H':
        deltaX, deltaY = 0, 1 ;
    x, y = moveR, moveC ; 
    newBoard = [] ;  
    for line in board:
        newBoard.append(line.copy()) ; 
    while 0 <= x < R and 0 <= y < C:
        if newBoard[x][y] != '.':
            break ; 
        newBoard[x][y] = player ; 
        x, y = x+deltaX,y+deltaY ; 
    
    deltaX,deltaY = -1*deltaX,-1*deltaY ; 
    x,y = moveR+deltaX,moveC+deltaY ; 
    while 0 <= x < R and 0 <= y < C:
        if newBoard[x][y] != '.':
            break ; 
        newBoard[x][y] = player ; 
        x, y = x+deltaX,y+deltaY ; 
    
    return newBoard ; 
    

# curPlayer is either 1(Becca) or 0(Terry)
# given the board status, and the player who's going to play the next
# hand. Return curPlayer if there's one move that this player can win.
# return the other player if there's no available move for this player 
# or all the available moves leads to a failure for the current player.
# this is the main function that's going to be used by solve.
def whoWins(board, curPlayer):
    R, C = len(board), len(board[0]) ; 
    nextPlayer = 1-curPlayer ; 
    for x in range(R):
        for y in range(C):
            moves = ['H', 'V'] ; 
            for move in moves:
                if isLegalMove(board, move, x,y):
                    newBoard = makeMove(board, move, x,y, str(curPlayer)) ; 
                    if whoWins(newBoard, nextPlayer) == curPlayer:
                        return curPlayer ; 

    # cannot find a win move for the current player
    # so the other player wins.
    return nextPlayer ; 

# brute-force version of the solve.
def solve2(Case):
    R,C,board = readInput() ; 

    numWinMoves = 0 ; 
    moves = ['H', 'V'] ; 
    player = 1;
    for x in range(R):
        for y in range(C):
            for move in moves:
                if isLegalMove(board, move, x, y):
                    newBoard = makeMove(board, move, x,y,player) ; 
                    if whoWins(newBoard, 1-player) == player:
                        numWinMoves += 1 ; 
    print('Case #{0}: {1}'.format(Case, numWinMoves)) ; 
    return ;

# common function.
# return a tuple of (R,C,board).
# board is List[string]
def readInput():
    R,C = [int(n) for n in input().split()] ; 
    board = [] ; 
    for i in range(R):
        line = input() ; 
        board.append(list(line)) ;
    return (R,C,board) ; 

def work():
    T = int(input()) ; 
    for i in range(1, T+1):
        solve2(i) ; 
    return ;

'''
Test functions.
'''
def test():
    result = tryMove((), 'H', dict(), dict(), 1, None) ; 
    print(result, ',expected 0') ; 
    result = tryMove((), 'H', dict(), dict(), 0, None) ; 
    print(result, ',expected 1') ; 
    return ;

def testLegalMove():
    board = ['..','..'] ; 
    move = 'H' ; 
    moveR, moveC = 0,0 ; 
    print(isLegalMove(board, move, moveR, moveC)) ; 

    board = ['.#', '..'] ; 
    move = 'H' ; 
    x, y = 0,0 ; 
    expect = False ;
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 

    move, expect = 'V', True; 
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 

    # case 3: include radioactive 
    board = ['...','B#.','C..'] ; 
    x,y = 2,1 ; 
    move, expect = 'V', False ; 
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 

    x,y = 2,2 ; 
    move,expect = 'V', True ; 
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 
    
    x,y = 1,0 ; 
    move, expect = 'H', False ; 
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 

    x,y = 1,0 ; 
    move, expect = 'V', False ; 
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 
  
    x,y = 0,0 ; 
    move, expect = 'V', True; 
    print(isLegalMove(board, move, x, y),\
            ', Expect:{0}'.format(expect)) ; 

    return ;

def printBoard(board):
    for line in board:
        l = '' ; 
        for c in line:
            l += str(c) ; 
        print(l) ; 
    return ;

def testMakeMove():
    board = [list('..0'),list('.1.'),list('...')] ; 
    move = 'H' ; 
    x,y = 0,0 ; 
    printBoard(board) ; 
    print(' => move={0} at ({1},{2})'.format(move, x,y)) ; 
    printBoard(makeMove(board, move, x, y, 1)) ; 
    print() ; 

    move = 'V' ; 
    printBoard(board) ; 
    print(' => move={0} at ({1},{2})'.format(move, x,y)) ; 
    printBoard(makeMove(board, move, x, y, 1)) ; 
    print() ; 

    board = [list('..0'),list('.1.'),list('...')] ; 
    move = 'V' ; 
    x,y = 2,0 ; 
    printBoard(board) ; 
    print(' => move={0} at ({1},{2})'.format(move, x,y)) ; 
    printBoard(makeMove(board, move, x, y, 1)) ; 
    print() ; 

    board = [list('..0'),list('.1.'),list('...')] ; 
    move = 'V' ; 
    x,y = 1,2 ; 
    printBoard(board) ; 
    print(' => move={0} at ({1},{2})'.format(move, x,y)) ; 
    printBoard(makeMove(board, move, x, y, 1)) ; 
    print() ; 
    return ;

def main():
    # testMakeMove() ;
    # test() ;
    work() ; 
    # testLegalMove() ; 
    return ;

if __name__ == "__main__":
    main() ; 
