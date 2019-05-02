class Node:
    def __init__(self, row, col, grid):
        self.row = row ;
        self.col = col ; 
        self.border = self.isBorder(grid) ; 

    def isBorder(self, grid):
        if self.row == 0 or self.row == len(grid)-1:
            return True ;
        if self.col == 0 or self.col == len(grid[0])-1:
            return True ; 

        neibors = self.neighbors(grid) ; 
        for n in neibors:
            if grid[n[0]][n[1]] != grid[self.row][self.col]:
                return True ; 
        return False ;

    def neighbors(self, grid):
        r, c = self.row, self.col ; 
        numRow = len(grid) ;
        numCol = len(grid[0]) ;
        lst = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)] ;
        lst = list(filter(lambda a: a[0] >= 0 and a[0] < numRow, lst)) ; 
        lst = list(filter(lambda a: a[1] >= 0 and a[1] < numCol, lst)) ; 
        # lst = list(filter(lambda a: grid[a[0]][a[1]] == grid[r][c], lst)) ;
        return lst ;


class Solution:
    def colorBorder(self, grid, r0, c0, color):
        seen = set() ; 
        queue = [(r0, c0)] ; 
        toChange = [] ; 
        while len(queue) > 0:
            coord = queue.pop(0) ; 
            if coord in seen:
                continue ; 
            node = Node(coord[0], coord[1], grid) ;
            seen.add(coord) ; 
            if node.border:
                toChange.append((node.row, node.col)) ; 
            neibors = node.neighbors(grid) ; 
            for n in neibors:
                if n not in seen and grid[n[0]][n[1]] == grid[r0][c0]:
                    queue.append(n) ; 

        for coord in toChange:
            grid[coord[0]][coord[1]] = color ; 
        return grid ; 

def main():
    grid = [[1,2,2], [2,3,2]] ; 
    r0 = 0 ; c0 = 1 ; color = 3 ;
    s = Solution() ; 
    print(grid) ; 
    g = s.colorBorder(grid, r0, c0, color) ; 
    print(g) ; 

    grid = [[1,1,1],[1,1,1],[1,1,1]] ;
    r0 = 1 ; c0 = 1 ; color = 2 ; 
    print(grid) ; 
    g = s.colorBorder(grid, r0, c0, color) ; 
    print(g) ;

    grid = [[1,2,1,2,1,2],[2,2,2,2,1,2],[1,2,2,2,1,2]] ;
    r0 = 1 ; c0 = 3 ; color = 1 ; 
    print(grid) ; 
    g = s.colorBorder(grid, r0, c0, color) ; 
    print(g) ;



if __name__ == "__main__":
    main() ; 

