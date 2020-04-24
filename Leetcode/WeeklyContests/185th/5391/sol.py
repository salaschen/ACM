'''
Prob: Leetcode - 1420 Build Array where you can find the 
maximum Exactly K Comparisons - Hard
Author: Ruowei Chen
Date: 21/Apr/2020
Note:
    1) Didn't AC this problem during contest.
    2) Try again now. Using DP. dp[i][j][k] means at position i
    in the array, when we place number j at this position, the number of 
    possible combinations of k comparisons happend (including the number j)
    at this point.
    For example, dp[0][n][1] = 1, for all n >= 1 because the original
    maximum_value is -1. 
    if dp[5][4][5] = 10, then dp[6][4][5] sum(dp[5][j][4]) for all j < 4
    and sum(dp[5][k][5] for all k >= 4.

    3) The dp above doesn't work because if the previous number is not the largest, then we cannot guaranteed that
    when the number in the next position is larger than the previous number, we can have one more comparison. For 
    example: dp[3][4][2] = 2, meaning at position 3, when number 4 is on that position, and 2 shifted already happend,
    then dp[4][5][3] = 2 is not right because we may have 1,5,4 so the current max is 5, add a 5 at the end doesn't 
    increase the number of shifts. 

    Now, I use the idea that someone posted, dp[i][j][k] meaning at position i, when we have j comparisons, the
    maximum number so far we have seen is k. The base case would be, dp[0][1][ck] = 1 for 1 <= ck <= m.
    For state transitions, dp[i+1][j][cm] = dp[i][j][cm] * cm, because, the next number we selected 1<=cm<=m,
    we have k selections. 
'''
class Solution:
    def __init__(self):
        return 

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        modNum = (10 ** 9) + 7
        # dp[nn][kk][mm]: nn is position, kk is the number of transitions that have happend, mm is the 
        # largest of the first nn numbers. 
        dp = [[[0 for _ in range(m+5)] for _ in range(k+5)] \
                for _ in range(n+5)]

        if m < k:
            return 0

        # now set the base case
        # the first number always change the value of max, because the max is -1 initially. 
        for i in range(1, m+1):
            dp[0][1][i] = 1

        # now do the transition
        # with no jump
        for i in range(1, n):
            for j in range(1, k+1):
                for mm in range(1, m+1):
                    # for non-jump cases:
                    dp[i][j][mm] = sum([dp[i-1][j-1][x] for x in range(1, mm)])

                    # for jumping cases
                    dp[i][j][mm] = dp[i][j][mm] + dp[i-1][j][mm] * mm

        result = 0
        for i in range(1, m+1):
            result = (result + dp[n-1][k][i]) % modNum

        return result
    
##### test #####
s = Solution()
n,m,k = 2,3,1
print(s.numOfArrays(n,m,k))
n,m,k = 5,2,3 
print(s.numOfArrays(n,m,k))
n,m,k = 4,5,4 
print(s.numOfArrays(n,m,k))
n,m,k = 9,1,1
print(s.numOfArrays(n,m,k))
n,m,k = 50, 100, 25
print(s.numOfArrays(n,m,k))
n,m,k = 37, 17, 7
print(s.numOfArrays(n,m,k))
