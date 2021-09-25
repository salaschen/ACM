class Solution:
    def sumOfBeauties(self, nums: [int]):
        nlen = len(nums) ; 
        left, right = [0 for i in range(nlen)], [0 for i in range(nlen)] ;
        left[0] = nums[0] ; 
        right[nlen-1] = nums[nlen-1] ;
        
        # scan from the left
        for i in range(1, nlen):
            if nums[i] > left[i-1]:
                left[i] = nums[i] ;
            else:
                left[i] = left[i-1] ;

        # scan from thr right
        for i in range(nlen-2, -1, -1):
            if nums[i] < right[i+1]:
                right[i] = nums[i] ; 
            else:
                right[i] = right[i+1] ; 

        result = 0 ; 
        for i in range(1, nlen-1):
            cur = nums[i] ; 
            if cur > left[i-1] and cur < right[i+1]:
                result += 2 ; 
            elif cur > nums[i-1] and cur < nums[i+1]:
                result += 1 ; 
            # print("cur={0}, result={1}".format(cur, result)) ; # debug

        # print('left:', left) ; # debug
        # print('right:', right) ; # debug
        return result ; 

s = Solution() ; 
nums = [1,2,3] ;
print('expect: 2', s.sumOfBeauties(nums)) ; 
nums = [2,4,6,4] ;
print('expect: 1', s.sumOfBeauties(nums)) ; 
nums = [3,2,1] ;
print('expect: 0', s.sumOfBeauties(nums)) ; 

