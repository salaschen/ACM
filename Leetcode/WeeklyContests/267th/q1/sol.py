'''
Prob: Easy
Author: Ruowei Chen
Date: 15/Nov/2021
Note:
    1) Brute-force simulation.
'''
class Solution:
    def timeRequiredToBuy(self, tickets: [int], k:int) -> int:
        result = 0 
        cur = 0
        tlen = len(tickets)
        while True:
            if tickets[cur] > 0:
                tickets[cur] -= 1
                result += 1
            if cur == k and tickets[cur] == 0:
                return result
            cur = (cur + 1) % tlen

### test ###
s = Solution()
tickets = [2,3,2]
k = 2
print(s.timeRequiredToBuy(tickets, k))

tickets = [5,1,1,1]
k = 0
print(s.timeRequiredToBuy(tickets, k))



                
