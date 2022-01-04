'''
Prob: 2127 - Hard (weekly contest)
Author: Ruowei Chen
Date: 04/Jan/2022
'''
class Solution:
    def maximumInvitations(self, favorite: [int]) -> int:
        nodes = set(favorite)
        searched = set()

        edges = self.readEdges(favorite)

        # phase 1: find all the *twins* trees and combine their total lengths
        result = 0
        twins = self.findTwins(favorite)
        for u, v in twins:
            temp = self.searchTwin([u,v], edges, searched)
            # print(searched)
            result += temp

        # phase 2: search for cycles in the remaining nodes
        remaining = nodes-searched
        while len(remaining) > 0:
            cur = remaining.pop()
            temp = self.findCycle(cur, edges, searched, set())
            result = max(temp, result)
            remaining = remaining - searched

        return result;

    # return 0 if cycle is not found, otherwise return the length of the cycle.
    def findCycle(self, node:int, edges:dict, searched:set , path: set) -> int:
        if node in path:
            return len(path)

        searched.add(node)
        path.add(node)
        for v in edges[node]:
            temp = self.findCycle(v, edges, searched, path)
            if temp > 0:
                return temp
            else:
                path.remove(v)
        
        return 0
        

    def readEdges(self, favorite: [int]) -> dict:
        edges = dict()
        for i in range(len(favorite)):
            u, v = i, favorite[i]
            if u not in edges:
                edges[u] = []
            if v not in edges:
                edges[v] = []
            edges[v].append(u)
        return edges

    # search the twin tree and find out the tree length
    # there's no cycle in the twin tree
    def searchTwin(self, twin: [int], edges: dict, searched: set) -> int:
        u, v = twin
        nodes = edges[u]
        nodes.remove(v)
        result = 0
        if len(nodes) > 0:
            result = max(list(map(lambda node: self.dfs(node, edges, searched), nodes)))

        # print(u, result)
        
        nodes = edges[v]
        nodes.remove(u)
        if len(nodes) > 0:
            result += max(list(map(lambda node: self.dfs(node, edges, searched), nodes)))

        # print(v, result)
        result += 2
        searched.add(u)
        searched.add(v)
        return result 

    def dfs(self, node: int, edges: dict, searched: set) -> int:
        result = 0
        searched.add(node)
        for v in edges[node]:
            temp = self.dfs(v, edges, searched)
            result = max(result, temp)
        return result + 1

    # tested
    def findTwins(self, favorite: [int]) -> [[int]]:
        added = set()
        result = []
        for i in range(len(favorite)):
            cur = i
            if cur in added:
                continue
            friend = favorite[cur]
            if favorite[friend] == cur:
                # they are *twins*
                added = added.union(set([cur, friend]))
                result.append([cur, friend])
        return result
                

### test ###
def caseTest():
    s = Solution()
    favorite = [3,0,1,0,1]
    # print(s.findTwins(favorite), 'expected:', [[0,3],[1,4]])
    # print(favorite, s.readEdges(favorite))
    print(favorite, s.maximumInvitations(favorite))

    
    favorite = [1,2,0]
    print(favorite, s.maximumInvitations(favorite))

    favorite = [2,2,1,2]
    print(favorite, s.maximumInvitations(favorite))

    favorite = [4,2,1,1,3,3,5,2,7,7,8, 0]
    twin = [1,2]
    edges = s.readEdges(favorite)
    # print(favorite, edges)
    print(favorite, s.maximumInvitations(favorite))

    favorite = [2,2,1,2, 8, 4, 4, 6, 7]
    print(favorite, s.maximumInvitations(favorite))
   
    favorite = [2,2,1,2, 8, 4, 4, 6, 7, 10, 9, 9, 9, 10]
    print(favorite, s.maximumInvitations(favorite))

caseTest()
