'''
Prob: Leetcode 128 - Longest Consecutive Sequence
Level: Hard
Author: Ruowei Chen
Note: 
    1) Need to be O(n) complexity.
'''
import random ; 

class Solution:
    def longestConsecutive(self, nums: [[int]]) -> int:
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
    test() ; 

if __name__ == "__main__":
    main() ; 