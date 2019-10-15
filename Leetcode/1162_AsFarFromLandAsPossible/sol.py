import collections ; 
import time ; 
import random ; 

class Solution:
    def getAdj(self, cell, N):
        x,y = cell ; 
        result = [(x,y+1),(x,y-1),(x-1,y),(x+1,y)] ; 
        result = list(filter(lambda p: 0<= p[0] < N and 0 <= p[1] < N, result)) ;  
        return result;

    # new solution
    def maxDistance(self, grid):

        # record the distance.
        N = len(grid) ; 
        
        queue = collections.deque() ;
        maxDist = -1 ; 

        # pick the cells that are 1
        for i in range(N): 
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i,j,0)) ; 

        if len(queue) == N*N or len(queue) == 0:
            return -1 ; 

        # go through the queues
        level = 0 ; 
        while len(queue) > 0:
            x,y, d = queue.popleft() ; 
            level = d ; 
            # adj = self.getAdj((x,y), N) ;
            for i,j in [(0,-1),(0,1),(1,0),(-1,0)]:
                xi,yj = i+x,y+j ; 
                if 0<= xi < N and 0 <= yj < N and grid[xi][yj] == 0:
                    queue.append((xi,yj,d+1)) ; 
                    grid[xi][yj] = 1 ; 

        maxDist = level ; 
        return maxDist; 

    
    # someone else's solution
    def maxDistanceBase(self, grid) :
        m,n = len(grid), len(grid[0])
        q = collections.deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        if len(q) == m * n or len(q) == 0: return -1
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.popleft()
                for x,y in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    xi, yj = x+i, y+j
                    if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
                        q.append((xi, yj))
                        grid[xi][yj] = 1
            level += 1;
        return level-1 ;
    
    def maxDistanceOld2(self, grid):
        # use a more direct brutal-force method.
        N = len(grid) ; 
        islands = [] ; 
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    islands.append((i,j)) ; 

        # while no island is present
        if len(islands) == 0:
            return -1 ; 

        maxDistanceResult = -1 ; 
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    continue ; 
                temp = min(list(map(lambda cell: abs(cell[0]-i)+abs(cell[1]-j), islands))) ; 
                if maxDistanceResult < temp: 
                   maxDistanceResult = temp ; 
                
        return maxDistanceResult ; 

# Testing Procedures

def test():
    s = Solution() ; 
    grid = [[1,0,1],[0,0,0],[1,0,1]] ; 
    grids = [] ; 
    grids.append((grid, 2)) ; 
    grid = [[1,0,0],[0,0,0],[0,0,0]] ; 
    grids.append((grid, 4)) ; 
    grids.append(([[0,0,0],[0,0,0],[0,0,0]],-1)) ; 
    grids.append(([[1,1,1],[1,1,1],[1,1,1]],-1)) ; 
    passed = 0 ; 
    for g, d in grids:
        if d == s.maxDistance(g):
            passed += 1 ; 
    print('test passed: {0}/{1}'.format(passed, len(grids))) ; 
    return ;

def genGrid(gridSize=5, p=0.2):
    grid = [] ;
    for i in range(gridSize):
        row = [] ;
        for j in range(gridSize):
            if random.uniform(0,1) <= p:
                row.append(1) ; 
            else:
                row.append(0) ; 
        grid.append(row) ; 
    return grid ; 

# wrapper test function.
# sol is either maxDistance or maxDistance2, grid is the grid to be run.
# return the distance and the time to run the solution.
def timeSolRun(sol, grid):
    t0 = time.time() ; 
    answer = sol(grid) ;
    t1 = time.time() ; 
    return (answer, t1-t0) ;

# compare the maxDistance one to maxDistance2 (old)
def compare():
    testSize = 20 ; 
    # generate all the test cases.
    passed = 0 ; 
    s = Solution() ; 
    t1, t2 = 0,0 ; 
    for i in range(testSize):
        gridSize = random.randint(3, 100) ; 
        testGrid = genGrid(gridSize) ; 
        testGrid2 = [x[:] for x in testGrid] ;
        a1,tt1 = timeSolRun(s.maxDistance, testGrid) ; 
        a2,tt2 = timeSolRun(s.maxDistanceBase, testGrid2) ; 
        if a1 == a2:
            passed += 1 ;
        t1 += tt1 ;
        t2 += tt2 ; 
    print('{0}/{1} passed, v1:{2:.3} seconds, base :{3:.3} seconds, ratio:{4:.3}.'.\
            format(passed, testSize, t1, t2, t1/t2)) ;
    return ;

def main():
    # test() ; 
    compare() ; 
    return ; 

if __name__ == "__main__":
    main() ; 

