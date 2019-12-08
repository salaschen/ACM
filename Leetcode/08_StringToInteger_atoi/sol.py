'''
Prob: Medium 08 String to Integer (atoi)
Author: Ruowei Chen
Date: 08/Dec/2019
'''
class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.lstrip() ; # get rid of all the white spaces.

        # invalid if not start with a sign or number
        if len(string) == 0 or (not string[0].isdigit() and not string[0] in ['-','+']):
            return 0 ; 

        # states
        ReadNumOrSign = 0 ; 
        ReadNum = 1 ; 
        State = ReadNumOrSign ; 
        numString = '' ; 
        curPos = 0 ; 
        isNegative = False ; 
        while curPos < len(string):
            cur = string[curPos] ; 
            if cur.isdigit():
                if State == ReadNumOrSign:
                    State = ReadNum ; 
                numString += cur ; 

            elif cur in '-+':
                if State == ReadNumOrSign:
                    State = ReadNum ; 
                    if cur == '-':
                        isNegative = True ; 
                    numString += cur ; 
                else: # not expecting signs.
                    break ; 
            else:
                # non sign or digit.
                break ; 
            curPos += 1 ;    
        
        # print(numString) ; # debug
        if len(numString) == 0: return 0 ;
        if len(numString) == 1 and numString[0] in '-+': return 0 ;  # only sign.
        number = int(numString) ; 
        int_min = - (2 ** 31) ; 
        int_max = (2 ** 31) - 1 ;
        if number < int_min: number = int_min ; 
        if number > int_max: number = int_max ; 
        return number ; 

######### Test ###########
def test():
    s = ['42', '  -42', '   ', '+.5', '4193 with words', 'words with 41', \
        '-55words', '+-500', '+052', '-2.5', '+2147483648', '-2147483648',\
        '-21484836488']; 
    sol = Solution() ;
    for n in s:
        print('{0} -> {1}'.format(n, sol.myAtoi(n))) ; 
    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    main() ;
