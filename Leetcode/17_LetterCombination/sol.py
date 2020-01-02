'''
Prob: 17 - Medium - Letter Combinations of a Phone Number
Author: Ruowei Chen
Date: 02/Jan/2020
'''
class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0: return [] ; 
        temp = [(2,'abc'),(3,'def'),(4,'ghi'),(5,'jkl'),\
            (6,'mno'),(7,'pqrs'),(8,'tuv'),(9,'wxyz')] ; 
        Map = dict() ; 
        for (key, value) in temp:
            Map[key] = value ; 
        return self.helper(digits, Map) ; 

    def helper(self, digits: str, Map) -> [str]:
        if len(digits) == 0:
            return [''] ; 
        tail = self.helper(digits[1:], Map) ; 
        result = [] ; 
        curLetters = Map[int(digits[0])] ;
        for word in tail:
            for letter in curLetters:
                result.append(letter + word) ; 
        return result ; 


##### Test ######
def test():
    # digits = '23456789' ;
    digits=  '9' ; 
    s = Solution() ; 
    print(s.letterCombinations(digits)) ; 

test() ; 