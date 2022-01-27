'''
Prob: Search 2D Matrix II - Medium
Author: Ruowei Chen
Date: 27/Jan/2022
'''
class Solution:
    
    # transpose the matrix (row->col, col->row)
    def transpose(self, matrix: [[int]]) -> [[int]]:
        m, n = len(matrix), len(matrix[0])
        result = [[] for i in range(n)]
        for i in range(m):
            row = matrix[i]
            for j in range(len(row)):
                result[j].append(row[j])
        return result

    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        tmatrix = self.transpose(matrix)
        # print(tmatrix) # debug
        return self.search(matrix, tmatrix, (0,0), (m-1,n-1), target)


    def search(self, matrix: [[int]], tmatrix: [[int]], left: (int, int), \
            down: (int, int), target: int) -> bool:
        # search both end
        if matrix[left[0]][left[1]] > target or matrix[down[0]][down[1]] < target:
            return False

        # generate four arrays to be searched
        lx,ly = left
        dx,dy = down
        arrays = [matrix[lx][ly:dy+1], \
                  matrix[dx][ly:dy+1], \
                  tmatrix[ly][lx:dx+1], \
                  tmatrix[dy][lx:dx+1]]
        for arr in arrays:
            try:
                # print('finding:', arr) # debug
                ind = arr.index(target)
                return True
            except:
                continue
        
        # not found in the currnet lines
        # go to the inner matrix
        lx, ly = lx+1, ly+1
        dx, dy = dx-1, dy-1
        # ouf of bound
        if lx > dx or ly > dy:
            return False
        else:
            return self.search(matrix, tmatrix, (lx,ly), (dx,dy), target)

### test ###
s = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(s.searchMatrix(matrix, target))

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 9 
print(s.searchMatrix(matrix, target))

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(s.searchMatrix(matrix, target))

matrix = [[1,1]]
target = 20
print(s.searchMatrix(matrix, target))

       
