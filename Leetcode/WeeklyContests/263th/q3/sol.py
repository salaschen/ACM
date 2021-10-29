from functools import reduce
class Solution:
    def __init__(self):
        self.maxOr = None 
        self.count = 0 

    def countMaxOrSubsets(self, nums: [int]) -> int:
        snums = sorted(nums)
        self.count = 0 
        # calculate the maximum or
        self.maxOr = reduce(lambda x,y: x | y, snums)

        self.df(snums, [])
        # debug
        # print(self.subsets)
        return self.count  

    def df(self, nums:[int], cur: [int]):
        if len(nums) == 0:
            if len(cur) == 0:
                return 
            '''
            if curString in self.subsets:
                return
            '''
            temp = reduce(lambda x,y: x | y, cur)
            if temp == self.maxOr:
                self.count += 1

        else:
            self.df(nums[1:], cur+[nums[0]])
            self.df(nums[1:], cur)

    
### test ###
s = Solution()
nums = [3,1]
print(s.countMaxOrSubsets(nums))

nums = [2,2,2]
print(s.countMaxOrSubsets(nums))


nums = [3,2,1,5]
print(s.countMaxOrSubsets(nums))

