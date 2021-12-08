'''
Prob: Hard - Acceptance: 109/1687
Author: Ruowei Chen
Date: 07/Dec/2021
Note:
    1) Use two kinds of edges, to-edge and from-edge.
    from-edge v1-v2 means there exist an edge from v1->v2
    to-edge v1-v2 means there exist an edge from v2->v1
    *brute-force* implementation, too slow.
    
    2) Naive Hierholzer's algorithm
'''
class Solution:
    def __init__(self):
        self.fromEdge = dict() 
        self.toEdge = dict()

    # use: Hierholzer's algorithm
    # naive implementation.
    def validArrangement(self, pairs:[[int]]) -> [[int]]:
        from collections import defaultdict, Counter
        graph = defaultdict(list)
        din, dout = Counter(), Counter() # the in-degree and out-degree count
        
        numSet = set()
        for u,v in pairs:
            dout[u] += 1
            din[v] += 1
            graph[u].append(v)
            numSet.add(u)
            numSet.add(v)

        start = pairs[0][0]
        for i in range(len(pairs)):
            u,v = pairs[i]
            if dout[u] - din[u] == 1: # this node has to be the starting node of the trail
                start = u
                break

        path, undoneSet = self.findPath(graph, start)
        # print('path:', path) # debug
        # print('undone:', undoneSet) # debug

        while len(undoneSet) > 0:
            u = undoneSet.pop()
            if len(graph[u]) == 0:
                continue
            tpath, nset = self.findPath(graph, u)
            undoneSet = undoneSet.union(nset)
            path = self.mergePath(path, tpath)

        # print('path:', path) # debug
        route = []
        for i in range(len(path)-1):
            route.append([path[i], path[i+1]])
        return route

    # [1,2,3] + [2,5,6,2] -> [1,2,5,6,2,3]
    def mergePath(self, p1:[int], p2:[int]) -> [int]:
        index = p1.index(p2[0])
        if index == len(p1)-1:
            return p1 + p2
        else:
            return p1[:index] + p2 + p1[index+1:]

    
    # find the eulerian path starting from the 'start' in this graph.
    # return the path, and the set of nodes that still has unvisited neighbors.
    def findPath(self, graph, start) -> ([int], set):
        undoneSet = set()
        cur = start
        path = []
        while len(graph[cur]) > 0:
            path.append(cur)
            temp = graph[cur].pop()
            if len(graph[cur]) > 0:
                undoneSet.add(cur)
            else:
                if cur in undoneSet:
                    undoneSet.remove(cur)
            cur = temp
        path.append(cur)
        return path, undoneSet

    # *brute-force* solution, correct but too slow.
    def validArrangement_old(self, pairs:[[int]]) -> [[int]]:
        fromSet, toSet = self.readEdges(pairs)
        print('pairs:', pairs) # debug
        
        added = set()
        front, end = [], [] # the front and end parts of the path
        # at any given time, there's at most one node at fromSet and/or one node
        # at toSet, because otherwise the pairs won't have any valid arrangement.
        # Any node in the fromSet, will appear at the rear of the path.
        # Any node in the toSet, will appear at the front of the path.
        while len(fromSet) > 0 or len(toSet) > 0:
            if len(fromSet) > 0:
                v1 = fromSet.pop()
                if v1 in added:
                    continue
                else:
                    added.add(v1)
                end.append(v1)
                # now remove all the edges into this node
                for v2 in self.toEdge[v1]:
                    self.fromEdge[v2].remove(v1)
                    if len(self.fromEdge[v2]) == 0:
                        fromSet.add(v2)

            elif len(toSet) > 0:
                v1 = toSet.pop()
                if v1 in added:
                    continue
                else:
                    added.add(v1)
                front.append(v1)
                # now remove all the edges from this node
                for v2 in self.fromEdge[v1]:
                    self.toEdge[v2].remove(v1)
                    if len(self.toEdge[v2]) == 0:
                        toSet.add(v2)
        
        # now all remaining is a cycle, or just zero. 
        mid = []
        total = set([i for i in range(len(pairs))])
        remaining = total - set(front) - set(end)
        if len(remaining) > 0:
            # use DFS on any node as the start point to find the hamilton cycle
            node = remaining.pop()
            self.dfs(node, remaining, [node])
            mid = self.mid

        # at the end
        end.reverse()
        print('front:', front)
        print('mid:', mid)
        print('end:', end)
        return list(map(lambda i: pairs[i], (front + mid + end)))

    def dfs(self, node, available: set, curPath: [int]) -> bool:
        if len(available) == 0:
            self.mid = curPath
            return True

        candidates = self.fromEdge[node]
        for v2 in candidates:
            if v2 not in available:
                continue
            if self.dfs(v2, available-set([v2]), curPath+[v2]):
                return True


    # return fromSet and toSet
    def readEdges(self, pairs: [[int]]) -> (set, set):
        # the set of nodes that still hasn't any edges.
        fromSet = set([i for i in range(len(pairs))])
        toSet = set([i for i in range(len(pairs))])

        for i in range(len(pairs)):
            self.fromEdge[i] = []
            self.toEdge[i] = []
            
        for i in range(0, len(pairs)-1):
            v1 = pairs[i]
            for j in range(i+1, len(pairs)):
                v2 = pairs[j]
                # v1 -> v2
                if v1[1] == v2[0]: 
                    self.fromEdge[i].append(j)
                    self.toEdge[j].append(i)
                    if i in fromSet:
                        fromSet.remove(i)
                    if j in toSet:
                        toSet.remove(j)
                # v2 -> v1
                if v1[0] == v2[1]: 
                    self.fromEdge[j].append(i)
                    self.toEdge[i].append(j)
                    if i in toSet:
                        toSet.remove(i)
                    if j in fromSet:
                        fromSet.remove(j)

        return (fromSet, toSet)

    
### test ###
def caseTest():
    s = Solution()
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    print(s.validArrangement(pairs))

    pairs = [[1,3],[3,2],[2,1]]
    print(s.validArrangement(pairs))

    pairs = [[1,2],[1,3],[2,1]]
    print(s.validArrangement(pairs))
    
    pairs = [[1,2]]
    print(s.validArrangement(pairs))


def largeCaseTest():
    s = Solution()
    size = 10 ** 5
    pairs = []
    for i in range(size):
        pairs.append([i, i+1])
    print(s.validArrangement(pairs))


# caseTest()
largeCaseTest()
