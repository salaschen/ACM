'''
Prob: Spiral Matrix II - Medium
Author: Ruowei Chen
Date: 27/Jan/2022
Note:
    1) Brute-force walk
'''
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        directions = [\
                # right
                (0, 1), \
                # down
                (1, 0), \
                # left
                (0, -1), \
                # up
                (-1, 0)] 

        result = [[0 for i in range(n)] for j in range(n)]

        dIndex = 0
        cur = directions[dIndex]
        point = (0,0) # invariant: point is always a slot that hasn't been filled yet
        for i in range(1, (n**2)+1):
            x,y = point
            # print(x,y, cur) # debug
            result[x][y] = i

            # get to the next point
            dx,dy = cur
            point = (x+dx, y+dy)
            nx, ny = point
            if self.isOutOfBound(n, point) or result[nx][ny] > 0:
                dIndex = (dIndex + 1) % len(directions)
                cur = directions[dIndex]
                dx,dy = cur
                point = (x+dx, y+dy)

        return result

    def isOutOfBound(self, n: int, point: (int, int)) -> bool:
        x,y = point
        return x < 0 or x >= n or y < 0 or y >= n

### test ###
s = Solution()
n = 4
print(s.generateMatrix(n))
