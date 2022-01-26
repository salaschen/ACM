'''
Prob: 75 Sort Colors - Medium
Author: Ruowei Chen
Date: 12/Jan/2022
Note:
    1) Brute-force algorithm first
'''
class Solution:
    def sortColors(self, nums: [int]) -> None:
        count = [0,0,0]
        for i in range(len(nums)):
            count[nums[i]] += 1
        
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

    # two pass algorithm
    def sortColorsOld(self, nums: [int]) -> None:
        ind = self.sortFromLeft(nums, 0, 0)
        self.sortFromLeft(nums, ind, 1)

    # make all the 0s in place
    def sortFromLeft(self, nums: [int], start, target) -> int:
        result = None
        if start is None:
            return None
        for i in range(start, len(nums)):
            cur = nums[i]
            if cur != target:
                # now find the next 0
                found = None
                for j in range(i+1, len(nums)):
                    if nums[j] == target:
                        found = j
                        break
                # all the 0s are in the right place
                if found is None: 
                    result = i
                    break
                # do the swap
                else:
                    nums[i], nums[found] = nums[found], nums[i]
        return result

    
### test ###
def caseTest():
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)

    nums = [2,0,1,0]
    s.sortColors(nums)
    print(nums)

    nums = [0,0,0,0]
    s.sortColors(nums)
    print(nums)

    nums = [1,1,1,1,1]
    s.sortColors(nums)
    print(nums)

    nums = [2,2,2,2,2]
    s.sortColors(nums)
    print(nums)

    nums = [2,0,2,2,2]
    s.sortColors(nums)
    print(nums)

    nums = [1,0,1,1,1]
    s.sortColors(nums)
    print(nums)



def compareArray(arr1, arr2):
    if len(arr1) != len(arr2): 
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def randomTest():
    import random
    times = 100
    size = 200
    s = Solution()
    result = 0
    for i in range(times):
        nums = [random.randint(0, 2) for i in range(size)]
        nums2 = nums[:]
        s.sortColors(nums2)
        nums = sorted(nums)
        if compareArray(nums, nums2):
            result += 1
    print('pass: {0}/{1}'.format(result, times))

randomTest()

