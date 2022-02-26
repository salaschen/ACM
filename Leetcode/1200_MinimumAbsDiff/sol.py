'''
Prob: Minimum Absolute Difference - Easy
Author: Ruowei Chen
Date: 26/Feb/2022
Note:
    1. O(nlgn) implementation, involves sorting.
'''
class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        lst = sorted(arr)
        result = []
        diff = None
        for i in range(len(lst)-1):
            a,b = lst[i], lst[i+1]
            if diff is None or diff == (b-a):
                result.append([a,b])
                diff = (b-a)
            elif diff > (b-a):
                result = [[a,b]]
                diff = b-a
        return result

### test ###
s = Solution()
arr = [3,8,-10,23,19,-4,-14,27]
print(s.minimumAbsDifference(arr))

arr = [4,2,1,3]
print(s.minimumAbsDifference(arr))

arr = [1,3,6,10,15]
print(s.minimumAbsDifference(arr))

