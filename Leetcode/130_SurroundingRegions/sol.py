'''
Prob: 130 - Medium, acceptance: 366,915/1,123,814
Author: Ruowei Chen
Date: 19/Nov/2021
'''
class Solution:
    def __init__(self):
        # record the 'O's that have been searched
        self.searched = set()

    def solve(self, board: [[str]]) -> None:
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if (i,j) in self.searched:
                    continue
                modified, isBorder = self.search((i,j), board, m, n)
                for pos in modified:
                    self.searched.add(pos)
                    if not isBorder:
                        board[pos[0]][pos[1]] = 'X'
    
    def search(self, pos, board, m, n):
        queue = [pos]
        modified = []
        searched = set()
        isBorder = False
        while len(queue) > 0:
            cur = queue.pop()
            if cur in searched:
                continue
            searched.add(cur)
            if cur[0] < 0 or cur[0] >= m or cur[1] < 0 or cur[1] >= n:
                isBorder = True
            elif board[cur[0]][cur[1]] == 'O':
                modified.append(cur)
                neighbors = [(cur[0]+1, cur[1]), (cur[0]-1, cur[1]), (cur[0], cur[1]+1), (cur[0], cur[1]-1)]
                queue.extend(neighbors)
            elif board[cur[0]][cur[1]] == 'X':
                continue 
        return (modified, isBorder)

### test ###
s = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
s.solve(board)
print(board)

board = [['X']]
s.solve(board)
print(board)




