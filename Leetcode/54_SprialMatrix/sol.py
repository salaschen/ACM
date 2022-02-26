'''
Prob: 54 Sprial Matrix - Medium
Author: Ruowei Chen
Date: 26/Feb/2022
'''
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # print(visited) # debug
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        pos = (0,0)
        result = []
        while True:
            x,y = pos
            # input()
            # print(f'(x,y) = {(x,y)}; d={d}') # debug
            if visited[x][y]:
                d = (d+1) % 4
                dx, dy = directions[d]
                x,y = x+dx, y+dy
                if visited[x][y]:
                    break
                else:
                    pos = (x,y)
            else:
                result.append(matrix[x][y])
                visited[x][y] = True
                dx, dy = directions[d]
                nx, ny = x+dx,y+dy
                if self.isBoundary(m,n,nx,ny) or visited[nx][ny]:
                    d = (d+1)%4
                    dx, dy = directions[d]
                pos = (x+dx, y+dy)
                if self.isBoundary(m,n,pos[0], pos[1]) or visited[pos[0]][pos[1]]:
                    break

                # print(f'result: {result}') # debug
        return result


    def isBoundary(self, m, n, x, y):
        return x < 0 or x >= m or y < 0 or y >= n
                

### test ###
s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(s.spiralOrder(matrix))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(s.spiralOrder(matrix))

matrix = [[5]]
print(s.spiralOrder(matrix))

matrix = [[5, 2]]
print(s.spiralOrder(matrix))

