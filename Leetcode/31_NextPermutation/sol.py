'''
Leetcode - Medium - Next Permutation
Author: Ruowei Chen
Date: 29/Mar/2020
'''
class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        # check boundary
        if len(nums) <= 1:
            return nums

        nlen = len(nums)
        state = 0
        c, p = nlen-2, nlen-1
        while c >= 0:
            cur, prev = nums[c], nums[p]
            if state == 0:
                if cur == prev:
                    # still in state 0
                    pass
                elif cur < prev:
                    # swap cur and prev and return
                    # state 5
                    nums[c], nums[p] = prev, cur
                    return nums
                else: # cur > prev 
                    # into state one
                    state = 1
            elif state == 1:
                if cur >= prev:
                    pass # still in state 1
                elif cur < prev:
                    state = 3
                    index = nlen - 1
                    while index >= p:
                        if nums[index] > cur:
                            break
                        index -= 1
                    # swap
                    nums[c], nums[index] = nums[index], nums[c]

                    nums[p:] = sorted(nums[p:])
                    return nums

            # update
            c,p = c-1,c
        
        # EOF
        if state == 1:
            return sorted(nums)
        elif state == 0:
            return nums

##### test #####
s = Solution()
print(s.nextPermutation([1,2,3]))
print(s.nextPermutation([1,2,3,4, 5]))
print(s.nextPermutation([1,3,2,1]))
print(s.nextPermutation([1,1,1,1]))
print(s.nextPermutation([5,4,3,2,1]))
print(s.nextPermutation([1]))
print(s.nextPermutation([2,3,1]))
