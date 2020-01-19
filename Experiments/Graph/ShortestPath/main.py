'''
Description: The main program used to test different algorithms.
Author: Ruowei Chen
Date: 18/Jan/2020
'''

'''
Desc: the bench mark program using depth-first algorithm.
N -> number of vertice
M -> number of edges
edges -> adjacency-matrix.
src -> source
dest -> destination
Return: the shortest distance from src to dest. None if the path is non-existent.
Note: 
    1) assumption for the data: if there's no edge from i to j,
    then edges[i][j] = None.
    2) edges[i][i] = 0 ; 
'''
import heapq ; 
def dfs(N, M, edges, src, dest):
    # transfer the edges to adjacency list.
    edgeList = [[] for n in range(N)] ; 
    for i in range(N):
        for j in range(N):
            if edges[i][j] is not None and edges[i][j] != 0:
                edgeList[i].append(j) ; 

    # now use dfs to solve the problem.
    return helper(N, [src], edges, edgeList, src, dest) ; 

def helper(N, path, edges, edgeList, src, dest):
    cur = path[-1] ; 
    if cur == dest:
        return sum(list(map(lambda n: edge[path[n]][path[n+1]], \
                           [i for i in range(len(path)-1)))) ; 

    nextNodes = list(filter(lambda v: v not in path, edgeList[cur])) ; 
    temp = [] ; 
    for node in nextNodes:
        temp.append(helper(N, path+[node],  edges, edgeList, src, dest)) ; 
    return min(helper) ; 

def main():
    pass ; 