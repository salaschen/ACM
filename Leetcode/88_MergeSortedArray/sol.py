'''
Prob: 88 Merge Sorted Array - Easy
Author: Ruowei Chen
Date: 27/Dec/2021
Note:
    1) python way of manipulating array memories (meaning I don't really care what
    is happening under the hood).
'''
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        temp = sorted(nums1[:m]+nums2)
        for i in range(n+m):
            nums1[i] = temp[i]