'''
Prob: 14 - Easy - Longest Common Prefix
Author: Ruowei Chen
Date: 31/Dec/2019
'''
class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        if len(strs) == 0: return ''  ;
        result = strs[0] ; 
        for i in range(1, len(strs)):
            cur = strs[i] ; 
            rlen = len(result) ; 
            clen = len(cur) ; 
            limit = min(rlen, clen) ; 
            j = 0 ; 
            temp = result[:limit] ; 
            for j in range(limit):
                if cur[j] != result[j]:
                    temp = result[:j] ; 
                    break ;
            result = temp ;  
            if result == '':
                break ; 
        return result; 


######## test #########
s = Solution() ; 
inp = ['flower', 'flow', 'flight'] ; 
print('output: {0}'.format(s.longestCommonPrefix(inp))) ; 

inp = ['dog', 'racecar', 'car'] ; 
print('output: {0}'.format(s.longestCommonPrefix(inp))) ; 

inp = ['race','race','race'] ; 
print('output: {0}'.format(s.longestCommonPrefix(inp))) ; 

inp = ['aa', 'a'] ; 
print('output: {0}'.format(s.longestCommonPrefix(inp))) ; 
