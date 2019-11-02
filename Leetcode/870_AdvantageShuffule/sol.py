'''
Prob: Leetcode 870 - Advantage Shuffle
Author: Ruowei Chen
Date: 02/Nov/2019
Note: Brute-force
'''
class Solution:
    def advantageCount(self, A: [[int]], B: [[int]]) -> [[int]]:
        a = sorted(A, reverse=True) ; 
        b = sorted(B, reverse=True) ; 
        A_i, B_i = 0,0 ; 
        arrayLen = len(A) ; 
        count = 0 ; 
        a_tail = arrayLen-1 ; 
        nonMatch = [] ; 
        match = dict() ; 
        while A_i < arrayLen and B_i < arrayLen:
            if a[A_i] > b[B_i]:
                count += 1 ;
                if b[B_i] in match:
                    match[b[B_i]].append(a[A_i]) ; 
                else:
                    match[b[B_i]] = [a[A_i]] ; 
                A_i += 1 ;
                B_i += 1 ; 
            else:
                nonMatch.append(a[a_tail]) ; 
                a_tail -=1 ; 
                B_i += 1 ; 

        # now construct the permutation of A that maximizes the advantage.
        result = [] ; 
        non_i = 0  ;
        for i in range(arrayLen):
            if B[i] in match:
                num = match[B[i]].pop(0) ; 
                result.append(num) ; 
                if len(match[B[i]]) == 0:
                    match.pop(B[i]) ; 
            else:
                result.append(nonMatch[non_i]) ; 
                non_i += 1 ; 

        return result; 
    
######### Test ############
def test():
    s = Solution() ; 
    A = [2,7,11,15] ; 
    B = [1,10,4,11] ; 
    print(A,B) ; 
    print(s.advantageCount(A,B)) ; 
    A = [12,24,8,32] ; 
    B = [13,25,32,11] ; 
    print(A,B) ; 
    print(s.advantageCount(A,B)) ; 

    return ; 

def main():
    test() ; 

if __name__ == "__main__":
    main() ; 