'''
Prob: Leetcode 1263 - Hard - Storekeeper game.
Author: Ruowei Chen
Date: 17/Nov/2019
Note:
    1) Use memoization to remember the searched state.
    2) Use BFS + A* to do the state search.
    3) First find all the distance from the target to all other points, used as heuristics.
    4) 21/Nov：Added a few important subroutines.
    5) 29/Nov: Add linked list as representation of the graph.
'''
import heapq ; 
from functools import reduce ; 
import collections ; 

class Solution:
    # nice print of the grid - for debug purpose.
    def printGrid(self, grid:[[int]]): 
        print(reduce(lambda row1,row2: row1+row2, \
            list(map(lambda row: reduce(lambda x,y: x+y, row)+'\n', grid)))) ; 

    # return True if the pos is in the grid and not a wall 
    def isLegit(self, grid, pos):
        x, y = pos ; 
        if x < 0 or y < 0 or x >= self.row or y >= self.col:
            return False ; 
        if grid[x][y] == '#': 
            return False ;
        else:
            return True ; 

    # Create linked list graph from the grid (done)
    def createGraph(self, grid:[[str]]):
        graph = dict() ; 
        row, col = len(grid), len(grid[0]) ; 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '#':
                    graph[(i,j)] = None ; 
                    continue ; 
                neighbors = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] ; 
                graph[(i,j)] = [] ; 
                for npoint in neighbors:
                    if self.isLegit(grid, npoint):
                        graph[(i,j)].append(npoint) ; 
        return graph;  

    # the main function - minimum steps to push the box into target position.
    def minPushBox(self, grid: [[str]]) -> int:
        # snapshot is the position of the store keeper plus
        # the position of the box.
        self.heuristic = dict() ; 
        self.row = len(grid) ; 
        self.col = len(grid[0]) ; 
        self.graph = self.createGraph(grid); # create a graph.
        target = (0,0) ; 
        bstart, pstart = (0,0), (0,0) ; 
        # read the grid into the data structure.
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 'T':
                    target = (i,j) ; 
                elif grid[i][j] == 'B':
                    bstart = (i,j) ; 
                elif grid[i][j] == 'S':
                    pstart = (i,j) ; 

        self.GenHeuristic(target, grid, self.heuristic) ; 
        result = self.AStar(target, grid, bstart, pstart) ; 
        return result ; 

    # target is the target destination of the box
    # grid is the map
    # bstart is the start position of the box, pstart is the start of the people
    def AStar(self, target:(int,int), grid:[[str]], bstart: (int,int), pstart: (int,int)):
        result = -1 ; 
        # to memorize the states that have been searched.
        # a state is (box, people)
        memory = set() ; 
        queue = [] ; # need to be a min heap
        state = (0, bstart, pstart ) ; 
        heapq.heappush(queue, (self.heuristic[bstart], state)) ; 
        memory.add((bstart, pstart)) ; 
        while len(queue) > 0:
            h,state = heapq.heappop(queue) ; 
            depth, boxPos, playerPos = state ; 
            if boxPos == target: # if the box is on the target.
                result = h; 
                break ; 
            # else need to expand this state.
            newDepth = depth + 1 ; 
            newStates = self.expandState(grid, boxPos, playerPos) ; 
            for st in newStates:
                newBoxPos, newPlayerPos = st ; 
                if (newBoxPos, newPlayerPos) in memory: continue ; 
                newH = newDepth + self.heuristic[newBoxPos] ; 
                newState = (newDepth, newBoxPos, newPlayerPos) ; 
                heapq.heappush(queue, (newH, newState)) ; 
                memory.add((newBoxPos, newPlayerPos)) ; 
                
        return result ; 

    # return a list of reachable, gameState, which is represented by a tuple (boxPos, playerPos).
    def expandState(self, grid: [[str]], box:(int,int), player:(int,int)) \
        -> [((int,int),(int,int))]:
        bx,by = box ; 
        newBoxStates = [(bx+1,by),(bx-1,by),(bx,by+1),(bx,by-1)] ;
        newPlayerStates = [(bx-1,by),(bx+1,by),(bx,by-1),(bx,by+1)] ; 
        states = [] ; 
        for i in range(0, len(newBoxStates)):
            x,y = newBoxStates[i] ; 
            px,py = newPlayerStates[i] ; 
            if not self.isLegit(grid, (x,y)) or not self.isLegit(grid, (px,py)): continue ; 
            if self.CanReach(grid, box, player, (px,py)):
                states.append(((x,y),(px,py))) ; 
        return states ;

    # Done: test if the player can travel from src to dest while not crossing box.
    def CanReach(self, grid, box, src, dest) -> bool:
        # just use BFS
        queue = collections.deque([src]) ; 
        searched = set([src]) ; 
        while len(queue) > 0:
            cur = queue.popleft() ; 
            if cur == box: continue ; # blocked by the box.
            if cur == dest: return True ; 
            else:
                neighbors = self.graph[cur] ; 
                if neighbors is None: continue ; 
                points = list(filter(lambda point: point not in searched, neighbors)) ; 
                searched.update(points) ; 
                queue.extend(points) ; 
        return False ; 
    
    # return a heuristic that the guess distance from one point (int, int) to 
    # the target, basically the manhattan distance. 
    def GenHeuristic(self, target: (int,int), grid: [[str]], heuristic: dict):
        # use BFS
        searched = set() ; 
        queue = [(target, 0)] ;
        rowLen, colLen = len(grid), len(grid[0]) ; 
        searched.add(target) ; 
        while len(queue) > 0:
            cur = queue.pop(0) ; 
            heuristic[cur[0]] = cur[1] ; 
            cx,cy = cur[0] ;
            curDepth = cur[1] ; 
            # neighbors = [(cx+1,cy),(cx-1,cy),(cx,cy-1), (cx,cy+1)] ; 
            neighbors = self.graph[cur[0]] ; 
            if neighbors is None: continue ; 
            for point in neighbors:
                if point in searched:
                    continue ; 
                queue.append(((point[0],point[1]), cur[1]+1)) ; 
                searched.add((point[0],point[1])) ; 
        return ; 

# end of Solution
######## test ########
def readInput():
    try:
        grid = [] ; 
        row = input() ; 
        while '0' not in row :
            grid.append(list(row)) ; 
            row = input() ; 
        return grid ; 
    except: # end-of-file.
        return None ; 

def main():
    s = Solution() ; 
    while True:
        grid = readInput() ;  
        if grid is None: break ; 
        s.printGrid(grid) ; 
        print(s.minPushBox(grid)) ; 
    return ; 

if __name__ == "__main__":
    main() ; 

