'''
Prob: Leetcode 174 - Dungeon Game
Level: Hard
Date: 16/Oct/2019
Author: Ruowei Chen
'''
from functools import reduce;
import random ;

class Solution:
    # the worker function.
    # return the whole dp matrix for debug purpose.
    def calculateMinimumHPSol(self, dungeon):
        M, N = len(dungeon), len(dungeon[0]) ; 
        dp = [[0 for x in range(len(dungeon[0]))] for y in range(len(dungeon))] ;
        dp[M-1][N-1] = -1*dungeon[M-1][N-1] + 1 ;
        if dp[M-1][N-1] <= 0:
            dp[M-1][N-1] = 1 ;
        # handle the bottom row.
        for i in range(N-2, -1, -1):
            dp[M-1][i] = dp[M-1][i+1] + -1*dungeon[M-1][i]  ; 
            dp[M-1][i] = dp[M-1][i] if dp[M-1][i] > 0 else 1 ; 

        # handle the rightmost column
        for i in range(M-2, -1, -1):
            dp[i][N-1] = dp[i+1][N-1] + -1*dungeon[i][N-1] ; 
            dp[i][N-1] = dp[i][N-1] if dp[i][N-1] > 0 else 1 ;
        
        # now handle the rest cells in the bottom up manner.
        for i in range(M-2, -1, -1):
            for j in range(N-2, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) ;  
                dp[i][j] = dp[i][j] + -1*dungeon[i][j] ; 
                dp[i][j] = dp[i][j] if dp[i][j] > 0 else 1 ; 

        return dp[0][0], dp ; 
    
    # the wrapper function.
    # dungeon: List[List[int]]
    # return int
    def calculateMinimumHP(self, dungeon):
        return self.calculateMinimumHPSol(dungeon)[0] ; 

# test functions
def verify(sol, dungeon):
    result, dp = sol.calculateMinimumHPSol(dungeon) ; 
    # print the matrix.
    print('new Case:\n' + ('*'*20)) ; 
    for row in dungeon:
        print(reduce(lambda a,b: a+' '+b, list(map(lambda n: '{0:4}'.format(n), row)))) ;
    print('*'*20) ;
    
    # now walk the matrix.
    x,y = 0,0 ; 
    seenOne = False ; 
    if dp[0][0] == 1:
        seenOne = True ; 
    print('initial HP: {0}, step into ({1},{2}), HP => {3}'.\
            format(dp[0][0], 0,0, dp[0][0]+dungeon[0][0])) ; 
    
    HP = dp[0][0]+dungeon[0][0] ;
    if HP == 1: seenOne = True ; 
    while x < len(dungeon)-1 or y < len(dungeon[0])-1:
        temp = -1 ; 
        if x+1 >= len(dungeon):
            direction = 'right' ; 
            nextX, nextY = x, y+1 ;
        elif y+1 >= len(dungeon[0]):
            direction = 'down' ; 
            nextX, nextY = x+1, y ; 
        else:
            if dp[x+1][y] < dp[x][y+1]:
                direction = 'down' ; 
                nextX, nextY = x+1, y ;
            else:
                direction = 'right' ; 
                nextX, nextY = x, y+1; 
        print('HP:{0}, step {1} into ({2},{3}), HP=>{4}'.\
                format(HP, direction, nextX, nextY, HP+dungeon[nextX][nextY])) ;
        HP = HP+dungeon[nextX][nextY] ;
        x,y = nextX, nextY ; 
        if HP == 1: seenOne = True ; 
        if HP <= 0:
            print('player is dead, test failed.') ; 
            return 0 ; 
    if not seenOne:
        print('player is alive, but the HP is not minimum, failed') ; 
        return 0 ;
    
    print('player is alive, test passed.') ; 
    return 1;

def genDungeon(m=5,n=4):
    dungeon = [] ;
    for i in range(m):
        row = []; 
        for j in range(n):
            temp = random.randint(-500, 500) ; 
            row.append(temp) ; 
        dungeon.append(row) ; 
    return dungeon ; 

def test():
    s = Solution() ; 
    testNum = 100 ; 
    passed = 0 ; 
    for i in range(testNum):
        dungeon = genDungeon() ;
        passed += verify(s, dungeon) ; 
    print('total: {0}/{1} passed'.format(passed, testNum)) ; 
    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    main() ; 

