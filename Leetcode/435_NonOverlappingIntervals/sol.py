'''
Prob: 435 - Medium
Author: Ruowei Chen
Date: 02/Mar/2022
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        intervals = sorted(intervals)
        i = 0
        result = 0
        ilen = len(intervals)
        while i < ilen-1:
            cur = intervals[i]
            nex = intervals[i+1]

            # print(f'intervals: {intervals}') # debug
            if nex[0] >= cur[0] and nex[0] < cur[1]:
                result += 1
                if self.contains(cur, nex):
                    # cur contains nex, so retian nex only
                    # intervals = intervals[:i] + intervals[i+1:]
                    # do nothing
                    i
                elif self.contains(nex, cur):
                    # retain cur only
                    # intervals = intervals[:i+1] + intervals[i+2:]
                    intervals[i+1], intervals[i] = cur, nex
                else:
                    if nex[1] >= cur[1]:
                        # remove nex
                        # intervals = intervals[:i+1] + intervals[i+2:]
                        intervals[i+1], intervals[i] = cur, nex

                    # else:
                        # remove cur
                        # intervals = intervals[:i] + intervals[i+1:]

            i += 1

        return result
        
    # return if i1 contains i2
    def contains(self, i1: [int], i2: [int]) -> bool:
        return i1[0] <= i2[0] and i1[1] >= i2[1]


### test ###
def randomTest():
    import random
    size = 10 ** 5
    low, up = (-5*10**4), (5*10**4)
    intervals = [sorted([random.randint(low, up), random.randint(low, up)]) for i in range(size)]
    s = Solution()
    print(s.eraseOverlapIntervals(intervals))
    return

def caseTest():
    s = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(s.eraseOverlapIntervals(intervals))

    intervals = [[1,2],[1,2],[1,2]] 
    print(s.eraseOverlapIntervals(intervals))

    intervals = [[1,2],[2,3]]
    print(s.eraseOverlapIntervals(intervals))

    intervals = [[1,100],[11,22],[1,11],[2,12]]
    print(s.eraseOverlapIntervals(intervals))

randomTest()


