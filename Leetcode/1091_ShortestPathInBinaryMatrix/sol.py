'''
Prob: 1091 - Medium - Shortest Path in Binary Matrix
Author: Ruowei Chen
Date: 11/Jan/2020
'''
import heapq ; 
import random ;
import time ;
from collections import deque ;

class Solution:
    def isLegitCoord(self, x, y, N):
        return x >= 0 and x < N and y >= 0 and y < N ; 

    def coordToId(self,x,y,N):
        return (y + x * N) ; 

    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        return self.m2(grid) ; 
        
    def m1(self, grid):
        N = len(grid) ; 
        if grid[0][0] == 1 or grid[N-1][N-1] == 1: 
            return -1 ; 
        edges, dist = self.createEdges(grid) ;
        return self.dijkstra(0, N*N-1, edges, dist) ;
    
    # using bfs
    def m2(self, grid):
        N = len(grid) ; 
        if grid[0][0] == 1 or grid[N-1][N-1] == 1: 
            return -1 ; 
        # edges, _ = self.createEdges(grid) ; 
        
        queue = deque([(1,0,0)]) ; 
        visited = set((0,0)) ; 
        while len(queue) > 0:
            cur = queue.popleft() ; 
            if cur[1] == N-1 and cur[2] == N-1:
                return cur[0] ; 
            
            x,y = cur[1],cur[2] ; 
            points = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1),\
                      (x,y-1),(x,y+1),(x-1,y),(x+1,y)] ; 

            for (px,py) in points:
                if 0 <= px < N and 0 <= py < N and (px,py) not in visited:
                    if grid[px][py] == 1: continue ; 
                    queue.append((cur[0]+1, px,py)) ; 
                    visited.add((px,py)) ; 

        return -1 ; 
        # return self.bfs(0, N*N-1, edges) ;

    def createEdges(self, grid: [[int]]):
        # edges = [[] for x in range(N*N)] ; 
        # develop the edges
        edges = dict() ; 
        dist = dict() ; 
        N = len(grid) ; 
        for x in range(0, N):
            for y in range(0, N):
                if grid[x][y] == 1:
                    continue ;
                v1 = self.coordToId(x,y,N) ; 
                dist[v1] = N * N * 10 ; 
                edges[v1] = [] ; 
                points = [(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1),\
                          (x,y-1),(x,y+1),(x-1,y),(x+1,y)] ; 
                points = list(filter(lambda p: self.isLegitCoord(p[0],p[1],N), points)) ; 
                for (px,py) in points:
                    if grid[px][py] == 0:
                        v2 = self.coordToId(px,py,N) ;    
                        edges[v1].append(v2); 
        return (edges, dist) ; 

    # try using bfs
    def bfs(self, src, dest, edges):
        queue = deque([(1,src)])  ;
        visited = set([src]) ; 
        while len(queue) > 0:
            cur = queue.popleft() ; 
            if cur[1] == dest:
                return cur[0] ; 
            for edge in edges[cur[1]]:
                if edge not in visited:
                    queue.append((cur[0]+1,edge)) ;
                    visited.add(edge) ; 
        return -1 ;    

    def dijkstra(self, source, dest, edges, dist):
        queue = [(1, source)] ; 
        dist[source] = 1 ; 
        visited = set() ; 
        while len(queue) > 0:
            cur = heapq.heappop(queue) ; 
            if cur[1] == dest:
                return cur[0] ; 
            if cur[1] in visited:
                continue ; 
            visited.add(cur[1]) ; 
            for v2 in edges[cur[1]]:
                if dist[v2] > dist[cur[1]] + 1:
                    dist[v2] = dist[cur[1]] + 1 ;
                    heapq.heappush(queue, (dist[v2], v2)) ; 
        return -1;

########### test ############
def randomTest():
    times = 100 ;
    s = Solution() ;
    
    m1Time, m2Time = 0, 0 ; 
    Pass = 0 ; 
    for i in range(times):
        N = random.randint(1, 200) ; 
        grid = [[random.randint(0,1) for x in range(N)] for y in range(N)] ; 
        start = time.time() ; 
        r1 = s.m1(grid) ; 
        end = time.time() ; 
        m1Time += (end-start) ;

        start = time.time() ; 
        r2 = s.m2(grid) ; 
        end = time.time() ;
        m2Time += (end-start) ; 
        
        if r1 == r2: Pass += 1 ; 
    print('{0}/{1} passed. m1 takes {2:.3}sec, m2 takes {3:.3}sec.'\
            .format(Pass, times, m1Time, m2Time)) ; 
    return ; 

def test():
    s = Solution() ; 
    grid = [[0,0,0],[1,1,0],[1,1,0]] ; 
    print(s.shortestPathBinaryMatrix(grid)) ;

    grid = [[0,1],[1,0]] ; 
    print(s.shortestPathBinaryMatrix(grid)) ;

    grid = [[0,1,1],[1,1,0], [0,0,0]] ; 
    print(s.shortestPathBinaryMatrix(grid)) ;

    return ; 

def main():
    randomTest() ; 
    # test() ; 

if __name__ == "__main__":
    main() ; 
