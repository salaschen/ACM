class Solution:
    def projectionArea(self, grid):
        '''
        :type grid: List[List[int]]

        '''
        xy_num = sum(list(map(lambda r: len(list(filter(lambda n: n != 0, r ))), grid))) ; 
        yz_num = sum(list(map(lambda r: max(r), grid))) ; 
        num_col = len(grid[0]) ; 
        xz_num = 0 ; 
        for i in range(0, num_col):
            xz_num += max(list(map(lambda r: r[i], grid))) ; 
        return xy_num+yz_num+xz_num ; 

if __name__ == "__main__":
    s = Solution() ;
    grid = [[2]] ; 
    print('result=', s.projectionArea(grid)) ; 
    
    grid = [[1,2],[3,4]] ; 
    print('result=', s.projectionArea(grid)) ; 

    grid = [[1,0], [0,2]] ; 
    print('result=', s.projectionArea(grid)) ; 

    grid = [[1,1,1], [1,0,1], [1,1,1]] ; 
    print('result=', s.projectionArea(grid)) ; 

    grid = [[2,2,2],[2,1,2], [2,2,2]] ; 
    print('result=', s.projectionArea(grid)) ; 


