'''
Prob: 56 Merge Intervals
Author: Ruowei Chen
Date: 26/Jan/2022
'''
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        # sort first, then merge from the front.
        intervals = sorted(intervals, key=lambda n: n[0])
        cur = 0
        while cur < len(intervals)-1:
            # try to merge with the next one
            this = intervals[cur]
            neXt = intervals[cur+1]
            if this[1] >= neXt[0]:
                # merge
                temp = [min(this[0], neXt[0]), max(this[1], neXt[1])]
                intervals[cur] = temp
                # delete the intervals[cur+1]
                intervals = intervals[:cur+1] + intervals[cur+2:]
            else:
                cur += 1
        return intervals

### test ###
s = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(s.merge(intervals))

intervals = [[1,4],[4,5]]
print(s.merge(intervals))

intervals = [[1,4],[5,6], [5, 8]]
print(s.merge(intervals))

intervals = [[1,4],[2,3]]
print(s.merge(intervals))

