'''
Prob: 75 Sort Colors
Author: Ruowei Chen
Date: 26/Feb/2022
Note:
    1) Second attempt for this problem
'''
class Solution:
    def sortColors(self, nums: [int]) -> None:
        zero, two = -1, -1
        for i in range(0, len(nums)):
            if nums[i] != 0:
                zero = i
                break
        for i in range(len(nums)-1, -1, -1):
            if nums[i] != 2:
                two = i
                break

        i = zero
        while i <= two:
            # print(f'nums: {nums}, i: {i}, zero: {zero}, two: {two}') # debug
            if nums[i] == 0:
                # swap this number with the zero index
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            
            elif nums[i] == 2:
                # swap this number with the two index
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
                if i <= zero and nums[i] == 0:
                    zero += 1
                    i += 1
            
            else:
                i += 1

        return

### test ###
def randomTest():
    import random
    times = 100
    pas = 0
    s = Solution()
    for _ in range(times):
        nums = [random.randint(0, 2) for i in range(300)]
        nums2 = nums[:]
        nums = sorted(nums)
        s.sortColors(nums2)
        if nums2 != nums:
            print(f'error: {nums2}')
        else:
            pas += 1
    print(f'pass {pas}/{times}')


def caseTest():
    import random
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums) 

    nums = [2,0,1]
    s.sortColors(nums)
    print(nums) 

    # nums = [2, 2, 1, 2, 1, 0, 1, 1, 0, 0]
    nums = [0, 1, 0, 2, 0, 1, 1, 1, 0, 2]
    # nums = [random.randint(0, 2) for i in range(10)]
    print(f'original: {nums}') 
    s.sortColors(nums)
    print(f'sorted: {nums}') 

# caseTest()
randomTest()
