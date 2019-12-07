'''
Prob: Leetcode 1260 Easy - Shift 2D Grid
Author: Ruowei Chen
Date: 17/Nov/2019
'''
class Solution:
    def shiftGrid(slef, grid: [[int]], k: int) -> [[int]]:
        # first flattens the grid into a one dimensional array
        temp = [] ; 
        for row in grid:
            for num in row:
                temp.append(num) ; 
        
        # shift the numbers to the right.
        length = len(temp) ; 
        k = k % length ; # the first error, k can be larger than the size of the grid.
        temp = temp[length-k:] + temp[0:length-k] ; 

        # structuralize the array back into two dimensional array 
        rowSize = len(grid[0]) ; 
        result = [] ; 
        cur = 0 ; 
        row = [] ; 
        while cur < length:
            if cur != 0 and cur % rowSize == 0:
                result.append(row) ; 
                row = [temp[cur]] ; 
            else:
                row.append(temp[cur]) ; 
            cur += 1 ; 
        if len(row) > 0:
            result.append(row) ; 

        return result ; 

s = Solution();
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]] ; 
k = 4 ; 
result = s.shiftGrid(grid, k) ; 
print(result) ; 