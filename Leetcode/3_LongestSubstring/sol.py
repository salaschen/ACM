'''
Prob: Medium - 3. Longest SubString without Repeating Characters
Author: Ruowei Chen
Date: 30/Nov/2019
Note: AC.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0 ; 
        curString = '' ; 
        for i in range(len(s)):
            cur = str[i] ; 
            if cur in curString:
                result = max(result, len(curString)) ; 
                # truncate all the string before the matching character.
                index = curString.index(cur) ; 
                curString = curString[index+1:] + cur ; 
            else:
                curString += cur ; 
        result = max(result, len(curString)) ; 
        return result ; 
                

