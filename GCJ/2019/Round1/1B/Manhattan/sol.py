'''
GCJ - 1B Manhattan
Author: Ruowei Chen
Date: 04/May/2019 - May the force be with you.
Note: 
    1) The Brute-Force ish way failed first, but I can think of a
good way to solve it.
'''

def work(Case):
    # readinput()
    P, Q = [int(n) for n in input().split()] ; 
    W = [] ; 
    N = [] ; 
    S = [] ;
    E = [] ;
    for i in range(P):
        x,y,d = input().split() ; 
        x = int(x) ; 
        y = int(y) ; 
        if d == 'N':
            N.append((x,y,d)) ; 
        elif d == 'S':
            S.append((x,y,d)) ; 
        elif d == 'E':
            E.append((x,y,d)) ; 
        else:
            W.append((x,y,d)) ; 
    
    N = sorted(N,key=lambda n: n[1]) ; 
    S = sorted(S,key=lambda n: n[1], reverse=True) ; 
    W = sorted(W,key=lambda n: n[0], reverse=True) ;
    E = sorted(E,key=lambda n: n[0]) ; 

    # print(N) ; print(S) ; print(W) ; print(E) ; # debug

    # initialize row and columns
    row = dict() ; 
    col = dict() ; 
    for i in range(0, Q+1):
        row[i] = 0 ; 
        col[i] = 0 ; 

    # process each direction. 
    # north
    if len(N) > 0:
        for i in range(0, len(N)-1):
            cur = N[i] ;
            neXt = N[i+1] ; 
            for j in range(cur[1]+1, neXt[1]+1):
                row[j] += i+1 ; 
        # the last row
        for j in range(N[len(N)-1][1]+1, Q+1):
            row[j] += len(N) ; 
    
    # print('row:', row) ; # debug

    # south
    if len(S) > 0:
        for i in range(0, len(S)-1):
            cur = S[i] ; 
            neXt = S[i+1] ; 
            for j in range(neXt[1], cur[1]):
                row[j] += i+1 ; 
        for j in range(0, S[len(S)-1][1]):
            row[j] += len(S) ; 
    
    # East
    if len(E) > 0:
        for i in range(0, len(E)-1):
            cur = E[i] ; 
            neXt = E[i+1] ; 
            for j in range(cur[0]+1, neXt[0]+1):
                col[j] += i+1 ;
        # the last col
        for j in range(E[len(E)-1][0]+1, Q+1):
            col[j] += len(E) ; 
    
    # west
    if len(W) > 0:
        for i in range(0, len(W)-1):
            cur = W[i] ; 
            neXt = W[i+1] ; 
            for j in range(neXt[0], cur[0]):
                col[j] += i+1 ; 
        # last col
        for j in range(0, W[len(W)-1][0]):
            col[j] += len(W) ; 

    # print('row:', row) ; # debug
    # print('col:', col) ; # debug
        
    # find the most rows and cols.
    maxRowValue = max(list(row.values())) ;
    r = -1 ;
    for i in range(0, Q+1):
        if row[i] == maxRowValue:
            r = i ; 
            break ; 
    maxColValue = max(list(col.values())) ; 
    c = -1 ; 
    for i in range(0, Q+1):
        if col[i] == maxColValue:
            c = i ; 
            break ; 
    
    print('Case #{0}: {1} {2}'.format(Case, c, r)) ; 
    
    return ;

def solve():
    T = int(input()) ; 
    for i in range(1, T+1):
        work(i) ;
    return ;

def main():
    solve() ; 

if __name__ == "__main__":
    main() ; 
