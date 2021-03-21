'''
Prob: Leetcode 1793 Maximum Score of a Good Subarray - hard
Author: Ruowei Chen
Date: 21/03/2021
'''
import random
class Solution:
    def evalElemAndElem(self, elem1: (int, int), elem2: (int, int)) -> int:
        return (max(elem1[0], elem2[0])-min(elem1[0], elem2[0])+1) * \
                min(elem1[1], elem2[1]); 

    def evalListAndElem(self, elem: (int, int), lst: [(int, int)]) -> int:
        return max(list(map(lambda e: self.evalElemAndElem(elem, e), lst))) ;

    def evalLists2(self, target: [(int, int)], bound: [(int, int)]) -> int:
        i, j = 0, 0 ; 
        tlen, blen = len(target), len(bound) ; 
        result = 0 ; 
        while i < tlen and j < blen and j >= 0:
            cur_t, cur_b = target[i], bound[j] ; 
            if cur_t[1] > cur_b[1]:
                if j > 0 and cur_t[1] < bound[j-1][1]:
                    result = max(result, self.evalElemAndElem(cur_t, bound[j-1])) ;
                i += 1 ;
            else: # cur_t[1] < cur_b[1]
                result = max(result, self.evalElemAndElem(cur_t, cur_b)) ; 
                j += 1 ;

        # if bound elements have been exhausted, there is still possibility that
        # the target elements can have better score. 
        if j == blen:
            result = max(result, self.evalListAndElem(bound[-1], target[i:])) ;

        # if the target elements have been exhausted, then no need to check further. 
        else:
            result = result ; 
        return result ;

    def evalLists(self, left: [(int,int)], right: [(int, int)]) -> int:
        i, j = 0, 0 ; 
        llen, rlen = len(left), len(right) ; 
        result = 0 ; 
        while i < llen and j < rlen:
            le, re = left[i], right[j] ; 
            result = max(result, self.evalElemAndElem(le, re)) ; 
            if le[1] < re[1]:
                j += 1 ;
            else:
                i += 1 ;
        if i == llen:
            result = max(result, self.evalListAndElem(left[-1], right[j:])) ; 
        else:
            result = max(result, self.evalListAndElem(right[-1], left[i:])) ; 
        return result ; 

    def maximumScore(self, nums: [int], k: int) -> int:
        nlen = len(nums) ; 
        if nlen == 1:
            return nums[0] ; 

        left, right = [], [] ; 
        
        # build up the left queue
        i, cur = k, nums[k] ; 
        while i > 0:
            if cur > nums[i-1]:
                left.append((i, cur)) ;
                cur = nums[i-1] ;
                i = i - 1 ; 
            else:
                i = i - 1 ;
        left.append((i, cur)) ; # add the last element

        # build up the right queue
        j, cur = k, nums[k] ;
        while j < nlen-1:
            if cur > nums[j+1]:
                right.append((j, cur)) ; 
                cur = nums[j+1] ; 
                j = j + 1 ;
            else:
                j = j + 1 ;
        right.append((j, cur)) ;  # add the last element
        # print(left) ; # debug
        # print(right) ; # debug
        # print('evalList:{0}, {1}'.format(left[0], right), \
        #         self.evalListAndElem(left[0], right)) ;  # debug
        result = self.evalLists2(left, right) ; 
        result = max(result, self.evalLists2(right, left)) ; 

        return result ; 

    # the most brute force version.
    # tested
    def bruteforce(self, nums: [int], k: int) -> int:
        result = 0;
        nlen = len(nums) ; 
        for i in range(0, k+1):
            for j in range(k, nlen):
                minNum = min(nums[i:j+1]) ; 
                temp = minNum*(j-i+1) ; 
                if temp > result:
                    # print("bf: i={0},j={1}, minNum={2}".format(i, j, minNum)) ;
                    # print("temp={0}".format(temp)) ;
                    result = temp ; 
        return result ; 

def testSmall():
    s = Solution() ; 
    '''
    nums = [1,4,3,7,4,5] ;
    k = 3 ;
    print(s.bruteforce(nums, k)) ; 
    print(s.maximumScore(nums, k)) ; 
    nums = [5,5,4,5,4,1,1,1] ;
    k = 0 ; 
    print(s.bruteforce(nums, k)) ; 
    print(s.maximumScore(nums, k)) ; 
    nums = [100] ; 
    k = 0 ;
    print(s.bruteforce(nums, k)) ; 
    print(s.maximumScore(nums, k)) ; 
    '''
    nums = [84, 66, 3, 81, 62, 94, 48, 38, 47, 96] ;
    k = 6 ;
    print("nums={0}, k={1}".format(nums, k)) ;
    print("bf:", s.bruteforce(nums, k)) ; 
    print("mx:", s.maximumScore(nums, k)) ; 

    return ;

def genCase(upper, size=1000) -> ([int], int):
    nums = [random.randint(1, upper) for x in range(size)] ;
    k = random.randint(0, size-1) ;
    return (nums, k) ;

def testMedium():
    s = Solution() ;
    times = 1 ;
    count = 0 ; 
    upper = 10000 ;
    size = 1000 ;
    for i in range(times):
        nums, k = genCase(upper, size) ;
        expect = s.bruteforce(nums, k) ;
        actual = s.maximumScore(nums, k) ;
        if expect != actual:
            print("nums={0}, k={1}, expect={2}, actual={3}".\
                    format(nums, k, expect, actual)) ;
        else:
            count += 1 ;
    print("test passed {0}/{1}".format(count, times))
    return ;

def test():
    # testSmall() ;
    testMedium() ; 

if __name__ == "__main__":
    test() ; 


