'''
Problem: Leetcode 91 Medium
Author: Ruowei Chen
Date: 05/Feb/2021
Note: 
    1) Use dynamic programming.
'''
import math

class Solution:
    def numDecodings(self, s: str) -> int:
        d = dict() ;
        d[0] = 1 ; 
        slength = len(s) ;
        if slength == 0 or s[0] == "0":
            return 0 ; 
        if s[-1] == "0":
            d[1] = 0 ;
        else:
            d[1] = 1 ;
        head = slength - 2 ; 
        for i in range(2, slength+1):
            d[i] = 0 ; 
            if (int(s[head]) > 0):
                d[i] = d[i-1] ;
            if (int(s[head:head+2]) <= 26 and s[head] != "0"):
                d[i] += d[i-2] ;
            head -= 1 ;

        return d[slength] ;

#### main process
s = Solution() ;
st = "12" ;
print(s.numDecodings(st)) ; 
st = "226" ;
print(s.numDecodings(st)) ; 
st = "0" ;
print(s.numDecodings(st)) ; 
st = "1" ;
print(s.numDecodings(st)) ; 
st = "1232999823842367423402345234523452345" ;
print(s.numDecodings(st)) ; 
st = "06" ;
print(s.numDecodings(st)) ; 
st = "10" ;
print(s.numDecodings(st)) ; 






