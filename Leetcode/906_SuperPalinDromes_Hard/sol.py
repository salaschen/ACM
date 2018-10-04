import math ; 
class Solution:
    def superpalindromesInRange(self, L,R):
        '''
        :type L: str
        :type R: str
        :rtype: int (the number of super palindromes)
        '''
        result = 0; 
        L,R = int(L), int(R) ;
        low, up = math.floor(L**0.5), math.ceil(R**0.5) ;
        llen, ulen = len(str(low)), len(str(up));
        supers = [] ; # debug
        for l in range(llen, ulen+1):
            ps = self.GenPalindrome(l) ; 
            for p in ps:
                num = int(p) ; 
                nsqr = num ** 2 ; 
                if nsqr < L or nsqr > R:
                    continue ; 
                if self.IsPalindrome(str(nsqr)):
                    supers.append(str(nsqr)) ; 
                    result += 1 ;
        print(supers) ; # debug
        return result ; 

    def IsPalindrome(self, text):
        if text == "":
            return True ; 
        if len(text) == 1:
            return True ; 
        return text[0] == text[-1] and self.IsPalindrome(text[1:-1]) ; 

    def GenPalindrome(self, length, allowZero = False, First=False):
        if length <= 0:
            return [] ; 
        elif length == 1:
            return [str(x) for x in range(0, 10)] ;
        elif length == 2:
            result = [x+x for x in [str(y) for y in range(1, 10)]] ; 
            if allowZero:
                result.append('00') ; 
            return result ; 
        else:
            result = [] ; 
            if First:
                lead = [str(x) for x in [1,2,3]] ; 
            else:
                lead = [str(x) for x in range(1, 10)] ; 
            if allowZero:
                lead.append('0') ; 
            subPalindromes = self.GenPalindrome(length-2, True) ; 
            for d in lead:
                for sub in subPalindromes:
                    result.append(d+sub+d) ; 
            return result ; 
    

if __name__ == "__main__":
    s = Solution() ; 
    # print(s.GenPalindrome(4)) ; 

    print(s.superpalindromesInRange('4', '1000000000000000000')) ; 
