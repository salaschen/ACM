'''
Prob: 1383 Maximum Performance of a Team
Author: Ruowei Chen
Date: 17/Mar/2020
'''
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: [int], efficiency: [int], k) -> int:
        # sort the engineer by efficiency
        eng = []
        for i in range(0, len(speed)):
            eng.append((efficiency[i], speed[i]))
        eng = sorted(eng, reverse=True)

        heap = []
        heapSum = 0
        result = -1
        modNum = 10 ** 9 + 7
        for i in range(0, len(eng)):
            curS = eng[i][1]
            curE = eng[i][0]
            if len(heap)+1 > k:
                popS = heapq.heappop(heap)
                heapq.heappush(heap, curS)
                heapSum += (curS - popS)
            else:
                heapq.heappush(heap, curS)
                heapSum += curS

            temp = (heapSum * curE) 
            result = max(result, temp)
        return result % modNum
    

######## test ##########
s = Solution()
speed = [2,10,3,1,5,8]
eff = [5,4,3,9,7,2]
n, k = 6,2
temp = s.maxPerformance(n, speed, eff, k)
print(temp)
            
                
            
        
        
