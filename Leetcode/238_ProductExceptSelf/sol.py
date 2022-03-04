'''
Prob: 238 - Meiudm
Author: Ruowei Chen
Date: 04/Mar/2022
Note:
    1) O(n) space and O(n) time without using the division operation.
'''
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        n = len(nums)
        front, end = [1 for i in range(n)], [1 for i in range(n)]
        for i in range(1, n):
            front[i] = front[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            end[i] = end[i+1] * nums[i+1]

        return list(map(lambda p: p[0]*p[1], zip(front, end)))
        
### test ###
s = Solution()
nums = [1,2,3,4]
print(s.productException(nums))

nums = [-1, 1, 0, -3, 3]
print(s.productException(nums))

