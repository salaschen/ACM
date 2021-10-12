'''
Prob: Leetcode 741 - Cherry Pickup
Level: Hard
Author: Ruowei Chen
Date: 17/Oct/2019
Note:
    dp from (0,0) to (N-1,N-1), then walk the path to update the cells.
    Then do the dp from another direction.
'''
from functools import reduce ;

class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        result, direction = self.doDP(grid) ;       
        if result == -1:
            # print(0) ;  # debug
            return 0; 
        self.printGrid(grid) ; # debug
        self.walkGrid(grid, direction) ; 
        self.printGrid(grid) ; # debug
        self.flipGrid(grid) ; 
        self.printGrid(grid) ; # debug
        r2, direction = self.doDP(grid) ; 
        self.walkGrid(grid, direction) ; 
        self.printGrid(grid) ; # debug

        result += r2 ; 
        print(result) ; # debug

        return result;

    # walk the grid and do updates. 
    def walkGrid(self, grid: [[int]], direction) -> None:
        x,y = 0, 0 ; 
        N = len(grid) ; 
        while x < N or y < N:
            grid[x][y] = 0 ; 
            xAdd,yAdd = direction[(x,y)] ; 
            x,y = x+xAdd, y+yAdd ;
        return ;

    def printGrid(self, grid):
        gridString = reduce(lambda r1,r2: r1+'\n'+r2,\
                list(map(lambda row: reduce(lambda n1,n2: \
                '{0:2}'.format(n1)+' '+'{0:2}'.format(n2), row), grid))) ;
        gridString = '*'*20+'\n' + gridString + '\n'+'*'*20 ; 
        print(gridString) ; 
        return ;

    # now need to flip the grid.
    def flipGrid(self, grid):
        N = len(grid) ; 
        for i in range(int((N+1)/2)):
            self.flipTwoRows(grid, i, N-1-i) ; 
        return ;

    def flipTwoRows(self, grid, row1, row2):
        N = len(grid) ; 
        limit = N ; 
        if row1 == row2: limit = int((N+1)/2) ; 
        for i in range(limit):
            grid[row1][i], grid[row2][N-1-i] = grid[row2][N-1-i],grid[row1][i] ; 
        return ;

    # do the dynamic programming to starting from (0,0) down to (N-1,N-1)
    def doDP(self, grid: [[int]]):
        N = len(grid) ; 
        dp = [[0 for i in range(N)] for j in range(N)] ;
        dp[N-1][N-1] = grid[N-1][N-1] ; 
        direction = dict() ; 
        direction[(N-1,N-1)] = (1,1) ; 

        # do the bottom row.
        for i in range(N-2,-1, -1):
            direction[(N-1,i)] = (0,1) ; # can only go to the right.
            if grid[N-1][i] == -1 or grid[N-1][i+1] == -1:
                dp[N-1][i] = -1 ; 
            else:
                dp[N-1][i] = grid[N-1][i] + dp[N-1][i+1] ; 

        # do the rightmost column
        for i in range(N-2, -1, -1):
            direction[(i,N-1)] = (1,0) ; # can only go down.
            if grid[i][N-1] == -1 or grid[i+1][N-1] == -1:
                dp[i][N-1] = -1 ; 
            else:
                dp[i][N-1] = grid[i][N-1] + dp[i+1][N-1] ; 

        # now do the rest rows.
        for i in range(N-2, -1, -1):
            for j in range(N-2, -1, -1):
                if grid[i][j] == -1:
                    dp[i][j] = - 1 ;
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1]) ; 
                    if dp[i][j] == -1:
                        continue ; 
                    else:
                        dp[i][j] += grid[i][j] ; 
                        if dp[i+1][j] > dp[i][j+1]:
                            direction[(i,j)] = (1,0) ; 
                        else:
                            direction[(i,j)] = (0,1) ; 

        return (dp[0][0], direction) ; 
        

######### test methods #########
def test():
    s = Solution() ; 
    g = [[0,1,-1],[1,0,-1],[1,1,1]] ;
    s.cherryPickup(g) ; 
    
    g = [[-1,-1,-1,-1],\
         [-1,-1,-1,-1,],\
         [-1,-1,-1,-1,],\
         [-1,-1,-1,-1,]] ; 
    s.cherryPickup(g) ; 

    g = [[0,0,0,0],\
         [0,0,0,0,],\
         [0,0,0,0,],\
         [0,0,0,0,]] ; 
    s.cherryPickup(g) ; 

    g = [[1,1,1,1],\
         [1,1,1,1,],\
         [1,1,1,1,],\
         [1,1,1,1,]] ; 
    s.cherryPickup(g) ; 

    g = [[ 1, 1, 1, 1],\
         [-1,-1,-1, 1,],\
         [-1,-1,-1, 1,],\
         [-1,-1,-1, 1,]] ; 
    s.cherryPickup(g) ; 

    g = [[ 1, 1, 0, 0],\
         [ 1,-1,-1, 0,],\
         [ 1,-1,-1, 0,],\
         [ 1, 1, 1, 1,]] ; 
    s.cherryPickup(g) ; 

    g = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]] ;
    s.cherryPickup(g) ; 

    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    main() ; 

