'''
Leetcode 417 - Pacific Atlantic Water Flow
Author: Ruowei Chen
Date: 17/Mar/2019
'''
class Solution:
    def pacificAtlantic(self, matrix):
        # only from equal or lower grid has an directed edge
        # to another grid. for example 3->3, or 3->5, but not 5->3.
        if len(matrix) == 0:
            return [] ; 

        edges = self.prepareEdges(matrix) ; 
        
        # find all the points that can flow to Pacific
        r,c = len(matrix), len(matrix[0]) ; 
        pacifics = set([(0, x) for x in range(0, c)]) ; 
        pacifics = pacifics.union(set([(x,0) for x in range(0, r)])) ; 
        pacifics = self.ConnectComponents(edges, pacifics) ; 
        
        atlantic = set([(r-1,x) for x in range(0, c)]) ; 
        atlantic = atlantic.union(set([(x, c-1) for x in range(0, r)])) ;
        atlantic = self.ConnectComponents(edges, atlantic) ; 
        
        result = list(pacifics.intersection(atlantic)) ; 
        result = list(map(lambda n: [n[0], n[1]], result)) ; 
        print(result) ; # debug
        return result; 
    
    def ConnectComponents(self, edges, pointSet):
        queue = list(pointSet) ; 
        searched = set() ; 
        while len(queue) > 0:
            cur = queue.pop() ; 
            searched.add(cur) ; 
            for point in edges[cur]:
                if point not in searched:
                    queue.append(point) ; 
        return searched ; 


    def prepareEdges(self, matrix):
        result = dict() ; 
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                result[(i,j)] = self.getEdges((i,j), matrix) ; 
        return result ; 

    def getEdges(self, coord, matrix):
        x,y = coord ; 
        r,c = len(matrix), len(matrix[0]) ;
        points = [(x+1, y), (x-1,y), (x,y+1),(x,y-1)] ; 
        points = list(filter(\
                lambda p: p[0] >= 0 and p[0] < r and \
                p[1] >= 0 and p[1] < c, points)) ; 
        result = [] ;
        for p in points:
            if matrix[x][y] <= matrix[p[0]][p[1]]:
                result.append(p) ; 
        return result ; 

def readInput():
    matrix = [] ;
    while True:
        try:
            row = [int(n) for n in input().split()] ; 
            matrix.append(row) ; 
        except EOFError:
            break ; 
    return matrix ; 

def work():
    matrix = readInput() ; 
    s = Solution() ; 
    s.pacificAtlantic(matrix) ; 

def main():
    work() ; 

if __name__ == "__main__":
    main() ; 
