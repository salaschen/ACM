'''
Prob: leetcode 33 - Medium - search in rotated sorted array
Author: Ruowei Chen
Date: 17/Apr/2020
Note:
    1) Find the pivot point first?
'''
import random
import time
class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums) <= 10:
            return self.bfSearch(nums, target) 

        piv = self.findPivot(nums) 

        # quick test first
        if target < nums[piv] or (target < nums[0] and target > nums[-1]):
            return -1

        if target >= nums[0]:
            return self.bsearch(nums[:piv], target)
        else:
            temp = self.bsearch(nums[piv:], target)
            if temp == -1:
                return -1
            else:
                return piv+temp

    def bsearch(self, nums: [int], target: int) -> int:
        low, up = 0, len(nums)-1 
        while low+1 < up:
            mid = (low+up) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                up = mid
            else:
                low = mid
        
        # now low+1 == up, we just need to check nums[low] and nums[up]
        if target == nums[low]:
            return low
        if target == nums[up]:
            return up
        return -1

    # brute-force when the length of the array is really small, say 10.
    def bfSearch(self, nums: [int], target: int) -> int:
        result = -1 
        for i in range(len(nums)):
            if nums[i] == target:
                result = i
                break
        return result

    def findPivot(self, nums: [int]) -> int:
        low, up = 0, len(nums)-1
        while True:
            mid = (low+up) // 2
            if nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                return mid
            if nums[low] < nums[mid]:
                low = mid 
            else:
                up = mid 
            if low+1 == up:
                if nums[low] > nums[up]:
                    return up
                else:
                    return low
        return


########## test ########
def testPivot():
    s = Solution()
    arr = [29, 30, 33, 35, 36, 38, 40, 3, 11, 12, 15, 17, 25, 27]
    print(arr)
    print(s.findPivot(arr))


def testBsearch():
    s = Solution()
    arr = [26, 28, 29, 30, 33, 34, 35, 39, 3, 7, 9, 11, 13, 14, 15, 19, 21, 23, 25]
    target = 24
    piv = s.findPivot(arr)
    print(s.bsearch(arr[:piv], target))

def testSearch():
    s = Solution()
    T = 100 
    size = 400000
    factor = 2
    Pass = 0
    bTime, aTime = 0, 0
    for i in range(T):
        arr = list(set([random.randint(1, size*factor) for _ in range(size)]))
        arr = sorted(arr)
        piv = random.randint(1, len(arr)-1)
        arr = arr[piv:] + arr[:piv]
        piv = len(arr[piv:])
        target = random.randint(1, size*factor)
        st = time.time()
        expect = s.bfSearch(arr, target)
        end = time.time()
        bTime += (end-st)
        st = time.time()
        actual = s.search(arr, target)
        end = time.time()
        aTime += (end-st)
        verdict = expect == actual
        fpiv = s.findPivot(arr)
        if verdict: Pass += 1
        else:
            print(arr, target)
        # print("exp: {0}, actual: {1}".format(expect, actual))
        print("case #{0}: {1}".format(i+1, verdict))
    print("total: {0}/{1} pass".format(Pass, T))
    print("test size: {0}, brute-force time: {1:.3}, actual time: {2:.3}"\
            .format(size, bTime, aTime))


testSearch()
