'''
UVa 1601 The Morning after Halloween, Japan 2007
Date: 11/Dec/2018
Note: Improved BFS
'''
import heapq ; 

def printMatrix(matrix, state):
    for i in range(len(matrix)):
        line = "" ; 
        row = matrix[i] ; 
        for j in range(len(row)):
            if (i,j) in state:
                line += chr(ord('a')+state.index((i,j))) ; 
            else:
                line += row[j] ;
        print(line) ; 
    return ; 

def ReadEdges(matrix, w, h):
    edges = dict() ; 
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '#':
                edges[str((i,j))] = [] ; # empty
            else:
                temp = [(i,j), (i+1,j), (i-1, j), (i,j+1), (i,j-1)] ;
                temp = list(filter(lambda pair: \
                        pair[0] >= 0 and pair[0] < h and pair[1] >= 0 and pair[1] < w \
                        and matrix[pair[0]][pair[1]] != '#', temp)) ; 
                edges[str((i,j))] = temp ; 
    return edges ; 

def GoalDistance(edges, goal):
    '''
    Return a dictionary that store the shortest distance from the goal states
    to any point on the map.
    for example, goal is [(1,2),(3,4),(5,6)]. Then the result has information like
    result[(1,2)][(1,6)]=8, result[(3,4)][(2,4)]=7, result[(5,6)][(5,3)]=2,etc.
    But result[(1,3)]=undefined, because (1,3) is not in the goal states.
    '''
    result = dict() ;
    for gstate in goal:
        result[str(gstate)] = BFSDist(edges, gstate) ;    
    return result ;

def BFSDist(edges, gstate):
    result = dict() ; 
    result[str(gstate)] = 0 ;
    queue = [gstate] ; 
    while len(queue) > 0:
        cur = queue.pop(0) ; 
        curDist = result[str(cur)] ; 
        for neXt in edges[str(cur)]:
            if str(neXt) not in result: 
                result[str(neXt)] = curDist + 1 ;
                queue.append(neXt) ; 
    return result ;

def work():
    w,h,n = [int(x) for x in input().split()] ;
    if w == 0 and h == 0 and n == 0:
        return 1 ;

    initial, goal, matrix = readInput(w,h,n) ;
    Edges = ReadEdges(matrix, w, h) ; 

    gdist = GoalDistance(Edges, goal); 

    dist = search(initial, goal, Edges, matrix, w, h, gdist) ; 
    print(dist) ; 

    return 0 ;

class Node:
    def __init__(self, state, dist, dm):
        self.state = state ;
        self.dist = dist ; 
        self.dm = dist+dm;

    def __lt__(self, other):
        return self.dm < (other.dm) ; 

    def __str__(self):
        return "[state]: {0}, f(n)={1}".format(str(self.state), self.dm) ;  

def search(initial, goal, edges, matrix, w, h, gdist):
    queue = [Node(initial, 0, manhattan(initial, goal, gdist))] ;
    seen = set() ;
    seen.add(str(initial)); 
    result = -1 ; 
    # print('initial:', str(initial), ', goal:', goal) ; # debug
    while len(queue) > 0:
        cur = heapq.heappop(queue) ; 
        # print("expanding" + str(cur)) ; # debug
        if IsGoal(cur.state, goal):
            # if result < 0 or result > cur.dist:
            result = cur.dist ;
            return result ; 

        nextStates = GetNextPoints(cur.state, edges, matrix, w, h) ;
        for state in nextStates:
            if str(state) not in seen: 
                node = Node(state, cur.dist+1, manhattan(state, goal, gdist)) ; 
                heapq.heappush(queue, node) ; 
                seen.add(str(state))  ;
    return result;

def manhattan(state, goal, gdist):
    result = 0 ; 
    for i in range(len(state)):
        sp = state[i] ; 
        gp = goal[i] ; 
        temp = gdist[str(goal[i])][str(state[i])] ; 
        # result += abs(sp[0]-gp[0]) + abs(sp[1]-gp[1]) ; 
        result += temp ; 
    return result/3 ; 

def IsGoal(state, goal):
    for i in range(len(state)):
        if state[i] != goal[i]:
            return False ; 
    return True;  

def GetNextPoints(state, edges, matrix, w, h):
    # state is a list of positions of ghosts.
    nextStates = list(map(lambda pos: GetNextPos(pos, edges, matrix, w,h),state)) ;

    if len(state) == 1:
        result = CrossJoin(nextStates[0], []) ;
    elif len(state) == 2:
        result = CrossJoin(nextStates[0], nextStates[1]); 
    elif len(state) == 3:
        result = CrossJoin(nextStates[0], nextStates[1]); 
        result = CrossJoin(result, nextStates[2]) ; 

    # filter out the states that ghost are on the same slot
    result = list(filter(lambda ghosts: not OnSameSlot(ghosts), result)) ;
    result = list(filter(lambda ghosts: not HasSwapPos(state, ghosts), result)) ; 
    result = list(filter(lambda ghosts: ghosts != state, result)); 

    return result; 

def HasSwapPos(initial, state):
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if initial[i] == state[j] and initial[j] == state[i]:
                return True ; 
    return False ; 

def OnSameSlot(ghosts):
    # ghosts is a list of pos
    for i in range(len(ghosts)):
        for j in range(i+1, len(ghosts)):
            if ghosts[i] == ghosts[j]:
                return True ; 
    return False ; 

def CrossJoin(lst1, lst2):
    # list is 
    result = [] ;
    if len(lst2) == 0:
        for elem1 in lst1:
            result.append([elem1]) ;
    else:
        for elem1 in lst1:
            for elem2 in lst2:
                if type(elem1) == type([]):
                    elem = elem1[:];
                    elem.append(elem2) ; 
                    result.append(elem);  
                else:
                    result.append([elem1, elem2]) ;
    return result ; 

def GetNextPos(pos,edges,matrix,w,h):
    # pos is (x,y)
    # return a list of pos that's not out of bound and not '#'
    x,y = pos ; 
    result = edges[str(pos)] ;
    return result; 

def readInput(w,h,n):
    matrix = [] ; 
    initial = [(0,0) for x in range(n)] ; # from A to C
    goal = [(0,0) for x in range(n)] ; 
    for i in range(h):
        line = input() ; 
        row = [] ; 
        for j in range(len(line)):
            c = line[j] ; 
            if c == '#' or c == ' ':
                row.append(c) ; 
            elif c.isupper(): # goal
                code = ord(c) - ord('A') ; 
                goal[code] = (i, j) ; 
                row.append(' ') ; 
            else: # initial
                code = ord(c) - ord('a') ; 
                initial[code] = (i,j) ; 
                row.append(' ') ; 
        matrix.append(row) ;
    return (initial, goal, matrix) ;

def solve():
    while work() == 0:
        continue ; 
    return ;
    
def main():
    solve() ; 
    return ; 

if __name__ == "__main__":
    main() ; 
