'''
Prob: Hard - 10 Regular Expression Matching
Author: Ruowei Chen
Date: 08/Dec/2019
Note: 
    1) Using DP to solve. 
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # using the [set()] to store which positions can a certain 
        # pattern matching character can match.
        # for example, s -> 'aaba', p -> 'a*', then
        # we have dp[1] = set(None,3,2,1,0) because * can match all the way back to the front.
        # and dp[0] -> (1, 0, 3), because 'a' can match the 'a' in s.

        # invalid format.
        if len(p) == 0: 
            if len(s) == 0:
                return True ; 
            else:
                return False ; 
        
        if '**' in p or p[0] == '*': return False ; 

        dp = [set([len(s)])] ; 
        # begin from the tail.
        # for i in range(len(p)-1, -1, -1):
        i = len(p)-1 ; 
        while i >= 0:
            cur = p[i] ; 
            prev = dp[-1] ; 
            if cur == '*':
                i -= 1 ; 
                cur = p[i] ; 
                values = set() ; 
                for val in prev:
                    values.add(val) ; # use 0 occurrence to match.
                    val -= 1 ;
                    while val >= 0 and (cur == s[val] or cur == '.'):
                        values.add(val) ; 
                        val -= 1 ; 
                dp.append(values) ; 
            elif cur == '.':
                values = list(filter(lambda num: num >=0, map(lambda v: v-1, prev))) ; 
            else: # cur is normal character
                values = []
                for val in prev:
                    if val-1 >= 0 and s[val-1] == cur:
                        values.append(val-1) ; 
            dp.append(values) ;                
            i -= 1 ; 

        if 0 in dp[-1]:
            return True ; 
        else:
            return False ; 

######### Test #########
def test():
    sol = Solution() ; 
    cases = [('aa','a'),('aa','a*'),('ab','.*'),('aab','c*a*b'),\
            ('mississippi','mis*is*p*')] ; 
    cases += [('abcdef', '.*'), ('abcde', 'b.*'), \
        ('abcdeee', 'abcdee*'), ('abcd','.abcd'), ('a','')] ;    
    
    for case in cases:
        s,p = case ; 
        print('s={0},p={1},result={2}'.format(s,p,sol.isMatch(s,p))) ; 
    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    main() ; 