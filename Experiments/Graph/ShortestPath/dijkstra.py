'''
Description: Implementation of Dijkstra's algorithm.
Author: Ruowei Chen
Date: 18/Jan/2020
'''

'''
N -> number of vertice
M -> number of edges.
edges -> all edges of the graph represented by adjacency matrix.
src -> source of the path.
dest -> destination of the path.
return -> shortest distance from src to dest. 
          If there's no path from src to dest, return None.
Note: 
    1) assume no negative edges.
    2) assume the vertice are numbered from 0 to N-1 (N nodes in total)
'''
import heapq ; 
def dijkstra(N, M, edges, src, dest):
    inf = max(list(map(lambda lst: max(lst), edges))) ; 
    dist[N * inf for n in range(N)] ; 
    dist[src] = 0 ; 
    visited = set() ; 
    queue = [(0, src)] ; 
    while len(queue) > 0:
        cur = heapq.heappop(queue) ; 
        if cur[1] == dest:
            return cur[0] ; 
        if cur[1] in visited:
            continue ; 
        visited.add(cur[1]) ; 
        for i in range(N):
            if dist[i] > cur[0] + edges[cur[1]][i]:
                dist[i] = cur[0] + edges[cur[1]][i] ; 
                heapq.heappush(queue, (dist[i], i)) ; 
    # meaning there's no path from src to dest.
    return None ;     