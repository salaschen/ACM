'''
Prob: 540 - Medium.
Author: Ruowei Chen
Date: 21/Nov/2021
'''
import random
import time
class Solution:
    # O(logn) time complexity
    def singleNonDuplicate(self, nums:[int]) -> int:
        nlen = len(nums)
        if nlen == 1:
            return nums[0]
        
        up = nlen-1
        low = 0
        while True:
            mid = (up + low) // 2
            if low == up:
                return nums[low]

            if nums[mid] == nums[mid+1]:
                if mid % 2 == 0:
                    low = mid+2
                else:
                    up = mid-1
            elif nums[mid] == nums[mid-1]:
                if mid % 2 == 0:
                    up = mid-2
                else:
                    low = mid+1
            else:
                return nums[mid]
        return None

    # O(N) time complexity
    def bruteForce(self, nums:[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1] 

### test ###
def caseTest():
    s = Solution()
    nums = [1,1,2,3,3,4,4,8,8]
    print(s.singleNonDuplicate(nums))
    print(s.bruteForce(nums))

    nums = [3,3,7,7,10,11,11]
    print(s.singleNonDuplicate(nums))
    print(s.bruteForce(nums))

def randomTest():
    s = Solution()
    times = 100
    bfTime, solTime = 0,0
    count = 0
    size = 10000
    for i in range(times):
        single = set()
        while len(single) < size:
            single.add(random.randint(0, size * 100))

        double = sorted(list(single) + list(single))
        pos = random.randint(0, len(double)-1)
        expect = double[pos]
        double = double[:pos] + double[pos+1:]
        start = time.time()
        bf = s.bruteForce(double)
        end = time.time()
        bfTime += (end-start)
        start = time.time()
        output = s.singleNonDuplicate(double)
        end = time.time()
        solTime += (end-start)
        
        if bf == expect and output == expect:
            count += 1
        else:
            print(expect, output, bf)
            print(double)

    print("pass: {0}/{1}".format(count,times))
    print("bf time: {0}".format(bfTime))
    print("sol time: {0}".format(solTime))
    return

   
caseTest()
# randomTest()

