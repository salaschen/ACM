'''
Prob: Milk Pumping
Author: Ruowei Chen
Date: 16/Dec/2019
Note: 
    1) Use DFS to memorize the cost and flow rate of the path.
    2) DFS solution TLE for cases #4 and beyond.
    3) Implement the official solution.
'''
import heapq ; 

def dfs(N, M, path, flow, cost, curFlow, curCost):
    cur = path[-1] ; 
    if cur == N and curCost != 0:
        return curFlow/curCost;

    points = [] ; 
    for i in range(N+1):
        if flow[cur][i] > 0 and i not in path: # an edge exist
            points.append(i) ; 
    
    result = None ; 

    for point in points:
        f = flow[cur][point] ; 
        c = cost[cur][point] ; 
        mincurFlow = f if (curFlow == 0 or f < curFlow) else curFlow ; 
        temp = dfs(N,M, path+[point],flow, cost, mincurFlow, c+curCost) ; 
        if temp is not None and (result is None or temp > result):
            result = temp ; 

    return result; 


def work(N,M,flow,cost):
    path = [] ; 
    path.append(1) ; 
    result = dfs(N, M, path, flow, cost, 0, 0) ; 
    return result ; 

# only use the pipes that has a flow equal or exceed the flimit
# return the cost of the path from 1 to N.
def dijkstra(N, flow, cost, flimit):
    dist = [1000*1001 for x in range(N+1)] ; 
    dist[1] = 0 ; 
    cur, Next = 1, None; 
    visited = set(); 
    queue = [(0,1)] ; 

    result = -1; 
    while len(queue) > 0:
        cur = heapq.heappop(queue) ; 
        if cur[1] == N:
            result = dist[cur[1]] ; 
            break ;

        # when the town has already been visited before. 
        if cur[1] in visited:
            continue ; 

        visited.add(cur[1]) ; 
        # reduce all the adjacent distances.
        for (c, v2) in cost[cur[1]]:
            if flow[v2][cur[1]] >= flimit and dist[v2] > cur[0] + c:
                dist[v2] = cur[0] + c ; 
                heapq.heappush(queue, (dist[v2], v2)) ; 
        '''    
        for i in range(1, N+1):
            if i not in visited:
                if flow[cur][i] >= flimit:
                    dist[i] = min(dist[i], dist[cur]+cost[cur][i]) ; 
                if Next is None or dist[i] < dist[Next]:
                    Next = i ; 
        cur, Next = Next, None ; 
        '''
    return result; 

# the official solution implementation
# return the maximum flow/cost ratio. 
def work2(N,M,flow,cost):
    # generate the flowSet.
    flows = set() ; 
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if flow[i][j] > 0:
                flows.add(flow[i][j]) ; 

    flows = sorted(list(flows)) ;
    result = -1 ; 
    for f in flows:
        curCost = dijkstra(N, flow, cost, f) ; 
        # print('curCost={0}'.format(curCost)) ; # debug
        # when a path cannot be found, exit the loop.
        if curCost < 0:
            break ;
        result = max(result, f/curCost) ; 
    return result ; 

def main():
    fin = open('pump.in') ; 
    N, M = [int(x) for x in fin.readline().split()] ; 
    flow = [[-1 for x in range(N+1)] for y in range(N+1)] ;
    cost = dict([(x, []) for x in range(1, N+1)]); 
    for i in range(M):
        v1,v2,c,f = [int(x) for x in fin.readline().split()] ; 
        flow[v1][v2] = f ; flow[v2][v1] = f ; 
        cost[v1].append((c, v2)) ; 
        cost[v2].append((c, v1)) ;
        # cost[v1][v2] = c ; cost[v2][v1] = c ;

    # result = work(N,M,flow, cost) ; 
    r2 = work2(N,M,flow,cost) ; 
    fout = open('pump.out', 'w') ; 
    # result = int(10**6 * result) ; 
    r2 = int(10**6 * r2) ; 
    # print('result={0},r2={1}'.format(result, r2)) ; # debug
    print(r2) ; # debug
    fout.write('{0}\n'.format(r2)) ; 
    return ; 


if __name__ == "__main__":
    main() ;


