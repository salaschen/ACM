'''
Prob: 1267 Medium
Author: Ruowei Chen
Date: 24/Feb/2022
'''
class Solution:
    def countServers(self, grid: [[int]]) -> int:
        added = set()
        m, n = len(grid), len(grid[0])
        rows = [[] for i in range(m)]
        cols = [[] for i in range(n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i].append((i,j))
                    cols[j].append((i,j))

        # now checks the rows and cols
        for row in rows:
            if len(row) > 1:
                for p in row:
                    added.add(p)
        
        for col in cols:
            if len(col) > 1:
                for p in col:
                    added.add(p)

        return len(added)

### test ###
s = Solution()
grid = [[1,0],[0,1]]
print(s.countServers(grid))

grid = [[1,0],[1,1]]
print(s.countServers(grid))

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print(s.countServers(grid))


