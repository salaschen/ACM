'''
GCJ Qualification Round
Author: Ruowei Chen
Date: 04/Apr/2020
'''

class Solution:
    def __init__(self):
        pass

    # read input and generate the matrix
    # and work out the result.
    def readInput(self) -> [[int]]:
        N = int(input())
        self.matrix = []
        self.N = N
        self.rr = 0 # repeated row 
        self.rc = 0 # repeated col
        self.trace = 0 # trace
        self.rmatrix = [[] for n in range(N)] # reverse matrix
        for i in range(N):
            row = [int(num) for num in input().split()]
            if len(row) > len(set(row)):
                self.rr += 1
            for j in range(N):
                self.rmatrix[j].append(row[j])
            self.trace += row[i]
            self.matrix.append(row)

        for col in self.rmatrix:
            if len(col) > len(set(col)):
                self.rc += 1

        return (self.trace, self.rr, self.rc)

###### main ######
s = Solution()
numCase = int(input())
for i in range(1, numCase+1):
    k, r, c = s.readInput()
    print('Case #{0}: {1} {2} {3}'.format(i, k, r, c))

