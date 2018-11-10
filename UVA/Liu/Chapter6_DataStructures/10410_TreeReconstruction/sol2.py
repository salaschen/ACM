'''
Implement the solution I peeked online.
Date: 10/Nov/2018
'''

def solve(bfs, dfs):
    # record the position of each node first
    pos = dict() ; 
    son = dict() ; 
    for i in range(len(bfs)):
        pos[bfs[i]] = i ; 
        son[bfs[i]] = [] ;

    # set up the stack and search 
    parent = dict() ; 
    root = bfs[0] ; 
    cur = root ; 
    for i in range(1, len(dfs)):
        if isParent(pos, cur, dfs[i], root):
            # if the current top is the parent of the current node
            # update the parent and son dict
            # and set current top to current node
            parent[dfs[i]] = cur ; 
            son[cur].append(dfs[i]) ;
            cur = dfs[i] ;
        else:
            while not isParent(pos, cur, dfs[i], root):
                cur = parent[cur] ; 
            parent[dfs[i]] = cur ; 
            son[cur].append(dfs[i]) ;
            cur = dfs[i] ;
    return son ; 

def isParent(pos, n1, n2, root):
    # if n1 is the parent of n2
    if n1 == root or pos[n1]+1 < pos[n2]:
        return True ;
    else:
        return False ; 

def work():
    num = 0 ; 
    try:
        num = int(input()) ; 
    except:
        return 1 ; 

    bfs = [int(n) for n in input().split()] ; 
    while len(bfs) < num:
        bfs.extend([int(n) for n in input().split()]) ;

    dfs = [int(n) for n in input().split()] ; 
    while len(dfs) < num:
        dfs.extend([int(n) for n in input().split()]) ;

    son = solve(bfs, dfs) ; 
    # TODO: print out result ;
    # print(result) ; # debug
    
    for i in range(1, num+1):
        line = str(i)+':' ;
        childs = sorted(son[i]) ;
        for j in range(0, len(childs)):
            line += ' {0}'.format(childs[j]) ;
        print(line) ;

    return 0 ; 


def main():
    while work() == 0:
        continue ; 

if __name__ == "__main__":
    main() ; 
