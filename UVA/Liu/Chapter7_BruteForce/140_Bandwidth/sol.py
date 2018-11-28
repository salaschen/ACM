'''
UVa 140 Bandwidth
Note: Decision tree + backtracking
Author: Ruowei Chen
Date: 28/Nov/2018
'''
def ReadEdges(line):
    edges = dict() ;
    for node in line.split(';'):
        v1, nodeList = node.split(':') ; 
        for n in nodeList:
            if v1 not in edges:
                edges[v1] = set() ; 
            edges[v1].add(n) ; 
            if n not in edges:
                edges[n] = set() ; 
            edges[n].add(v1) ; 
    return edges ; 

result = -1 ;
ordering = [] ; 

def search(lst, order, level, edges, curMax):
    global result ;
    global ordering ; 
    if level == len(lst):
        # check the last dist 
        last = order[level-1] ; 
        for node in edges[last]:
            curMax = max(curMax, level-1-(order.index(node))) ;
        if result == -1 or curMax < result:
            result = curMax ; 
            ordering = order[:] ; 
            # print('ordering:', ordering) ; # debug
        return ;
    else:
        for node in lst:
            if node not in order:
                # update the curMax
                tempMax = curMax ; 
                for v in edges[node]:
                    if v in order:
                        tempMax = max(tempMax, level-(order.index(v))) ; 
                if result == -1 or tempMax < result:
                    order.append(node) ;
                    search(lst, order, level+1, edges, tempMax) ; 
                    order.pop() ; 
        return ;


def work():
    line = input() ; 
    if line == '#':
        return 1; 
    edges = ReadEdges(line) ;
    lst = sorted(edges.keys()) ; 
    # print(lst) ; # debug

    global ordering ; 
    global result ; 
    ordering = [] ;
    result = -1 ; 

    for l in lst:
        search(lst,[l], 1, edges, 0) ;  

    ordering.append('->') ; 
    ordering.append(str(result)) ; 
    # print('ordering:', ordering) ; # debug

    line = ordering.pop(0) ; 
    for i in range(0, len(ordering)):
        line += ' {0}'.format(ordering[i]) ;
    print(line) ;
    return 0 ;

def main():
    while True:
        if work() != 0:
            break ; 
    return ;

if __name__ == "__main__":
    main() ;
