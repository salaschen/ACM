'''
Prob: 409 Longest Palindrome - Easy
Author: Ruowei Chen
Date: 04/Mar/2022
'''
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        centre = False
        c = Counter(s)
        result = 0
        for key in c.keys():
            result += (c[key] // 2) * 2
            if c[key] % 2 == 1:
                centre = True
        if centre:
            result += 1
        return result


### test ###
sol = Solution()
s = 'abccccdd'
print(sol.longestPalindrome(s))

s = 'a'
print(sol.longestPalindrome(s))

s = 'bb'
print(sol.longestPalindrome(s))



