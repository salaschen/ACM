'''
Prob: 12 - medium - Integer to Roman
Author: Ruowei Chen
Date: 30/Dec/2019
'''

class Solution:
    def __init__(self):
        symbolList = [(1,'I'), (5,'V'), (10,'X'), (50, 'L'), \
            (100, 'C'), (500, 'D'), (1000, 'M'), \
            (4, 'IV'), (9, 'IX'), (40, 'XL'), (90, 'XC'), \
            (400,'CD'), (900,'CM')] ; 
        self.symbols = dict() ; 
        for (value, sym) in symbolList:
            self.symbols[value] = sym ; 
        
        return ;        

    def intToRoman2(self, num: int) -> str:
        result = '' ; 
        result += (num // 1000) * 'M' ; 
        num = num % 1000 ; 
        base = 100 ; 
        while base > 0:
            result += self.helper( num, base) ; 
            num = num % base ; 
            base = base // 10 ; 
        return result ;
    
    def helper(self, num, base):
        count = num // base ; 
        if count == 0: return ''; 
        result = '' ; 
        if count == 9 or count == 4:
            result += self.symbols[count * base] ; 
        else:
            if count >= 5:
                result += self.symbols[5 * base] ; 
            result += (count % 5) * self.symbols[base] ; 
        return result ; 

    # iterate solution
    def intToRoman(self, num: int) -> str:
        result = '' ; 
        thousand = num // 1000 ; 
        if thousand > 0:
            result += thousand * 'M' ; 
        
        num = num % 1000 ; 
        hundred = num // 100 ; 
        if hundred > 0:
            if hundred == 9 or hundred == 4:
                result += self.symbols[hundred * 100] ; 
            else:
                if hundred >= 5:
                     result += 'D'
                result += (hundred % 5) * 'C' ; 
        
        num = num % 100 ; 
        tenth = num // 10 ; 
        if tenth > 0:
            if tenth == 9 or tenth == 4:
                result += self.symbols[tenth*10] ; 
            else:
                if tenth >= 5:
                    result += 'L' ; 
                result += (tenth % 5) * 'X' ; 

        num = num % 10 ; 
        single = num  ; 
        if single > 0:
            if single == 9 or single == 4:
                result += self.symbols[single] ; 
            else:
                if single >= 5:
                    result += 'V' ; 
                result += (single % 5) * 'I' ; 
        return result ; 


############ test ############
def main():
    nums = [1,2,3,4,5,6,7,8,9,\
        10,11,12,13,14,15,16,17,18,19,20,\
        3,4,9,58,1994, 3999] ; 
    s = Solution() ; 
    print(list(map(lambda n: s.intToRoman(n), nums))) ; 
    print(list(map(lambda n: s.intToRoman2(n), nums))) ; 

    allPass = True ; 
    for i in range(1, 4000):
        str1, str2 = s.intToRoman(i), s.intToRoman2(i) ; 
        if str1 != str2:
            print('error for {0}, expect {1}, actual {2}'.format(i, str1, str2)) ; 
            allPass = False ; 
    if allPass:
        print('All test passed.') ; 
    return ; 

if __name__ == "__main__":
    main() ; 