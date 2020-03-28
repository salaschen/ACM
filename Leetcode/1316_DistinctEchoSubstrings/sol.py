'''
Leetcode 1316 - Hard - Distinct Echo Substrings
Author: Ruowei Chen
Date: 28/Mar/2020
Note: Test for Rolling hash
'''
import random
from functools import reduce

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        tlen = len(text) 
        if tlen <= 1:
            return 0
        curLen = 1

        dump = set() # for debug only
        
        R = 26
        M = 1
        Q = 10 ** 9 - 7
        hashDict = dict()
        for i in range(tlen-1):
            hashDict[i] = ord(text[i]) * R 
            if text[i] == text[i+1]:
                dump.add(text[i]+text[i+1]) 
        hashDict[tlen-1] = ord(text[tlen-1]) * R

        M += 1
        while M <= tlen/2:
            # recalculate the hash
            for i in range(0, tlen-M+1):
                hashDict[i] = (hashDict[i] * R + ord(text[i+M-1])) % Q

            for i in range(0, tlen):
                first = i
                second = i+M
                if second+M > tlen:
                    break
                if hashDict[first] == hashDict[second]:
                    dump.add(text[first:first+M]+text[second:second+M])

            M += 1

        print(dump) ; # debug
        return len(dump)

def test():
    string = "abcdefg"
    Q = 10 ** 9 - 7 
    M = 3 # length of the pattern;
    R = 26 # for alphabet
    RM = (R ** (M-1)) % Q 
    
    # calculate the hash for "abc"
    cur = hash("abc", R,M,Q) 
    print(cur) ; 
    
    # now calculate the next hash
    expect = hash("bcd", R, M, Q) 
    actual = ((cur - ord('a')*(RM))*R + ord('d')) % Q
    print('expect={0}, actual={1}'.format(expect, actual))
    return

def hash(string, R, M, Q):
    cur = 0 ;
    slen = len(string)
    for i in range(0, M):
        if i >= slen:
            break
        cur = cur * R + ord(string[i])
    return cur % Q
    
# find the first pattern occurrence in the text
# return the index of the occurrence, -1 if not found.
def substring(text, pattern):
    if len(text) < len(pattern):
        return -1
    R = 26
    M = len(pattern)
    Q = 10 ** 9 - 7
    tlen = len(text)
    RM = (R ** (M-1)) % Q
    
    phash = hash(pattern, R, M, Q)
    thash = hash(text, R, M, Q)
    index = 0
    while index < tlen:
        if thash == phash:
            return index
        # now roll the thash.
        thash = ((thash + ord(text[index])*(Q - RM)) * R + ord(text[index+M])) % Q
        index += 1
    return -1 


########## test ##########33
def gen(stringSet, length):
    return reduce(lambda a,b: a+b, [random.choice(stringSet) for i in range(length)])


s = Solution()
text = "abcabcabc"
print(s.distinctEchoSubstrings(text))
text = "leetcodeleetcode"
print(s.distinctEchoSubstrings(text))
text = ""
print(s.distinctEchoSubstrings(text))
text = "a"
print(s.distinctEchoSubstrings(text))
text = gen([chr(ord('a')+i) for i in range(5)], 100)
print(s.distinctEchoSubstrings(text))

