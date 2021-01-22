'''
Problem: 53 Maximum Subarray - Leetcode
Author: Ruowei Chen
Date: 22/Jan/2021
Note:
    1) Linear time O(N) algorithm.
'''
import random ; 
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        if len(nums) == 0:
            return None ;

        result = nums[0] ;
        size = len(nums) ; 
        curSum = nums[0] ;
        i = 1 ;  
        while i < size: 
            if curSum > result:
                result = curSum ; 

            if curSum < 0:
                curSum = nums[i] ;
            else:
                curSum += nums[i] ;
            i += 1 ;
        if curSum > result:
            result = curSum ; 
        return result ; 

    # slow method for testing
    def slow(self, nums: [int]) -> int:
        result = nums[0]; 
        size = len(nums) ;
        for i in range(size):
            temp = nums[i] ;
            if result < temp:
                result = temp ; 
            for j in range(i+1, size):
                temp += nums[j] ;
                if result < temp:
                    result = temp ; 
        return result ;


#### testing
s = Solution() ;
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] ;
print(s.maxSubArray(nums)) ;
nums = [1] ; 
print(s.maxSubArray(nums)) ;
nums = [-1, -2, -3, -4, 0, -5] ;
print(s.maxSubArray(nums));
nums = [-10000] ;
print(s.maxSubArray(nums)) ;
nums = [random.randint(-1*10**5, 10**5) for i in range(10**4)]
print(s.maxSubArray(nums)) ;
print(s.slow(nums)) ;
nums = [86, -86, 47, -49, 86, 77, 42, 7, 61, 50]
print(nums) ;
print(s.maxSubArray(nums)) ;
print(s.slow(nums)) ;
        
