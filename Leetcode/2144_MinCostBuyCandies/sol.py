'''
Prob: 2144 - Easy
Author: Ruowei Chen
Date: 26/Feb/2022
'''
class Solution:
    def minimumCost(self, cost: [int]) -> int:
        cost = sorted(cost, reverse=True)
        result = 0
        clen = len(cost)
        i = 0

        # at least three candies left in the loop
        while i < (clen-2):
            result += (cost[i] + cost[i+1])
            i += 3

        result += sum(cost[i:])
        return result

### test ###
s = Solution()
cost = [1,2,3]
print(s.minimumCost(cost))

cost = [6,5,7,9,2,2]
print(s.minimumCost(cost))

cost = [5,5]
print(s.minimumCost(cost))


