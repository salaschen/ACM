import collections ; 

class Solution:
    def getAdj(self, cell, N):
        x,y = cell ; 
        result = [(x,y+1),(x,y-1),(x-1,y),(x+1,y)] ; 
        result = list(filter(lambda p: 0<= p[0] < N and 0 <= p[1] < N, result)) ;  
        return result;

    def maxDistance(self, grid):
        # filter out the non-water and non-land conditions.
        if sum(list(map(lambda lst: lst.count(1), grid))) == 0:
            return -1 ; 
        if sum(list(map(lambda lst: lst.count(0), grid))) == 0:
            return -1 ; 

        # record the distance.
        distance = dict();
        N = len(grid) ; 
        
        queue = collections.deque() ;
        maxDist = -1 ; 

        # pick the cells that are 1
        for i in range(N): 
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i,j,0)) ; 
                    distance[(i,j)] = 0 ; 

        # go through the queues
        while len(queue) > 0:
            x,y, d = queue.popleft() ; 
            if (x,y) in distance and distance[(x,y)] < d :
                continue ; 
            else:
                distance[(x,y)] = d ; 
                if d > maxDist:
                    maxDist = d ; 
                adj = self.getAdj((x,y), N) ;
                for r,c in adj:
                    queue.append((r,c,d+1)) ; 

        return maxDist; 

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

def main():
    test() ; 
    return ; 

if __name__ == "__main__":
    main() ; 

