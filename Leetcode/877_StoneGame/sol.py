import random
class Solution:
    def __init__(self):
        self.memory = dict() ;
        self.aliceTurn = True ;

    # return the number of stones that Alice obtains when playing optimally.
    def dfs(self, piles: [int], start: int, end: int, player: bool, scores:[int]) -> [int, int]:
        if (start, end, player) in self.memory:
            return self.memory[(start, end, player)] ;

        # error happens
        if start > end:
            return [0, 0] ;

        # if no choice is left, the last move is Bob's turn
        if start == end:
            [alice, bob] = scores ;
            cur = piles[start] ;
            return [alice, bob+cur] ;

        # if it's bob's turn, it want to 
        op1 = piles[start] ; 
        [a1, b1] = self.dfs(piles, start+1, end, not player, scores) ; 
        op2 = piles[end] ; 
        [a2, b2] = self.dfs(piles, start, end-1, not player, scores) ; 
        
        if player != self.aliceTurn: 
            # bob's move
            if op1+b1 > op2+b2:
                self.memory[(start, end, player)] = [a1, b1+op1] ;
            else:
                self.memory[(start, end, player)] = [a2, b2+op2] ; 
        else:   
            # alice's move
            if op1+a1 > op2+a2:
                self.memory[(start, end, player)] = [a1+op1, b1] ; 
            else:
                self.memory[(start, end, player)] = [a2+op2, b2] ; 

        return self.memory[(start, end, player)] ;


    def stoneGame(self, piles: [int]) -> bool:
        [alice, bob] = self.dfs(piles, 0, len(piles)-1, self.aliceTurn, [0, 0]) ; 
        
        return alice > bob ;




### test ###
s = Solution() ;
piles = [5,3,4,5] ;
print(piles, s.stoneGame(piles)) ; 

piles = [3,7,2,3] ;
print(piles, s.stoneGame(piles)) ; 

piles = [random.randint(1, 500) for i in range(500)] ; 
print(piles, s.stoneGame(piles)) ; 
