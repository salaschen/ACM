'''
UVa 10603 Fill
Date: 05/Dec/2018
'''
import heapq ;
class Node:
    def __init__(self, state, water):
        self.state = state ; 
        self.water = water ; 

    def __lt__(self, other):
        return self.water < other.water ; 

    def __gt__(self, other):
        return self.water > other.water ; 

    def __eq__(self, other):
        return self.water == other.water ; 
    
    def __str__(self):
        return '[node]:' + str(self.state) + ", water=" + str(self.water) ;

    def Transitions(self, capacity):
        '''
        capacity is a triple
        return a list of nodes that can be transitioned from the current node
        ''' 
        result = [] ; 
        for i in range(3):
            for j in range(3):
                if i != j:
                    temp = self.FromTo(i,j,capacity) ; 
                    if temp[1] != 0:
                        result.append(Node(temp[0], temp[1]+self.water)) ; 
        return result ; 

    def FromTo(self, fr, to, capacity):
        # fr: 0 to 2 ; to: 0 to 2
        # return a new state
        fromJug = self.state[fr] ; 
        toJug = self.state[to] ; 
        unchanged = list(filter(lambda n: n not in [fr,to], [n for n in range(3)]))[0]  ; 

        fromJugCap = capacity[fr] ; 
        toJugCap = capacity[to] ; 

        water = 0 ;
        if toJugCap-toJug >= fromJug:
            toJug = toJug+fromJug ; 
            water = fromJug ;
            fromJug = 0 ; 
        else:
            fromJug = fromJug-(toJugCap-toJug) ; 
            water = (toJugCap-toJug) ; 
            toJug = toJugCap ; 
            
        newState = [0 for n in range(3)] ; 
        newState[fr] = fromJug ; 
        newState[to] = toJug ; 
        newState[unchanged] = self.state[unchanged] ; 
        return (newState, water) ; 

def testNode():
    node1 = Node([1,2,3], 20) ; 
    print(node1.FromTo(0, 1, [3, 4, 5]), 'expect: [0,3,3]') ; 
    print(node1.FromTo(1, 0, [2, 4, 3]), 'expect: [2,1,3]') ; 
    print(node1.FromTo(2, 0, [1,2,5]),   'expect: [1,2,3]') ; 
    print(node1.FromTo(1, 2, [1,2,6]),   'expect: [1,0,5]') ; 

    # test transitions
    print('*' * 25) ; 
    nodes = node1.Transitions([3,4,5]) ; 
    print(node1) ; 
    for node in nodes:
        print(node) ; 

    return ; 


def work():
    a,b,c,d = [int(n) for n in input().split()] ;
    queue = [] ; 
    capacity = [a,b,c] ; 
    node = Node([0,0,c], 0) ; 
    queue.append(node) ; 

    d0 = 0 ; 
    water = 0 ;
    searched = dict() ;
    searched[str(node.state)] = node.water ; 
    while len(queue) > 0:
        node = heapq.heappop(queue) ; 
        for value in node.state:
            if value == d:
                print('{0} {1}'.format(node.water, value)) ; 
                return ; 
            elif value > d0 and value < d:
                d0 = value ; 
                water = node.water ; 
        if str(node.state) not in searched or \
           searched[str(node.state)] > node.water:
            searched[str(node.state)] = node.water ; 

        transitions = node.Transitions(capacity) ; 
        for node in transitions:
            if str(node.state) not in searched or \
                    searched[str(node.state)] > node.water:
                heapq.heappush(queue, node) ;
        continue ; 
    print('{0} {1}'.format(water, d0)) ; 
    return ;

def solve():
    n = int(input()) ; 
    for i in range(n):
        work() ;
    return ;

def main():
    # testNode() ;
    solve() ; 
    return ; 

if __name__ == "__main__":
    main() ; 
