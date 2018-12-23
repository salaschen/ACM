'''
UVa 11212 Editing a Book
Date: 17/Dec/2018
Author: Ruowei Chen
Note: Simple BFS
Update 1: change from list representation to string representation.
Update 2: change heuristic to double function
Update 3: change heuristic to number of numbers with a *wrong* after number
'''
import heapq ;
import math ;
def work(Case):
    n = int(input()) ;
    if n == 0:
        return 1 ;
    original = [num for num in input().split()] ;
    start = "" ;
    for i in range(0, len(original)):
        start += original[i] ; 
    result = search(start, n) ; 
    print("Case {0}: {1}".format(Case, result)) ;
    return 0 ;

lright = [str(n+1) for n in range(0, 9)] ;
right = dict(); 
for i in range(1, len(lright)):
    right[str(i)] = lright[i] ; 
right['9'] = None ;

class Node:
    def __init__(self, ordering, dist):
        self.ordering = ordering; 
        self.dist = dist ; 
        self.hdist = self.heuristic(); 
    
    def __lt__(self, other):
        return self.dist+self.hdist < other.dist+other.hdist ;

    def heuristic(self):
        result = 0 ; 
        global right ;
        for i in range(0, 8):
            if self.ordering[i+1] != right[self.ordering[i]]:
                result += 1 ;
        if self.ordering[8] != '9':
            result += 1 ; 
        return result / 3 ; 

    def __str__(self):
        return self.ordering+', dist='+str(self.dist)+', hdist='+str(self.hdist) ;

def BFS(goal, n, parent = None):
    result = dict() ; 
    queue = [(goal, 0)] ;
    seen = set() ;  seen.add(goal) ;
    numExpand = 0 ; 
    numChecked = 0 ;
    while len(queue) > 0:
        cur = queue.pop(0) ;
        numExpand += 1 ;
        for child in expand(cur[0], n):
            numChecked += 1 ; 
            if child not in seen:
                seen.add(child) ; 
                result[child] = cur[1]+1 ;
                queue.append((child, cur[1]+1)) ; 
                # for debug
                if parent is not None:
                    parent[child] = cur[0] ; 
        continue ; 
    print('numExpanded={0}, numChecked={1}'.format(numExpand, numChecked)) ; # debug
    return result ; 

def TestBFS():
    goal = '123456789' ;
    original = '539284167' ;
    parent = dict() ; 
    result = BFS(goal, len(goal), parent) ;
    print('original:', original, ' ',  result[original]) ;
    cur = original ;
    while cur in parent:
        print(cur) ; 
        cur = parent[cur] ; 
    print('goal:', cur) ;
    return ;

def search(original, n):
    original = Node(original, 0) ;
    queue = [] ; 
    heapq.heappush(queue, original) ;
    goal = "" ; 
    for i in range(1, n+1):
        goal += str(i) ;
    seen = set() ;
    seen.add(original.ordering) ; 
    # parent = dict();  # debug
    # parent[original.ordering] = None ;  # debug
    while len(queue) > 0:
        cur = heapq.heappop(queue) ; 
        if cur.ordering == goal:
            result = cur.dist ;
            cur = cur.ordering ;
            # while cur is not None:
            #    print(cur) ;  # debug
            #    cur = parent[cur] ; 
            return result ; 
        else:
            children = expand(cur.ordering, n) ;
            for successor in children:
                if successor not in seen:
                    # parent[successor] = cur.ordering ; # debug
                    node = Node(successor, cur.dist+1) ;
                    seen.add(successor) ; 
                    heapq.heappush(queue, node); 
    return None ;

def expand(original, n):
    '''
    original: string
    n: int
    return a list of new orderings(string) 
    '''
    result = [] ; 
    #seen = set() ;
    #seen.add(original) ; 
    for l in range(1, n):
        # l is the length of the string to be moved.
        for st in range(0, n-1):
            # st is the starting index 
            if n-st < l:
                break; 
            mov = original[st:st+l] ; 
            rest = original[:st]+original[st+l:] ; 
            for ins in range(st+1, n):
                # ins is the insert position
                # it doesn't insert in front, only backward, so start from st+1
                temp = rest[:ins]+mov+rest[ins:] ; 
                # if temp not in seen:
                result.append(temp) ; 
                #    seen.add(temp) ; 
    return result ; 

def TestExpand():
    original = '34512' ;
    print(expand(original, len(original))) ; 
    return ;
        

def solve(): 
    Case = 1
    while work(Case) == 0:
        Case += 1 ; 
        continue ; 
    return ;

def main():
    solve() ; 
    # TestBFS() ; 
    # TestExpand() ;
    return ; 

if __name__ == "__main__":
    main() ; 
