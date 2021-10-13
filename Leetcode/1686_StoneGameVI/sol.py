'''
Prob: Medium, Acceptance: 52.5%
Author: Ruowei Chen
Date: 13/Oct/2021
Note: 
    1) Greedy algorithm.
'''
from functools import cmp_to_key 
def compare(n1, n2):
    if n1[0] != n2[0]:
        return n1[0]-n2[0] ;
    else:
        return n1[1] ;

class Solution:
    def stoneGameVI(self, aliceValues: [int], bobValues: [int]) -> int:
        aliceDiff = list(map(lambda a,b: (a+b, a, b), aliceValues, bobValues)) ; 

        aliceDiff = sorted(aliceDiff, key=cmp_to_key(compare), reverse=True) ; 
        print(aliceDiff) ; # debug

        alice = 0 ;
        bob = 0 ; 
        turn = True ;
        for i in range(0, len(aliceDiff)):
            if turn:
                alice += aliceDiff[i][1] ;
            else:
                bob += aliceDiff[i][2] ; 
            turn = not turn ;
        
        if alice == bob:
            return 0; 
        elif alice > bob:
            return 1 ; 
        else:
            return -1 ; 


#### test ####
s = Solution() ;
aliceValues, bobValues = [1,3],[2,1]
print(s.stoneGameVI(aliceValues, bobValues)) ; 

aliceValues, bobValues = [1,2],[3,1]
print(s.stoneGameVI(aliceValues, bobValues)) ; 

aliceValues, bobValues = [2,4,3],[1,6,7]
print(s.stoneGameVI(aliceValues, bobValues)) ; 

