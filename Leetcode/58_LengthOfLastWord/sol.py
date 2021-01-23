'''
Problem: 58 Length of Last Word - Leetcode Easy
Author: Ruowei Chen
Date: 23/Jan/2021
'''

class Solution:
    def lengthOfLastWordOld(self, s: str) -> int:
        lst = s.split() ; 
        if len(lst) == 0:
            return 0 ;
        else:
            return len(lst[-1]) ; 

    def lengthOfLastWord(self, s: str) -> int:
        lastIndex = len(s) - 1 ; 
        while s[lastIndex] == ' ' and lastIndex >= 0:
            lastIndex -= 1 ; 
        if lastIndex < 0:
            return 0 ;
        result = 0 ; 
        while s[lastIndex] != ' ' and lastIndex >= 0:
            result += 1 ;
            lastIndex -= 1 ; 
        return result ; 
        
