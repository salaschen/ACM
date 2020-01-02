'''
Prob: 16 - Medium - 3 Sum closest
Author: Ruowei Chen
Date: 02/Dec/2019
Note:
    1) implement a closest binary search on a subarray. 
    2) After 3 attemps, finally implement a slow solution.
'''
import random 

class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
        result = None ; 
        nlen = len(nums) ; 
        nums = sorted(nums) ; 
        for i in range(0, nlen-2):
            for j in range(i+1, nlen-1):

                '''
                if nums[i]+nums[j] > target and result is not None:
                    break ; # try the next i.
                '''
                '''
                if (target-nums[i]-nums[j]) < nums[j+1] and result is not None:
                    break ; 
                '''
                third = self.searchClosest(nums[j+1:], target-nums[i]-nums[j]) ; 
                threeSum = nums[i]+nums[j]+third ; 
                if threeSum == target: return target ; 
                if result is None or abs(threeSum-target) < abs(result-target):
                    result = threeSum ; 
        return result ; 

    def searchClosest(self, nums:[int], target: int) -> int:
        if len(nums) == 0: return None ; 
        if len(nums) < 10:
            minDist = min(list(map(lambda n: abs(n-target), nums))) ; 
            return (list(filter(lambda n: abs(n-target) == minDist, nums)))[0] ;

        # now for large arrays.
        low,up = 0, len(nums)-1 ; 
        if nums[low] == target or nums[up] == target: 
            return target ; 

        minDist = min(abs(nums[low]-target), abs(nums[up]-target)) ; 
        result = (list(filter(lambda n: abs(n-target) == minDist, [nums[low], nums[up]])))[0]; 

        while low < up-1:
            mid = (low+up)//2 ; 
            if nums[mid] == target:
                return nums[mid] ; 
            if abs(nums[mid]-target) < minDist:
                minDist = abs(nums[mid]-target) ; 
                result = nums[mid] ; 
            # print('minDist={0}, result={1}'.format(minDist, result)) ; # debug
            if nums[mid] > target:
                up = mid ; 
            else:
                low = mid ; 
        return result ; 

############ test #########
def bruteForce(nums: [int], target: int) -> int:
    nlen = len(nums) ; 
    result = None ; 
    for i in range(0, nlen-2):
        for j in range(i+1, nlen-1):
            cur = nums[i]+nums[j] ; 
            for k in range(j+1, nlen):
                threeSum = cur+nums[k] ; 
                if threeSum == target: return threeSum; 
                if result is None or abs(threeSum-target) < abs(result-target):
                    result = threeSum ;
    return result ; 

def test2():
    s = Solution() ; 
    nums = [-43,61,-62,24,73,64,-23,94,-65,-27,24,-56,8,54,0,19,-100,-64,-53,6,-22,13,-18,55,-41,37,34,-43,0,-8,-95,76,73,21,-93,16,98,60,70,-32,30,-7,-27,-73,79,-26,41,32,41,-5,82,-14,50,-94,22,62,60,-48,51,12,-34,68,-40,-20,-20,46,46,-79,1,82,-98,41,-79,-43,-76,-25,-94,-16,-25,46,-95,-79,53,-1,-30,43,93,17,72,66,83,-89,-16,42,40,87,-46,40,22,85,-91,46,-77,19,-56,-28,8,47,-20,65,8,60,-49,-86,-74,56,30,79,97,-89,14,-90,66,-12,-57,46,-61,87,72,13,75,75,36,79,-16,84,-49,-86,76,68,-8,-65,-86,-11,55,-69,-59,34,63,59,-11,43,16,7,93,57,-55,2,38,64,3,22,-9,-22,-34,-84,90,-71,-88,64,-19,13,-8,-81,-95,-38,-9,-25,82,57,60,-26,66,21,8,65,-38,-68,-59,24,91]
    nums = sorted(nums) ; 
    print(nums) ; # debug
    target = -231 
    print('expect={0}'.format(bruteForce(nums, target))) ; 
    print('target={0}, result={1}'.format(target, s.threeSumClosest(nums, target))) ; 
    return ; 

def test():
    times = 200 ; 
    size = 200 ; 
    s = Solution() ; 
    Pass = 0 ;
    for i in range(times):
        nums = [random.randint(-1*size, 1*size) for x in range(size)] ; 
        target = random.randint(-5*size, 5*size) ; 
        expect = bruteForce(nums, target) ; 
        actual = s.threeSumClosest(nums, target) ; 
        if expect == actual: Pass += 1 ; 
        else:
            print('Error: expect {0}, actual {1}'.format(expect, actual)) ; 
    print('{0}/{1} passed.'.format(Pass, times)) ; 
    return ; 

test() ; 