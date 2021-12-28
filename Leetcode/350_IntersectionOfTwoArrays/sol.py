'''
Prob: 350 - Easy (Study plan)
Author: Ruowei Chen
Date: 28/Dec/2021
'''
class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        n1 = dict()
        for num in nums1:
            if num in n1:
                n1[num] += 1
            else:
                n1[num] = 1

        result = []
        for num in nums2:
            if num in n1 and n1[num] > 0:
                result.append(num)
                n1[num] -= 1
                if n1[num] == 0:
                    n1.pop(num)
        return result

### test ###
s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersect(nums1, nums2))
