'''
Prob: Medium - 18% AC rate
Date: 13/Oct/2021
Author: Ruowei Chen
Note: 
    1) use dfs with memoisation.
'''

class Solution:
    def stoneGameIX(self, stones: [int]) -> bool:
        stones = list(map(lambda s: s%3, stones)) ; 
        numZero = len(list(filter(lambda n: n == 0, stones))) ; 
        numOne = len(list(filter(lambda n: n == 1, stones))) ; 
        numTwo = len(list(filter(lambda n: n == 2, stones))) ;

        # we can offset the pairs of (1 and 0's) and only keep about 3 pairs. 
        if (numOne > 3 and numTwo > 3):
            common =  min(numOne, numTwo) - 3; 
            numOne -= common ; 
            numTwo -= common ;
        
        # if there's more than two, it wont change the result
        # but just to be safe, I'll leave at most 4.
        numZero = numZero % 4 ;

        Alice = True ; 
        result = self.dfs([numZero, numOne, numTwo], Alice, 0) ; 
        return result ;

    def dfs(self, stones: [int], player: bool, cur: int):
        # If the stones picked by last player makes to accumulation
        # stones to be divisible by 3, then the current player wins.
        if cur != 0 and cur % 3 == 0:
            return player ;

        # if there's no remaining stones left, bob wins.
        if sum(stones) == 0:
            return False ; # bob wins.

        [zero, one, two] = stones ; 
        cand = [] ; 
        if zero > 0:
            cand.append(self.dfs([zero-1, one, two], not player, cur)) ;
        if one > 0:
            cand.append(self.dfs([zero, one-1, two], not player, cur+1)) ; 
        if two > 0:
            cand.append(self.dfs([zero, one, two-1], not player, cur+2)) ; 
        best = list(filter(lambda n: n == player, cand)) ;
        if len(best) > 0:
            return player ; 
        else:
            return not player ; 

    def stoneGameIX_old(self, stones: [int]) -> bool:
        stones = list(map(lambda s: s%3, stones)) ; 
        # print(stones) ; # debug
        numZero = len(list(filter(lambda n: n == 0, stones))) ; 
        numOne = len(list(filter(lambda n: n == 1, stones))) ; 
        numTwo = len(list(filter(lambda n: n == 2, stones))) ;
        if sum(stones) % 3 != 0 and len(stones) % 2 == 1:
            return False ; 
        if numZero == len(stones):
            return False ;
        if numOne > numTwo:
            if numOne - numTwo == 1:
                return False ;
            elif numOne - numTwo == 1:
                return False ; 
            else:
                if numZero % 2 == 1:
                    return True ; 
                else:
                    return False ; 

        if numOne == numTwo:
            if numZero % 2 == 0:
                return True; 
            else:
                return False; 

        if numOne < numTwo:
            if numTwo - numOne == 1:
                return False ; 
            elif numTwo - numOne == 2:
                return False ; 
            else:
                if numZero % 2 == 1:
                    return True ;
                else:
                    return False ; 


#### test ####
s = Solution() ; 
stones = [2,1] ;
print(s.stoneGameIX(stones)) ; 
stones = [2] ;
print(s.stoneGameIX(stones)) ; 
stones = [5,1,2,4,3] ;
print(s.stoneGameIX(stones)) ; 
stones = [20,3,20,17,2,12,15,17,4] ;
print(s.stoneGameIX(stones)) ; 
