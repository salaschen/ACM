'''
Level: Easy
Author: Ruowei Chen
Date: 02/Oct/2021
'''
class Solution:
    def __init__(self):
        self.mem = dict() ; 

    def tribonacci(self, n: int) -> int:
        self.mem[0],self.mem[1], self.mem[2] = 0,1,1 ;
        cur = 2 ; 
        while cur < n:
            self.mem[cur+1] = self.mem[cur] + self.mem[cur-1] + self.mem[cur-2] ;
            cur += 1 ;
        return self.mem[n] ;