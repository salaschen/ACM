import collections ; 
import time ; 
import random ; 

class Solution:
    def getAdj(self, cell, N):
        x,y = cell ; 
        result = [(x,y+1),(x,y-1),(x-1,y),(x+1,y)] ; 
        result = list(filter(lambda p: 0<= p[0] < N and 0 <= p[1] < N, result)) ;  
        return result;

    # old solution
    def maxDistance2(self, grid):
        # filter out the non-water and non-land conditions.
        if sum(list(map(lambda lst: lst.count(1), grid))) == 0:
            return -1 ; 
        if sum(list(map(lambda lst: lst.count(0), grid))) == 0:
            return -1 ; 

        # record the distance.
        distance = dict();
        visited = set() ; 
        N = len(grid) ; 
        
        queue = collections.deque() ;
        maxDist = -1 ; 

        # pick the cells that are 1
        for i in range(N): 
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i,j,0)) ; 
                    visited.add((i,j)) ; 

        # go through the queues
        while len(queue) > 0:
            x,y, d = queue.popleft() ; 
            distance[(x,y)] = d ; 
            if d > maxDist:
                maxDist = d ; 
            adj = self.getAdj((x,y), N) ;
            for r,c in adj:
                if (r,c) not in visited:
                    queue.append((r,c,d+1)) ; 
                    visited.add((r,c)) ; 

        return maxDist; 

    def maxDistance(self, grid):
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
    testSize = 10 ; 
    # generate all the test cases.
    passed = 0 ; 
    s = Solution() ; 
    t1, t2 = 0,0 ; 
    for i in range(testSize):
        gridSize = random.randint(3, 100) ; 
        testGrid = genGrid(gridSize) ; 
        a1,tt1 = timeSolRun(s.maxDistance, testGrid) ; 
        a2,tt2 = timeSolRun(s.maxDistance2, testGrid) ; 
        if a1 == a2:
            passed += 1 ;
        t1 += tt1 ;
        t2 += tt2 ; 
    print('{0}/{1} passed, v1:{2} seconds, old:{3} seconds.'.\
            format(passed, testSize, t1, t2)) ;
    return ;

def main():
    # test() ; 
    compare() ; 
    return ; 

if __name__ == "__main__":
    main() ; 

