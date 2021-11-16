'''
Prob: 2068 - Easy
Author: Ruowei Chen
Date: 16/Nov/2021
'''
class Solution:
    def checkAlmostEquivalent(self, word1:str, word2: str) -> bool:
        freq1, freq2 = [0 for i in range(26)], [0 for i in range(26)]
        for i in range(len(word1)):
            freq1[ord(word1[i])-ord('a')] += 1
            freq2[ord(word2[i])-ord('a')] += 1
        for i in range(26):
            if abs(freq1[i]-freq2[i]) > 3:
                return False
        return True

### test ###
s = Solution()
word1 = 'aaaa'
word2 = 'bccb'
print(s.checkAlmostEquivalent(word1, word2))


word1 = 'abcdeef'
word2 = 'abaaacc'
print(s.checkAlmostEquivalent(word1, word2))

word1 = 'cccddabba'
word2 = 'babababab'
print(s.checkAlmostEquivalent(word1, word2))


word1 = 'a'
word2 = 'b'
print(s.checkAlmostEquivalent(word1, word2))


