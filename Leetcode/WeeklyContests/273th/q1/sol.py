class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        from functools import reduce
        temp = (list(str(num)))
        temp.reverse()
        temp = reduce(lambda a,b: a+b, temp, '')
        
        temp = int(temp)
        temp = (list(str(temp)))
        temp.reverse()
        temp = reduce(lambda a,b: a+b, temp, '')
        temp = int(temp)

        return temp == num


### test ###
s = Solution()
num = 526
print(s.isSameAfterReversals(num))
num = 0 
print(s.isSameAfterReversals(num))
num = 1800 
print(s.isSameAfterReversals(num))
