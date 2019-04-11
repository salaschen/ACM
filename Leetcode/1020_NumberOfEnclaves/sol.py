'''
Leetcode - 1020 Number of Enclaves
Author: Ruowei Chen
Date: 11/Apr/2019
'''
class Solution:
    def numEnclaves(self, A):
        # scan all the boundary points, if it's one, then begin to do
        # a bfs of the point for 1s, and set all the reachable 1s to 0.
        # at the end, count how many 1's left. 
        boundary = getBoundaryPoints(len(A)-1, len(A[0])-1) ; 
        for point in boundary:
            x,y = point ; 
            if A[x][y] == 1:
                bfs(A, x,y) ; 
        
        result = 0 ; 
        for row in A:
            for y in row:
                if  y == 1:
                    result += 1 ; 
        
        return result;        

def bfs(A, x, y):
    queue = [(x,y)] ; 
    seen = set() ; 
    while len(queue) > 0:
        px, py = queue.pop(0) ; 
        A[px][py] = 0 ; 
        adjPoints = getAdjPoints((px, py), len(A)-1, len(A[0])-1) ; 
        for p in adjPoints:
            if A[p[0]][p[1]] == 1 and p not in seen:
                queue.append(p) ;
                seen.add(p) ;
    return ; 

# maxRow - start from 0 to the max (inclusive)
# maxCol - start from 0 to the max (inclusive)
# point - tuple (x, y) x - row, y - col.
# Get all adjacent points of the point
def getAdjPoints(point, maxRow, maxCol):
    x, y = point ; 
    points = [(x+1, y), (x-1,y), (x,y+1), (x, y-1)] ;
    points = list(filter(lambda p: p[0] >= 0 and p[0] <= maxRow, points)) ; 
    points = list(filter(lambda p: p[1] >= 0 and p[1] <= maxCol, points)) ; 
    return points ; 

def getBoundaryPoints(maxRow, maxCol):
    # top row
    points = [(0,x) for x in range(0, maxCol+1)] ; 
    # bottom row
    points.extend([(maxRow, x) for x in range(0, maxCol+1)]) ; 
    # left col
    points.extend([(x, 0) for x in range(0, maxRow+1)]) ; 
    # right col
    points.extend([(x, maxCol) for x in range(0, maxRow+1)]) ; 
    return points ; 

def testBig():
    line = input()[1:-1] ;
    A = [] ; 
    row = [] ; 
    for i in range(0, len(line)):
        if line[i] == '[':
            # start of the row
            txt = '' ; 
        elif line[i] == ']': # end of the row
            row = [int(n) for n in txt.split(',')] ; 
            A.append(row) ; 
        else:
            txt += line[i] ; 
    s = Solution() ;
    result = s.numEnclaves(A) ; 
    print(result) ; 
    return ; 

def main():
    testBig() ; 
    return ;

if __name__ == "__main__":
    main() ; 


