'''
Prob: Easy - Acceptance: 3513/8443
Author: Ruowei Chen
Date: 07/Dec/2021
'''
class Solution:
    def __init__(self):
        self.seenCombo = set() 
        self.numbers = set()

    def findEvenNumbers(self, digits: [int]) -> [int]:
        self.seenCombo = set()
        self.numbers = set()
        dlen = len(digits)
        for i in range(0, dlen-2):
            for j in range(i+1, dlen-1):
                for k in range(j+1, dlen):
                    lst = sorted([digits[i], digits[j], digits[k]])
                    if str(lst) in self.seenCombo:
                        continue
                    else:
                        self.seenCombo.add(str(lst))
                        temp = self.genList(lst)
                        for num in temp:
                            self.numbers.add(num)
        return sorted(list(self.numbers))

    def genList(self, numList: [int]) -> [int]:
        from itertools import permutations
        perm = permutations(numList)
        result = set() 
        for p in perm:
            if p[0] != 0 and p[2] % 2 == 0:
                temp = int(str(p[0])+str(p[1])+str(p[2]))
                result.add(temp)
        return result


### test ###
s = Solution()
digits = [2,1,3,0]
print(s.findEvenNumbers(digits))

digits = [2,2,8,8,2]
print(s.findEvenNumbers(digits))

digits = [3,7,5]
print(s.findEvenNumbers(digits))

digits = [0,2,0,0]
print(s.findEvenNumbers(digits))

digits = [0,0,0]
print(s.findEvenNumbers(digits))

digits = [3,4,8,4,2,4,9,5,4,3,2,1,1,8,1,2,2,7,0,0,5,8,3,0,3,1,9,6,4,6,9,8,4,9,6,1,1,8,4,7,4,3,6,4,7,7,3,5,9,0,5,0,8,0,5,2,9,1,3,7,5,0,6,3,9,9,8,0,7,9,2,7,6,7,6,6,6,0,3,7,7,0,5,5,8,2,4,2,1,2,8,2,3,8,5,6,1,5,1,9]
print(s.findEvenNumbers(digits))


