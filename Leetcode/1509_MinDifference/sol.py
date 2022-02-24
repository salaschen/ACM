'''
Prob: 1509 Medium
Author: Ruowei Chen
Date: 24/Feb/2022
'''
class Solution:
    def minDifference(self, nums: [int]) -> int:
        if len(nums) <= 4:
            return 0
        nums = sorted(nums)
        return self.dfs(nums, 3)

    def dfs(self, nums: [int], moves: int) -> int:
        if moves == 0:
            # print(f'{nums}') # debug
            return abs(nums[0]-nums[-1])
        else:
            return min(self.dfs(nums[1:], moves-1), \
                       self.dfs(nums[:-1], moves-1))

### test ###
s = Solution()
nums = [5,3,2,4]
print(s.minDifference(nums))

nums = [1,5,0,10,14]
print(s.minDifference(nums))

import random
nums = [random.randint(1, 20) for i in range(10)]
print(sorted(nums))
print(s.minDifference(nums))
