'''
Prob: Leetcode 1995 - Count Special Quadruplets
Level: Easy
Author: Ruowei Chen
Date: 08/Sep/2021
'''
class Solution:

    def countQuadruplets(self, nums: [int]) -> int:
        tripSumDict = dict() ; 
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    temp = nums[i]+nums[j]+nums[k] ; 
                    if temp in tripSumDict:
                        tripSumDict[temp].append((i,j,k)) ;
                    else:
                        tripSumDict[temp] = [(i,j,k)] ; 
        
        result = 0 ;
        for i in range(0, len(nums)):
            if nums[i] in tripSumDict:
                for triplets in tripSumDict[nums[i]]:
                    if i > max(triplets):
                        result += 1 ; 
        return result ; 

s = Solution() ;
nums = [1,2,3,6] ;
print(s.countQuadruplets(nums))

nums = [3,3,6,4,5] ;
print(s.countQuadruplets(nums))

nums = [1,1,1,3,5] ;
print(s.countQuadruplets(nums))
