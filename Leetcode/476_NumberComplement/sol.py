'''
Prob: 476 Number Complement - Easy
Author: Ruowei Chen
Date: 27/Dec/2021
Note:
    1) Find the number of bits for this target. (5 -> 101 -> 3 bits)
    2) Then find the maximum number these bits can represent (3 bits -> 111 -> 7)
    3) subtract the max by target (7-5=2 -> 010), which is the bit-complement of the target.
'''
class Solution:
    def findComplement(self, num: int) -> int:
        from math import log,floor 
        numbits = floor(log(num, 2)) + 1
        maximum = (1 << (numbits)) - 1
        return maximum - num


### test ###
s = Solution()
num = 5
print(s.findComplement(num))

num = 1
print(s.findComplement(num))

num = 2
print(s.findComplement(num))

num = 3
print(s.findComplement(num))

num = 15 
print(s.findComplement(num))

