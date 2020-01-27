'''
Prob: UVA 1603 Square Destroyer
Date: 26/Jan/2020 - Happy Australia Day!
Author: Ruowei chen
Note: 
    1) Use iterative deepening dfs. 
'''
class Square:
    def isVertical(self, index, n):
        temp = index % (2*n+1) ; 
        return temp == 0 or temp > n ; 

    # create the square given the top left edge's index,
    # and the size of the square, and n is the n*n square's size
    # the index starts from 1.
    def __init__(self, topLeftIndex, size, n):
        self.edges = set() ; 
        self.size = size ; 
        self.n = n ; 

        # make sure the edge given is actually a vertical edge.
        if not self.isVertical(topLeftIndex,n):
            print('not vertical') ; # debug
            return None; 

        # calculate the row and column of the top left edge.
        # column and row also starts from 1. 
        col = n+1 if topLeftIndex % (2*n+1) == 0 else (topLeftIndex % (2*n+1)) - n ; 
        row = topLeftIndex // (2*n+1) + 1 ; 

        # now test if the square can be created.
        if topLeftIndex <= 0 or col + size > n+1 or row + size > n+1:
            # print('out of limit') ; # debug
            return None ; 
        
        # now create the square as a set of edges.
        top = topLeftIndex - n ;
        # adding the top edges.
        for i in range(size):
            self.edges.add(top+i) ; 

        # adding the left edges.
        left = topLeftIndex ; 
        for i in range(size):
            self.edges.add(left+i*(2*n+1)) ; 

        # adding the right edges:
        right = topLeftIndex + size ; 
        for i in range(size): 
            self.edges.add(right+i*(2*n+1)) ; 

        # adding the bottom edges:
        bottom = top + (2*n+1) * size ; 
        for i in range(size):
            self.edges.add(bottom+i) ; 
        return ; 
        
    def __str__(self):
        if len(self.edges) == 0: return 'None' ; 
        edges = sorted(list(self.edges)) ; 
        topLeft = edges[0]+ self.n ; 
        return '{0} size: {1} ->'.format(topLeft, self.size) +  str(edges); 

# create all the squares in a n*n matrix.
# tested
def createAllSquares(n):
    squareList = [] ; 
    dummy = Square(0, 1, 1) ; 
    for i in range(1, (2*n+1)*n+n+1):
        if dummy.isVertical(i, n):
            for size in range(1, n+1):
                sq = Square(i, size, n) ; 
                if len(sq.edges) > 0:
                    squareList.append(sq) ; 
    return squareList ; 

# given an edge and the list of squares that are currently complete,
# return the list of squares that are still complete after removing the edge.
# tested.
def deleteEdge(edge : int, squares: [int], squareList: [Square]) -> [int]:
    if edge == 0: return squares ; 
    remain = [] ; 
    for sq in squares:
        square = squareList[sq] ; 
        if edge not in square.edges:
            remain.append(sq) ; 
    return remain;  

def test():
    # s = Square(1, 4, 3) ; 
    squareList = createAllSquares(3) ; 
    squares = [i for i in range(0, len(squareList))] ; 
    edge = 14 ; 
    remain = deleteEdge(edge, squares, squareList) ; 
    print(remain) ; 
    for r in remain:
        print(squareList[r]) ; 
    return ; 

def work():
    n = int(input()) ; 
    missing = [int(n) for n in input().split()] ; 
    squareList = createAllSquares(n) ; 
    squares = [i for i in range(len(squareList))] ; 
    # delete all the squares that are affected by the missing edges.
    for edge in missing:
        squares = deleteEdge(edge, squares, squareList) ; 
    
    if len(squares) == 0:
        return 0 ; 

def main():
    # test() ; 
    T = int(input()) ; 
    for i in range(T):
        work() ; 
    pass ; 

main() ; 


