'''
Leetcode 32 - Longest Valid Parentheses
Author: Ruowei Chen
Date: 10/Apr/2020
Note:
    1) failed the first submission on "()(()"
    2) failed the second attempt on "(()(((()", considerting use dp.
'''
import random
import time

class Solution:
    
    def longestValidParenthesesOld(self, s: str) -> int:
        curDepth = 0
        curLength = 0
        curOpen = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                curOpen += 1
            elif s[i] == ')':
                # legal
                if curOpen > 0:
                    curOpen -= 1
                    curDepth += 1
                    if curOpen == 0: # a valid group has formed.
                        curLength += curDepth
                        curDepth = 0

                # illegal - look back and find the longest substring.
                else:
                    result = max([result, curLength, curDepth])
                    curDepth = 0
                    curLength = 0
                    curOpen = 0

        if curOpen >= 0:
            result = max([result, curLength, curDepth])

        return result * 2

    def longestValidParentheses(self, s: str) -> int:
        result = 0
        slen = len(s)
        dp = [0 for n in range(slen)]
        cur = slen-2
        while cur >= 0:
            dp[cur] = 0
            if s[cur] == ')':
                dp[cur] = 0

            else:
                # now start with "("
                temp = 0
                nex = cur+1
                
                if dp[nex] > 0:
                    temp += dp[nex]
                    tail = nex+dp[nex]

                    if tail < slen and dp[tail] > 0:
                        temp += dp[tail]
                        tail = tail + dp[tail]
                        
                    if tail < slen and s[tail] == ')':
                        dp[cur] = temp + 2
                        
                    
                elif s[nex] == ')':
                    dp[cur] = 2 # because it matches the next character.
                    tail = cur + 2
                    if tail < slen:
                        dp[cur] += dp[tail]
            
            cur -= 1

        result = 0
        visited = set()
        for start in range(slen):
            temp = 0
            # if start in visited: 
            #     continue
            cur = start
            visited.add(cur)
            while cur < slen and dp[cur] != 0:
                temp += dp[cur] 
                cur = cur + dp[cur]
                visited.add(cur)

            result = max(temp, result)
        return result

    def longestValidParentheses0(self, s: str) -> int:
        slen = len(s)
        dp = [0 for n in range(slen)]
        cur = slen-2
        while cur >= 0:
            nex = cur+1
            if s[cur] == ')':
                dp[cur] = 0

            else:
                # now start with "("
                temp = 0
                if dp[nex] > 0:
                    temp += dp[nex]
                    tail = nex+dp[nex]

                    while tail < slen and dp[tail] > 0:
                        temp += dp[tail]
                        tail = tail + dp[tail]

                    if tail < slen and s[tail] == ')':
                        dp[cur] = temp + 2

                elif s[nex] == ')':
                    dp[cur] = 2 # because it matches the next character.
                    tail = cur + 2
            
            cur -= 1

        # print(dp) # debug
        result = 0
        for start in range(slen):
            temp = 0
            cur = start
            while cur < slen and dp[cur] != 0:
                temp += dp[cur] 
                cur = cur + dp[cur]
            result = max(temp, result)
        return result

###### test #######
def test():
    s = Solution()
    strings = ["()(()", "(()", ")()())", "())))())))))))()(())", "(()(((((()", "(()())))))",\
            "(()(((()))))))))()()", "(())()()()"]
    for string in strings:
        result = s.longestValidParentheses(string)
        print("Input: {0}\nOutput: {1}".format(string, result))
    return 

def genString(L: int):
    result = ''
    for i in range(L):
        result += random.choice(['(', ')'])
    return result

def calculate(string: str, start: int) -> int:
    curOpen = 0
    curDepth = 0
    curLength = 0
    slen = len(string)
    cur = start
    result = 0
    while cur < slen:
        if string[cur] == '(':
            curOpen += 1
        else:
            if curOpen > 0:
                curOpen -= 1
                curDepth += 1 
                if curOpen == 0:
                    curLength += curDepth
                    curDepth = 0
            else:
                result = max([result, curLength, curDepth])
                return result*2
        cur += 1

    result = max([result, curLength, curDepth]) 
    return result*2


def bruteForce(string: str):
    slen = len(string)
    result = 0
    for i in range(0, slen-1):
        temp = calculate(string, i) 
        # print("i={0}, temp={1}".format(i, temp)) # debug
        result = max(result, temp)
    return result

def btest():
    string = "(()((((()"
    print(string)
    print(bruteForce(string))
    return 
    
def randomTest():
    T = 1000   
    L = 100
    s = Solution()
    Pass = 0
    etime, atime = 0, 0
    for i in range(T):
        string = genString(L)
        st = time.time()
        expect = s.longestValidParentheses0(string)
        et = time.time()
        etime += (et-st)
        st = time.time()
        actual = s.longestValidParentheses(string)
        et = time.time()
        atime += (et-st)
        if expect == actual:
            Pass += 1
        else:
            print("string: {0}\nexpect: {1}\nactual: {2}".format(string, expect, actual))

    print("Length: {4}\ntest passed {0}/{1}\nexpect time: {2}\nactual time: {3}"\
            .format(Pass, T, etime, atime, L))
    return 

def main():
    randomTest()
    # btest()
    # test()
    return 


main()

