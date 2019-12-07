'''
Prob: Leetcode 128 - Longest Consecutive Sequence
Level: Hard
Author: Ruowei Chen
Note: 
    1) Need to be O(n) complexity.
    2) AC on the second time, first time missed the empty case.
    3) Coded the official solution and compare the performance. My implementation does run on O(N) complexity,
    as shown by the performance test, just on a slower speed than the official implementation.
'''
import random ; 
import time ; 

class Solution:
    def longestConsecutive2(self, nums:[[int]]) -> int:
        '''official'''
        if len(nums) == 0:
            return 0 ; 

        numSet = set(nums) ; 
        longestStreak = 1 ; 
        for num in numSet:
            if num-1 not in numSet:
                currentStreak = 1 ; 
                cur = num ; 
                while cur+1 in numSet:
                    currentStreak += 1 ; 
                    cur += 1 ;
                longestStreak = max(currentStreak, longestStreak) ; 
        return longestStreak ; 

    def longestConsecutive(self, nums: [[int]]) -> int:
        '''Personal'''
        length = dict() ;        
        result = 0 ; 
        for i in range(len(nums)):
            num = nums[i] ; 

            if num in length:
                continue ; 

            # by default set the length of the sequence to 1.
            length[num] = 1 ; 
            if length[num] > result:
                result = length[num] ;

            # merge with the left side
            if (num-1) in length:
                leftMostIndex = num-length[num-1] ; 
                length[leftMostIndex] += 1 ; 
                length[num] = length[leftMostIndex] ; 
                if length[num] > result:
                    result = length[num] ; 

            # merge with the right side
            if (num+1) in length:
                rightMostIndex = num+length[num+1] ; 
                length[rightMostIndex] += length[num] ; 
                leftMostIndex = num-length[num] + 1 ; 
                length[leftMostIndex] = length[rightMostIndex] ; 
                if length[leftMostIndex] > result:
                    result = length[leftMostIndex] ; 

        return result ; 

###### Test #####
def performanceCompare():
    s = Solution() ; 
    m1, m2 = s.longestConsecutive, s.longestConsecutive2 ; 
    for size in [100,1000,10000,100000,200000,400000]:
        case = genCase(size) ; 
        r1, t1 = runCase(m1, case) ; 
        r2, t2 = runCase(m2, case) ; 
        ok = 'passed' if r1 == r2 else 'failed' ;
        print('size {0} {1}: {2} - {3:.3} milliseconds, {4} - {5:.3} milliseconds'.\
        format(size, ok, m1.__doc__, t1*1000, m2.__doc__, t2*1000 ))

    pass ; 

def runCase(method, case=[]) -> (int, float):
    startTime = time.time() ; 
    result = method(case) ; 
    endTime = time.time() ; 
    costTime = (endTime-startTime) ;
    return (result, costTime)
    
def genCase(size=100):
    lst = [random.randint(0, size*2) for x in range(size)]  ; 
    return lst ; 


def test():
    s = Solution() ; 
    l = [100,4,200,1,3,2] ; 
    cases = [] ; 
    cases.append((l, 4)) ; 
    cases.append(case1()) ; 
    cases.append(case2()) ; 
    cases.append(case3()) ;

    passed = 0 ; 
    for case in cases:
        l, expected = case ; 
        result = s.longestConsecutive(l) ; 
        if result == expected:
            passed += 1 ; 

    print('tests： {0}/{1} passed.'.format(passed, len(cases))) ; 
    return ;

def case1():
    l = [x for x in range(0, 100000,2)] ; 
    expected = 1 ; 
    return (l, expected) ; 

def case2():
    expected = 977 ; 
    l1 = [x for x in range(1, expected+1)] ; 
    l2 = [y for y in range(expected+2, expected*2-100)] ; 
    l = l1+l2 ; 
    random.shuffle(l) ; 
    return (l, expected) ; 
    
def case3():
    l = [] ; 
    expected = 0 ; 
    return (l, expected) ;

def main():
    # test() ; 
    performanceCompare() ; 
    return ;

if __name__ == "__main__":
    main() ; 