'''
Prob: 13 - Easy - Roman to Integer
Author: Ruowei Chen
Date: 31/Dec/2019
'''
import lib ; 

class Solution:
    def __init__(self):
        syms = [('I', 1), ('V',5), ('X',10), ('L',50),\
                ('C',100),('D',500),('M',1000)] ; 
        self.symbols = dict() ; 
        for (key, value) in syms:
            self.symbols[key] = value ; 
        return ; 

    def romanToInt(self, s: str) -> int:
        cur = 0 ; 
        slen = len(s) ; 
        result = 0 ;
        while cur < slen:
            # subtraction case.
            if cur+1 < slen and \
                self.symbols[s[cur]] < self.symbols[s[cur+1]]:
                result += (self.symbols[s[cur+1]]-self.symbols[s[cur]]) ; 
                cur += 2 ; 
            else:
                result += self.symbols[s[cur]] ;
                cur += 1 ; 
        return result ; 


########### test ##############
romans = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV'] ; 
s = Solution() ; 
for roman in romans:
    print('{0} => {1}'.format(roman, s.romanToInt(roman))) ; 

gen = lib.Solution() ; 
Pass = 0 ; 
for i in range(1, 4000):
    roman = gen.intToRoman(i) ; 
    num = s.romanToInt(roman) ;
    if num == i:
        Pass += 1 ; 
print('{0}/{1} cases passed'.format(Pass, 3999)) ; 