'''
Prob: 74 - Search a 2D Matrix - Medium (Study plan)
Author: Ruowei Chen
Date: 30/Dec/2021
'''
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        import bisect
        line = []
        for row in matrix:
            line.append(row[0])
        pos = bisect.bisect(line, target)
        if pos == 0: 
            return False
        if line[pos-1] == target:
            return True
        
        # search in the row
        row = matrix[pos-1]
        pos = bisect.bisect(row, target)
        if pos == 0 :
            return False
        if row[pos-1] == target:
            return True
        else:
            return False

### test ###
s = Solution()
matrix = [[1,3,5,7], [10,11,16,20], [23,30, 34,60]]
print(s.searchMatrix(matrix, 3))
print(s.searchMatrix(matrix, 1))
print(s.searchMatrix(matrix, 0), False)
print(s.searchMatrix(matrix, 10), True)
print(s.searchMatrix(matrix, 23), True)
print(s.searchMatrix(matrix, 7), True)
print(s.searchMatrix(matrix, 60), True)
print(s.searchMatrix(matrix, 30), True)
print(s.searchMatrix(matrix, 31), False)
print(s.searchMatrix(matrix, 61), False)
print(s.searchMatrix(matrix, 10000), False)
print(s.searchMatrix(matrix, 15), False)
print(s.searchMatrix(matrix, 21), False)



