'''
Prob: Leetcode 1262 Medium
Author: Ruowei Chen
Date: 17/Nov/2019
'''

class Solution:
    def maxSumDivThree(self, nums: [int]) -> int:
        one = [] ;
        two = [] ; 
        for num in nums:
            mode = num % 3 ; 
            if mode == 1:
                one.append(num) ; 
            elif mode == 2:
                two.append(num) ; 
        one = sorted(one) ; 
        two = sorted(two) ; 
        total = sum(nums) ; 
        if total % 3 == 0:
            return total ;       
        elif total % 3 == 1:
            candidate = [] ; 
            if len(one) != 0:
                candidate.append(one[0]) ; 
            if len(two) >= 2:
                candidate.append(two[0]+two[1]) ; 
            return total - min(candidate) ; 
        elif total % 3 == 2:
            candidate = [] ; 
            if len(one) >= 2:
                candidate.append(one[0]+one[1]) ; 
            if len(two) > 0:
                candidate.append(two[0]) ; 
            return total - min(candidate) ; 
        else:
            return 0 ; 

#### test ###
def main():
    s = Solution() ; 
    nums = [[3,6,5,1,8], [4],[1,2,3,4,4],\
        [7,2,2,2,3], [1,2,2,2,3], [0],\
        [7,1,2,5,2,2,3],] ; 
    for numList in nums:
        print('Input: {0}'.format(numList)); 
        print('Output: {0}'.format(s.maxSumDivThree(numList))) ; 
        print() ; 
    return ; 

if __name__ == "__main__":
    main() ; 