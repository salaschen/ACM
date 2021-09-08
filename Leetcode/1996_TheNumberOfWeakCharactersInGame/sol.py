'''
Prob: 1996 - The Number of Weak Characters in the Game
Level: Medium
Author: Ruowei Chen
Date: 08/Sep/2021
'''

class Solution:
    def numberOfWeakCharacters(self, properties: [[int]]) -> int:
        properties.sort(reverse=True) ;
        curAttack = properties[0][0] ; 
        maxDefence = properties[0][1] ;
        maxAttack = properties[0][0] ;
        result = 0 ; 
        subMaxDefence = 0 ;
        for i in range(1, len(properties)):
            cur = properties[i] ; 
            if cur[0] != curAttack:
                maxDefence = max(subMaxDefence, maxDefence) ;
                subMaxDefence = cur[1] ; 
                curAttack = cur[0] ;

            if cur[1] < maxDefence and cur[0] < maxAttack:
                result += 1 ; 

        return result ; 

s = Solution() ;
properties = [[5,5],[6,3],[3,6]] ;
print(s.numberOfWeakCharacters(properties)) ; 

properties = [[2,2],[3,3]] ;
print(s.numberOfWeakCharacters(properties)) ; 

properties = [[1,5],[10,4],[4,3]];
print(s.numberOfWeakCharacters(properties)) ; 

properties = [[1,1],[2,1],[2,2],[1,2]] ;
print(s.numberOfWeakCharacters(properties)) ; 

properties = [[7,9],[10,7],[6,9],[10,4],[7,5],[7,10]];
print(s.numberOfWeakCharacters(properties)) ; 

