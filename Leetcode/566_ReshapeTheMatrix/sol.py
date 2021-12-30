'''
Prob: 566 - Reshape the Matrix - Easy (study plan)
Author: Ruowei Chen
Date: 30/Dec/2021
'''
class Solution:
    def matrixReshape(self, mat: [[int]], r: int, c: int) -> [[int]]:
        m,n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        result = []
        line, count = [], 0
        for row in mat:
            for num in row:
                if count == c:
                    result.append(line)
                    line, count = [],0
                line.append(num)
                count += 1
        result.append(line)
        return result

### test ###
s = Solution()
mat = [[1,2],[3,4]]
r,c = 1,4
print(s.matrixReshape(mat, r,c))
        
mat = [[1,2],[3,4]]
r,c = 2,4
print(s.matrixReshape(mat, r,c))

mat = [[1,2],[3,4],[5,6],[7,8]]
r,c = 2,4
print(s.matrixReshape(mat, r,c))



