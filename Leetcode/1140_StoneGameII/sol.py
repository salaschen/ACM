'''
Prob: Leetcode - Medium
Author: Ruowei Chen
Date: 26/Oct/2021
Note:
    1) Dynamic Programming - Wrong optimal structure, need to include the current m
    2) Dfs with cache - pass

'''

from functools import lru_cache
class Solution:

    def stoneGameII_New(self, piles:[int]) -> int:
        self.T = len(piles)
        self.sums = [sum(piles)]
        
        for i in range(1, self.T):
            self.sums.append(self.sums[-1]-piles[i-1])
        # print(self.sums) # debug
        return self.dp(0, 1)

    @lru_cache(None)
    def dp(self, pos, m):
        answer = 0
        if self.T - pos <= 2 * m:
            answer = self.sums[pos]
        else:
            answer = self.sums[pos] - min([self.dp(pos+x, max(m,x)) for x in range(1, 2*m+1)])
        # print('dp({0},{1})={2}'.format(pos,m,answer)) # debug
        return answer ;
    
    def stoneGameII(self, piles:[int]) -> int:
        sums = [sum(piles)]
        T = len(piles)
        for i in range(1, T):
            sums.append(sums[-1]-piles[i-1])

        M = max(2, T)  # the maximum of m
        dp = [[0 for x in range(M+1)] for y in range(T+1)]
        for i in range(M+1):
            dp[T-1][i] = piles[T-1]
        dp[T-1][0] = 0

        # now work the dps backward
        for i in range(T-1, -1, -1):
            dp[i][0] = 0 
            for m in range(1, M+1):
                if 2*m >= T-i: # now I can all the remaining stones, why not.
                    dp[i][m] = sums[i]
                else:
                    candidates = [ dp[i][m-1] ]
                    
                    # take 2m-1 piles
                    cur = sums[i] - dp[2*m-1+i][2*m-1]
                    candidates.append(cur)

                    # take 2m piles
                    cur = sums[i] - dp[2*m+i][2*m]
                    candidates.append(cur)

                    dp[i][m] = max(candidates)
                    # print('dp[{0}][{1}] candidates: {2}'.format(i,m,candidates)) # debug

        # debug
        print(piles)
        for i in range(T+1):
            line = "{0}:".format(i)
            for j in range(M):
                line += '({0}, {1}),'.format(j, dp[i][j])               
            print(line)

        return dp[0][1]

#### test ####
s = Solution()
'''
piles = [2,7,9,4,4]
print('answer:', s.stoneGameII(piles))

piles = [1,2,3,4,5,100]
print('answer:', s.stoneGameII(piles))
'''

piles = [i for i in range(1, 101)]
print('New answer:', s.stoneGameII_New(piles))

'''
piles = [1]
print('answer:', s.stoneGameII(piles))

piles = [1,2]
print('answer:', s.stoneGameII(piles))
'''

piles = [1,2,3,4,5,6,7,8,9]
print('answer:', s.stoneGameII(piles))
print('other answer:', s.stoneGameII_Other(piles))
