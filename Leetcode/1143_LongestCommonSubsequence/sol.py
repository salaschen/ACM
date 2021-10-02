'''
Level: Medium
Author: Ruowei Chen
Date: 02/Oct/2021
Note: 
    1) Feels like it's going to be DP, but I don't know how yet. 
    2) After reading on wiki now I know, and it's a NP-Hard problem so fair enough.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int: 
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)] ; 
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1 ; 
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) ;
        # print(dp) ; # debug
        return dp[len(text1)][len(text2)] ; 

##### test #####
s = Solution() ;
print(s.longestCommonSubsequence("abcde", "ace"))  ;
print(s.longestCommonSubsequence("abc", "abc"))  ;
print(s.longestCommonSubsequence("abc", "def"))  ;
