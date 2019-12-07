'''
Prob: Medium 05 - Longest Palindromic Substring
Author: Ruowei Chen
Date: 08/Dec/2019
Note: 
    1) O(N^2) solution, linear scan.
'''
import random

class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s) ; 
        if slen == 0:
            return '' ;
        result = s[0] ; 
        length = 1 ;

        for pos in range(0, slen-1):
            # 1 if s[pos]==s[pos+1], we can use the s[pos] and s[pos+1]
            # both as the middle to grow outwards.
            if s[pos] == s[pos+1]:
                head = pos-1 ; 
                tail = pos+2 ; 
                while head >= 0 and tail < slen:
                    if s[head] == s[tail]:
                        head -= 1 ;
                        tail += 1 ; 
                    else:
                        break ;
                if s[head+1] == s[tail-1]:
                    if tail-head-1 > length:
                        length = tail-head-1 ; 
                        result = s[head+1:tail] ;

            # 2 just use s[pos] as the middle to grow outwards
            head,tail = pos-1,pos+1 ; 
            while head >= 0 and tail < slen:
                if s[head] == s[tail]:
                    head -= 1 ;
                    tail += 1 ; 
                else:
                    break ;

            if s[head+1] == s[tail-1]:
                if tail-head-1 > length:
                    length = tail-head-1 ; 
                    result = s[head+1:tail] ;

        return result ; 


###### Test #########
def genLongword(size, small=False):
    result = '' ;
    charSet = [chr(x) for x in range(ord('a'), ord('z')+1)] ; 
    if small:
        charSet =[chr(x) for x in range(ord('a'), ord('g')+1)] ; 
    for i in range(size):
        result += random.choice(charSet) ; 
    return result ; 

def isPalindrom(s):
    if len(s) <= 1:
        return True ; 
    return s[0] == s[-1] and isPalindrom(s[1:-1]) ;

def test():
    s = Solution() ; 
    string = 'babad' ;
    print(s.longestPalindrome(string)) ; 
    string = 'cbbd' ;
    print(s.longestPalindrome(string)) ; 
    string = 'abcdefedcbae' ;
    print(s.longestPalindrome(string)) ; 
    string = 'a' ;
    print(s.longestPalindrome(string)) ; 
    string = 'ea' ;
    print(s.longestPalindrome(string)) ; 
    string = 'aa' ;
    print(s.longestPalindrome(string)) ; 
    string = '' ;
    print(s.longestPalindrome(string)) ; 

    times = 100 ;
    count = 0 ; 
    for i in range(times):
        word = genLongword(100, True) ;
        palindrome = s.longestPalindrome(word) ; 
        if isPalindrom(palindrome):
            count += 1 ; 
            print(word) ; 
            print(palindrome) ; 
    print('palindrome found: {0}/{1}'.format(count, times)) ; 
    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    main() ; 
