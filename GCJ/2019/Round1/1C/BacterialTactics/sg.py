'''
Google Code Jam 2019 Round 1C - Bateria Tactics
Sprague-Grundy implementation.
Date: 22/Jul/2019
Author: Ruowei Chen
Note: 
    1) 07/08/2019: Try to figure out what went wrong with the sprague-grundy.
    Use single.in as the case that fails the test.
        - Develop a print board function to help debugging, its signature is 
        printBoard(board, startRow, endRow, startCol, endCol), inclusive.

        - Fix a bug in the isLegalMove function, now time for retest.
'''
# global variables
memory = None ; 
board = None ; 

def readInput(r, c):
    board = [] ; 
    for i in range(r):
        board.append(input()) ; 
    return board; 

# direction is 'V' or 'H'
# when 'V', num is the col number
# when 'H', num is the row number
# return True or False
def isLegalMove(r0, r1, c0, c1, num, direction):
    global board ; 
    # handle the out-of-bound case
    if len(board) == 0:
        return False ; 
    if direction == 'H' and (num < r0 or num > r1):
            return False ; 
    if direction == 'V' and (num < c0  or num > c1):
        return False ; 
    # get the col or row 
    if direction == 'H':
        line = board[num][c0:c1+1] ; 
    else:
        line = ''.join(list(map(lambda row: row[num], board[r0:r1+1]))) ; 

    # make sure line has no radioactive material.
    if '#' in line:
        return False ; 
    else:
        return True ; 

# make the move and divide the board into two sub-boards.
# return the two boards as tuple.
# a board is (r0, r1, c0, c1) where r0 is the first row and r1 is the last row
# c0 is the first column and c1 is the last column. 
# if the board is empty, then return (-1, -1, -1, -1).
def makeMove(r0, r1, c0, c1, num, direction):
    # This should be guarded against in the caller, so I think the caller 
    # shouldn't expect the result to be (None, None).
    '''
    if not isLegalMove(r0, r1, c0, c1, num, direction):
        return (None, None) ; 
    '''

    b1, b2 = None, None ; 
    # divide the board horizontally.
    if direction == 'H':
        if r0 == num:
            b1 = (-1,-1,-1,-1) ; 
        else:
            b1 = (r0,num-1,c0,c1) ; 
        if r1 == num:
            b2 = (-1,-1,-1,-1) ; 
        else:
            b2 = (num+1,r1,c0,c1) ; 

    # divide the board vertically.
    if direction == 'V':
        if c0 == num:
            b1 = (-1,-1,-1,-1) ; 
        else:
            b1 = (r0,r1,c0,num-1) ; 
        if c1 == num:
            b2 = (-1,-1,-1,-1) ; 
        else:
            b2 = (r0,r1,num+1,c1) ;
    return (b1,b2);

# minimum excludant - the first non-negative number 
# that's no in the numSet
def mex(numSet):
    i = 0 ; 
    while i in numSet:
        i += 1 ; 
    return i ;

# Need to know the all possible following Nim states 
# by exploring all the possible legal moves. Then by doing a mex function
# on these nimbers, we know the nimber for the current board. 
# Also, we need to know how many moves are actually winning moves, 
# so we need to calculate how many of these moves that lead to a 
# zero nimber (for your opponent, that means she will fail).
#
# Input (r0, r1, c0, c1): r0: start row, r1: end row (inclusive)
# c0: start column, c1: end column (inclusive). They are used to 
# represent the board. 
# return: (nimDict, nimber)
# nimDict: nimber(follower) -> number of moves
# nimber: the nimber for the current board. 
def getNimber(r0, r1, c0, c1):
    global memory ; 
    global board ; 
    
    nimDict = dict() ; 
    if (r0,r1,c0,c1) == (-1,-1,-1,-1):
        return (nimDict, 0) ; 

    numCol, numRow = abs(c1-c0)+1,  abs(r1-r0)+1;

    # make horizontal moves
    for i in range(r0, r1+1):
        if isLegalMove(r0, r1, c0, c1, i, 'H'):
            sub = makeMove(r0, r1, c0, c1, i, 'H') ; 
            rr0,rr1,cc0,cc1 = sub[0] ; 
            # try to retrieve the nimber from the memory first.
            n1, n2 = 0, 0 ;
            if (rr0, rr1, cc0, cc1) in memory:
                n1 = memory[(rr0,rr1,cc0,cc1)] ; 
            else:
                _, n1 = getNimber(rr0,rr1,cc0,cc1) ; 
            
                            
            rr0,rr1,cc0,cc1 = sub[1] ; 
            if (rr0, rr1, cc0, cc1) in memory:
                n2 = memory[(rr0,rr1,cc0,cc1)] ; 
            else:
                _, n2 = getNimber(rr0,rr1,cc0,cc1) ; 

            nim = n1 ^ n2 ; 
            if nim not in nimDict:
                nimDict[nim] = numCol ; 
            else:
                nimDict[nim] += numCol ; 

    # make vertical moves
    for i in range(c0, c1+1):
        if isLegalMove(r0, r1, c0, c1, i, 'V'):
            sub = makeMove(r0, r1, c0, c1, i, 'V') ; 
            rr0,rr1,cc0,cc1 = sub[0] ; 
            n1, n2 = 0, 0 ;
            if (rr0,rr1,cc0,cc1) in memory:
                n1 = memory[(rr0,rr1,cc0,cc1)] ;
            else:
                _, n1 = getNimber(rr0,rr1,cc0,cc1) ; 

            rr0,rr1,cc0,cc1 = sub[1] ; 
            if (rr0,rr1,cc0,cc1) in memory:
                n2 = memory[(rr0,rr1,cc0,cc1)] ;
            else:
                _, n2 = getNimber(rr0,rr1,cc0,cc1) ; 

            nim = n1 ^ n2 ; 
            if nim not in nimDict:
                nimDict[nim] = numRow ; 
            else:
                nimDict[nim] += numRow ; 

    
    nimber = mex(list(nimDict.keys())) ;

    #  debug
    # printBoard(board, r0, r1, c0, c1) ; 
    # print('nimber={0}'.format(nimber)) ; 
    # print(nimDict) ; 

    memory[(r0,r1,c0,c1)] = nimber ; 
    return (nimDict, nimber) ; 

# calculate a board's nimber value.
# useless function

'''
def nimber(r0, r1, c0, c1):
    # this is the terminal node.
    if (r0,r1,c0,c1) == (-1,-1,-1,-1):
        return 0 ; 
    
    # try to read from the memory
    global memory ; 
    if (r0,r1,c0,c1) in memory:
        return memory[(r0,r1,c0,c1)] ;

    nimDict, nimber = getNimber(r0,r1,c0,c1); 
    return nimber; 
'''

def solveFunc(bd):
    global memory ;
    memory = dict() ; 
    global board ; 
    board = bd ; 
    nimDict, nim = getNimber(0, len(board)-1, 0, len(board[0])-1) ;
    memory = None ; 
    if nim == 0:
        return 0 ; 
    else:
        return nimDict[0] ; 

def solve(Case):
    r, c = [int(x) for x in input().split()] ;
    global board ; 
    board = readInput(r, c) ; 
    
    # nimDict, nim = getNimber(0, len(board)-1, 0, len(board[0])-1) ;
    result = solveFunc(board) ; 
    print('Case #{0}: {1}'.format(Case, result)) ; 
    '''
    if nim == 0:
        print('Case #{0}: {1}'.format(Case, 0)) ; 
    else:
        print('Case #{0}: {1}'.format(Case, nimDict[0])) ;
    '''

    # clear the memory, get ready for the next run. 
    memory = None ; 
    board = None ; 
    return ;

# main work function
def work():
    num = int(input()) ;    
    for i in range(1, num+1):
        solve(i) ; 
    return ;

def printBoard(board, startRow, endRow, startCol, endCol):
    if startRow == -1 and endRow == -1:
        print('Empty') ; 
        return ;
    for r in range(startRow, endRow+1):
        line = '' ; 
        for c in range(startCol, endCol+1):
            line += board[r][c] ;
        print(line) ; 
    return ;
    

# test functions
def testLegalMove():
    global board ;
    board = ['#.##','....','#.##', '#...'] ;
    cases = [(0, 'V', False), (1, 'V', True), (1,'H',True), (0,'H', False),\
            (-1, 'V', False), (-1, 'H', False), (4, 'V', False),\
            (4, 'H', False), (3,'H', False)]; 
    ok = 0 ; 
    r0, r1, c0, c1 = 0, len(board)-1, 0, len(board[0])-1 ;
    for case in cases:
        num, direction, expect = case ; 
        result = isLegalMove(r0,r1,c0,c1, num, direction) ; 
        print('expect={0}, result={1}'.format(expect, result)) ; 
        if result == expect:
            ok += 1 ; 

    print("test passed: {0}/{1}".format(ok, len(cases))) ; 
    return ;

def testMakeMove():
    r0, r1, c0, c1, num, direction = 0, 0, 1, 4, 0, 'H' ; 
    result = makeMove(r0, r1, c0, c1, num, direction) ; 
    print(result) ; 
    return ;

def testNimber():
    global board ;
    global memory ;
    memory = dict() ; 
    board = ['....', '#.##','....','#.##', '....'] ;
    r0, r1, c0, c1 = 0, len(board)-1, 0, len(board[0])-1 ;
    nimDict, nim = getNimber(r0,r1,c0,c1) ; 
    print(nimDict) ;
    print(nim) ; 
    return ;

def test():
    testLegalMove() ; 
    # testMakeMove() ; 
    # testNimber() ; 
    return ;

def main():
    # test() ; 
    work() ; 

if __name__ == "__main__":
    main() ; 
