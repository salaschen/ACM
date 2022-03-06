'''
Prob: 187 Medium
Author: Ruowei Chen
Date: 06/Mar/2022
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        from collections import Counter
        c = Counter()
        start, end = 0, 10
        while end <= len(s):
            c[s[start:end]] += 1
            start, end = start + 1, end + 1
        return [key for key in c if c[key] > 1]

### test ###
sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(sol.findRepeatedDnaSequences(s))
        
s = "AAAAAAAAAAAAA"
print(sol.findRepeatedDnaSequences(s))
 
