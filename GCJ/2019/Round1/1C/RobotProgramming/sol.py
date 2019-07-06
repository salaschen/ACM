'''
Robot Programming
Author: Ruowei Chen
Date: 04/May/2019
Note: 
    1) greedy + bfs
'''
def winMove(move):
    if move == 'R':
        return 'P' ;
    if move == 'S':
        return 'R' ; 
    else:
        return 'S' ; 

def bfs(path, robots, level):
    if len(robots) == 0:
        return True ; 

    avail = set() ; 
    for r in robots:
        curMove = level % len(r) ; 
        avail.add(r[curMove]) ; 

    # see how many moves are available.
    if len(avail) == 1:
        roMove = (list(avail))[0] ;
        path.append(winMove(roMove)) ; 
        return True ; # ok
    if len(avail) == 3:
        return False ; # cannot make any moves
    
    # now we can select the move.
    avail = list(avail) ; 
    m1 = avail[0] ;
    m2 = avail[1] ; 
    if m1 == winMove(m2):
        move = m1 ; 
    else:
        move = m2 ; 
    path.append(move) ;    
    rcopy = [] ; 
    for r in robots:
        curMove = level % len(r) ; 
        if r[curMove] == move:
            rcopy.append(r) ; 
    
    return bfs(path, rcopy, level+1) ; 


def work(Case):
    A = int(input()) ; 
    robots = [] ; 
    for i in range(A):
        robots.append(input()) ; 

    # print(robots) ;  # debug
    path = [] ;
    result = bfs(path, robots, 0) ; 

    if result:
        moves = '' ;
        for m in path:
            moves += m ; 
        print('Case #{0}: {1}'.format(Case, moves)) ; 
    else:
        print('Case #{0}: IMPOSSIBLE'.format(Case)) ; 

    return ;

def solve():
    T = int(input()) ; 
    for i in range(T):
        work(i+1) ; 

def main():
    solve() ; 

if __name__ == "__main__":
    main() ; 
