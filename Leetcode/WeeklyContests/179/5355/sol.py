class Solution:
    def frogPosition(self, n: int, edges: [[int]], t: int, target: int) -> float:
        if len(edges) == 0 or len(edges[0]) == 0:
            if target == 1:
                return 1.0
            else:
                return 0.0

        # do a mapping on the edges
        edgeMap = dict()
        for edge in edges:
            u,v = edge
            if u not in edgeMap:
                edgeMap[u] = []
            edgeMap[u].append(v)
            if v not in edgeMap:
                edgeMap[v] = []
            edgeMap[v].append(u)

        # print(edgeMap) # debug
        result = [0.0]
        self.dfs([1], edgeMap, 0, t, target, 1.0, result) ; 
        return sum(result)
    
    def dfs(self, visited: [int], edgeMap, depth, t, target, prob, result):
        if depth > t: # expires
            return 

        last = visited[-1]
        # found the target
        if last == target:
            if depth == t: # exact match
                result.append(prob)
                return 
            elif depth < t:
                
                child = edgeMap[last]
                good = True
                for c in child:
                    if c not in visited:
                        good = False
                        break
                if good:
                    result.append(prob)
                return 

        childs = edgeMap[last]
        childs = list(filter(lambda c: c not in visited, childs))
        if len(childs) > 0:
            cprob = prob/len(childs)*1.0
            for c in childs:
                self.dfs(visited+[c], edgeMap, depth+1, t, target, cprob, result)
        return 

#### test #####
s = Solution()
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 1
target = 7
print(s.frogPosition(n, edges, t, target))

n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 20
target = 6
print(s.frogPosition(n, edges, t, target))

n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
print(s.frogPosition(n, edges, t, target))

n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 1
print(s.frogPosition(n, edges, t, target))

n = 1
edges = [[]]
t = 1
target = 1
print(s.frogPosition(n, edges, t, target))

