'''
Level: Easy
Author: Ruowei Chen
Date: 02/Oct/2021
'''
class Solution:
    def fib(self, n: int) -> int:
        fn = [0,1] ;
        if n < 2:
            return fn[n] ; 
        cur = 1
        while n > cur:
            temp = fn[0]+fn[1] ; 
            fn[0] = fn[1] ;
            fn[1] = temp ; 
            cur += 1 ;
        return fn[1] ; 
        
        
        