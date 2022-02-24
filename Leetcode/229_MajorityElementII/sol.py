'''
Prob: 229 Majority Element II
Author: Ruowei Chen
Date: 24/Feb/2022
Note: 
    1) Randomized algorithm
'''
class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        import random
        import math
        sampleSize = 100
        samples = [(random.choice(nums), 0) for i in range(sampleSize)]
        mem = dict(samples)
        for n in nums:
            if n in mem:
                mem[n] += 1

        result = []
        size = len(nums)
        for key in mem.keys():
            if mem[key] > math.floor(size / 3):
                result.append(key)

        return result

### test ###
s = Solution()
nums = [3,2,3]
print(s.majorityElement(nums))

nums = [1]
print(s.majorityElement(nums))
        
nums = [1,2]
print(s.majorityElement(nums))
 
