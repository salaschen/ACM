'''
Author: Ruowei Chen
Date: 02/May/2019
Prob: Leetcode 841 - Keys and Rooms
'''

class Solution:
    def canVisitAllRooms(self, rooms):
        # see if we have all the keys
        numRoom = len(rooms) ; 
        keys = set([0]) ; 
        for room in rooms:
            keys = keys.union(set(room)) ; 
        if len(keys) < numRoom:
            return False ; 

        seen = set([0]) ; 
        queue = [0] ;
        while len(queue) > 0:
            cur = queue.pop(0) ; 
            keyList = rooms[cur] ;
            for k in keyList:
                if k not in seen:
                    queue.append(k) ; 
                    seen.add(k) ; 
            if len(seen) == numRoom:
                return True ; 

        return False ; 
