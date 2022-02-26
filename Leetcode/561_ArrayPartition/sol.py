'''
Prob: 561 Array Partition I - Easy
Author: Ruowei Chen
Date: 26/Feb/2022
'''
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums = sorted(nums)
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result

### test ###
s = Solution()
nums = [1,4,3,2]
print(s.arrayPairSum(nums))

nums = [6,2,6,5,1,2]
print(s.arrayPairSum(nums))

