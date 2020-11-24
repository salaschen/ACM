'''
Leetcode 1567 Medium
    Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
    A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
    Return the maximum length of a subarray with positive product.
Author: Ruowei Chen
Date: 24/Nov/2020
'''
import random
import time

class Solution:
    def getMaxLen(self, nums: [int]) -> int:
        return max(list(map(lambda subarray: self.getMaxSubarray(subarray), self.splitByZero(nums))))

    # [int] -> int
    # interp. get the length of the longest subarray which product was positive
    # assume the array doesn't contain zero. 
    def getMaxSubarray(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0

        negIndex = []
        for i in range(len(nums)):
            if nums[i] < 0:
                negIndex.append(i)

        # if no negative numbers in the array, include all the numbers.
        if len(negIndex) == 0:
            return len(nums)

        # even number of negative numbers in the array
        # include all the numbers
        if len(negIndex) % 2 == 0:
            return len(nums)

        first, last = negIndex[0], negIndex[-1]
        return max(0, last, len(nums)-first-1)

    # [int] -> [[int]
    # interp. split the list into a list of list by using 0 as the separator. 
    # tested
    def splitByZero(self, nums: [int]) -> [[int]]:
        result = []
        cur = []
        for num in nums:
            if num == 0:
                if len(cur) > 0:
                    result.append(cur)
                    cur = []
            else:
                cur.append(num)
        if len(cur) > 0:
            result.append(cur)
        if len(result) == 0:
            result.append([])
        return result

#### testing functions
def testSplitByZero():
    s = Solution()
    a = [0,1,2,3,0,5,6,0,9,-1,-2,8,0]
    b = s.splitByZero(a)
    print(b)
    expect = [[1,2,3],[5,6],[9,-1,-2,8]]
    print(b == expect)

def testGetMaxLen():
    s = Solution()
    nums = [1,-2,-3,4]
    print(nums)
    print(s.getMaxLen(nums))
    print(bruteForce(nums))

    nums = [0,1,-2,-3,-4]
    print(nums)
    print(s.getMaxLen(nums))
    print(bruteForce(nums))

    nums = [-1,-2,-3,0,1]
    print(nums)
    print(s.getMaxLen(nums))
    print(bruteForce(nums))

    nums = [-1, 2]
    print(nums)
    print(s.getMaxLen(nums))
    print(bruteForce(nums))

    nums = [1,2,3,5,-6,4,0,10]
    print(nums)
    print(s.getMaxLen(nums))
    print(bruteForce(nums))

    nums = [0,0,0,0,0]
    print(nums)
    print(s.getMaxLen(nums))
    print(bruteForce(nums))



# brute-force version
# used for testing
def bruteForce(nums: [int]) -> int:
    result = 0
    for i in range(len(nums)):
        start = i
        product = 1 
        cur = i 
        length = 0
        while cur < len(nums):
            product *= nums[cur]
            if product > 0:
                length = (cur-start+1)
            elif product == 0:
                break
            cur += 1
        result = max(length, result)
    return result

def testWithBruteForce():
    Times = 100
    s = Solution()
    Pass = 0
    bTime, fTime = 0, 0
    for i in range(Times):
        size = random.randint(10, 1000)
        # generate an random array
        array = [random.randint(-100, 100) for i in range(size)]
        start = time.time()
        expect = bruteForce(array)
        end = time.time()
        bTime += (end - start)
        start = time.time()
        result = s.getMaxLen(array)
        end = time.time()
        fTime += (end - start)
        if result == expect:
            Pass += 1
        else:
            print("array:", array)
            print("expect = {0}, actual = {1}".format(expect, result))
    print("test: {0}/{1} passed".format(Pass, Times))
    print("brute-force: {0:.2} sec, solution: {1:.2} sec".format(bTime, fTime))
    return


def main():
    testGetMaxLen()
    # testWithBruteForce()
    return

if __name__ == "__main__":
    main()
