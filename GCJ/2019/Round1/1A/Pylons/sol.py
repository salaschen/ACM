'''
GCJ 1A: Pylons
Author: Ruowei Chen
Note: 
    1) Brute-Force
    2) 22/Apr/2019 - Try to implement the stochastic solution as suggested by post-match analysis.

'''
import random
import time

# point is a number
# return (rowNumber, col number) all index from 1
def getRC(point, R, C):
    p = point - 1 ; 
    r = (p//C) +1 ; 
    c = (point%C) ;
    if c == 0:
        c += C ; 
    return (r, c) ; 

# return a tuple of (edge, neighbors)
# edge is a map: point -> List[points]
# neighbors is map: point -> List[points]
# point b is point a's neighbor if b and a *violates* the constraints.
def genEdges(points, R, C):
    result = dict() ; 
    neighbors = dict() ; 
    # set up the map
    for p in points:
        result[p] = [] ;
        neighbors[p] = [] ; 
    # foreach point, find connection
    for i in range(0, len(points)-1):
        src = points[i] ; 
        sr, sc = getRC(src, R, C) ; 
        for j in range(i+1, len(points)):
            target = points[j] ; 
            tr, tc = getRC(target, R, C) ; 
            violate = False ; 
            if sr == tr or sc == tc:
                violate = True ; 
            if tr-tc == sr-sc:
                violate = True ; 
            if tr+tc == sr+sc:
                violate = True ; 

            if not violate:
                result[src].append(target) ; 
                result[target].append(src) ; 
            else:
                neighbors[src].append(target) ; 
                neighbors[target].append(src) ; 
    return (result, neighbors) ;

# return whether or not a path can be found
# if True, then the path will be stored in path.
# points are the points that are left, will be in sorted order.
# mem is memoization, to memory if the current state is possible or
# not.
def findPath(path, points, edges, mem):
    if len(points) == 0:
        return True; 
    src = path[-1] ; 
    # check if this state has been tried before
    rep = str(src) + ',' + str(points) ; 
    # print(rep) ; # debug
    if rep in mem:
        return False ; 

    ePoints = edges[src] ; 
    for p in ePoints:
        if p not in points:
            continue ; 
        cpoints = points.copy() ; 
        path.append(p) ; 
        cpoints.remove(p) ; 
        result = findPath(path, cpoints, edges, mem) ;
        # path is found
        if result:
            return True ;
        else:
            path.pop() ; 
    
    mem[rep] = False ; 
    return False ; 

def solveSmall(Case, R, C, points, edges):
    mem = dict() ; 
    for p in points:
        cpoints = points.copy() ; 
        cpoints.remove(p) ; 
        path = [p] ; 
        result = findPath(path, cpoints, edges, mem) ; 
        if result:
            print('Case #{0}: POSSIBLE'.format(Case)) ; 
            # print path
            for p in path:
                r,c = getRC(p, R, C) ; 
                print('{0} {1}'.format(r, c)) ; 
            return ;

    # if no path is possible.
    print('Case #{0}: IMPOSSIBLE'.format(Case)) ; 
    return ; 
 
# return a boolean
def hasHamiltonCycle(points, edges):
    n = len(points) ; 
    for i in range(0, len(points)-1):
        p1 = points[i] ;
        dg1 = len(edges[p1]) ; # degree
        for j in range(i+1, len(points)):
            p2 = points[j] ;                
            if p2 in edges[p1]: # p1 and p2 are adjacent, ignore.
                continue ; 
            else:
                dg2 = len(edges[p2]) ; 
                if dg1 + dg2 < n:
                    return False ; 
    return True ; 

# return True if path is found, False, otherwise.
def randomFind(R, C, points, edges, path):
    start = random.choice(points) ; 
    path.append(start) ; 
    # repeatedly find a point in a random fashion.
    n = R * C ; 
    pathLen = 1 ; 
    while pathLen < n:
        nextPoints = edges[start] ;
        nextPoints = list(filter(lambda p: p not in path, nextPoints)) ; 
        if len(nextPoints) == 0:
            return False ; 
        start = random.choice(nextPoints) ; 
        path.append(start) ;
        pathLen += 1 ; 
    return True ; 

# use greedy algorithm to solve the problem
# ah, it's neighbors not degrees. 
def greedy(Case, R, C, points, edges, neighbors):
    if not hasHamiltonCycle(points, edges):
        print('Case #{0}: IMPOSSIBLE'.format(Case)) ; 
        return ;
    else:
        # find the point which has the most unvisited 'neighbors'
        start = None ; dg = 0 ; 
        for p in points:
            print('{0}, num={1}'.format(p, len(neighbors[p]))) ; # debug
            if len(neighbors[p]) > dg:
                dg = len(neighbors[p]) ;
                start = p ; 

        path = [start] ;
        while len(path) < len(points):
            neibors = edges[start] ;
            neXt = None ; dg = 0 ; 
            for n in neibors:
                if n in path: continue ; 
                num = len(list(filter(lambda p: p not in path, neighbors[n]))) ;
                if num > dg:
                    dg = num; 
                    neXt = n ; 
            start = neXt ; 

            if start is None:
                # print('path:', path) ; # debug
                print('R={0},C={1},path length={2}'.format(R,C,len(path))) ; # debug
                print('Case #{0}: IMPOSSIBLE'.format(Case)) ; 
                return ;

            path.append(start) ; 
            continue ; 

        # print out the result
        print('Case #{0}: POSSIBLE'.format(Case)) ; 
        for p in path:
            r,c = getRC(p, R, C) ; 
            print('{0} {1}'.format(r, c)) ; 
    return ;

def solveBig(Case, R, C, points, edges):
    random.seed(1) ;
    # Use ore's theorem to decide whether the graph has a hamilton cycle.
    # if not hasHamiltonCycle(points, edges):
    #     print('Case #{0}: IMPOSSIBLE'.format(Case)) ; 
    #     return ;
    path = [] ; 
    Try =  0;
    while not randomFind(R, C, points, edges, path) and Try < 1000:
        path = [] ; 
        Try += 1 ;
        continue ; 
    print('Case #{0}: POSSIBLE'.format(Case)) ; 
    for p in path:
        r,c = getRC(p, R, C) ; 
        print('{0} {1}'.format(r, c)) ; 
    return ;

    print('Case #{0}: IMPOSSIBLE'.format(Case)) ; 

    return ;

def work(Case):
    R, C = [int(n) for n in input().split()] ; 
    points = [i for i in range(1, R*C+1)] ; 
    edges, neighbors = genEdges(points, R, C) ; 
    # print(edges) ;  # debug
    if R <= 5 and C <= 5:
        solveSmall(Case, R, C, points, edges) ; 
    else:
        solveBig(Case, R, C, points, edges) ;
        # greedy(Case, R, C, points, edges, neighbors) ; 
    return ;

def solve():
    T = int(input()) ; 
    for i in range(1, T+1):
        work(i) ; 

def test():
    R = 3 ; C = 4 ;
    for p in range(1, 13):
        print(p) ; 
        print(getRC(p, R, C)) ; 

def main():
    solve() ; 
    # test() ;

if __name__ == "__main__":
    main() ;
