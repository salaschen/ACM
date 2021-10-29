class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        if len(s) == 0:
            return False 

        numList = list(map(lambda n: int(n), list(filter(lambda n: n.isnumeric(), s.split()))))
        if len(numList) == 0:
            return False
        for i in range(1, len(numList)):
            if numList[i] <= numList[i-1]:
                return False
        return True 


##### test #####
sol = Solution()
s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
print(sol.areNumbersAscending(s))

s = "hello world 5 x 5"
print(sol.areNumbersAscending(s))

s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
print(sol.areNumbersAscending(s))




