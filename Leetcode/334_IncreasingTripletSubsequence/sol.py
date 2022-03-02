'''increasingTriplet
Prob: 334 - Medium
Author: Ruowei Chen
Date: 02/Mar/2022
Note: 
    1) Use a state machine
'''
class Solution:
    def __init__(self):
        return

    def increasingTriplet(self, nums: [int]) -> bool:
        self.stacks = []
        self.state = 'empty'
        for i in range(len(nums)):
            cur = nums[i]
            # print(f'state: {self.state}, stacks: {self.stacks}') # debug
            if self.fillStack(cur):
                return True
        return False

    # whether a triplet is found
    def fillStack(self, cur: int) -> bool:
        # no number is recorded. 
        if self.state == 'empty':
            self.stacks.append([cur])
            self.state = 'one'
            return False

        # only one number is recorded.
        if self.state == 'one':
            stack = self.stacks[0]
            if cur < stack[0]:
                stack[0] = cur
            elif cur > stack[0]:
                stack.append(cur)
                self.state = 'two'
            return False

        # two numbers are recorded.
        if self.state == 'two':
            stack = self.stacks[0]

            # a triplet is found, return Success.
            if cur > stack[1]:
                return True

            # replace the second number
            elif cur > stack[0] and cur < stack[1]:
                stack[1] = cur
                return False

            # can record this number as well.
            elif cur < stack[0]:
                self.stacks.append([cur])
                self.state = 'three'

            return False

        # three numbers are recorded.
        if self.state == 'three':
            stack = self.stacks[0] 

            # a triplet is found, return Success
            if cur > stack[1]:
                return True

            # when it's in the middle between first and second number
            # replace the second number
            if cur > stack[0] and cur < stack[1]:
                stack[1] = cur
                return False

            # can check if it can be added to the second stack
            if cur <= stack[0]:
                stack2 = self.stacks[1]
                
                # the cur can be added into the second stack and the 
                # first stack can be discarded.
                if cur > stack2[0]:
                    stack2.append(cur)
                    self.stacks = self.stacks[1:]
                    self.state = 'two'
                    return False

                # it can replace the smallest number in the second stack
                if cur < stack2[0]:
                    stack2[0] = cur
                    return False

            return False
        
        return False
    

### test ###
def randomTest():
    pass

def caseTest():
    s = Solution()
    nums = [1,2,3,4,5]
    print(s.increasingTriplet(nums))

    nums = [5,4,3,2,1]
    print(s.increasingTriplet(nums))

    nums = [2,1,5,0,4,6]
    print(s.increasingTriplet(nums))

    nums = [2,4,-2,-3]
    print(s.increasingTriplet(nums))

caseTest()
