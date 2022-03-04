'''
Prob: 560 - Medium
Author: Ruowei Chen
Date: 04/Mar/2022
'''
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        n = len(nums)
        mem = dict()
        mem[0] = 1
        cur = 0
        count = 0
        for i in range(n):
            cur += nums[i]
            if cur-k in mem:
                count += mem[cur-k]
            if cur in mem:
                mem[cur] += 1
            else:
                mem[cur] = 1
        return count

    def slow(self, nums: [int], k: int) -> int:
        n = len(nums)
        f = [0 for i in range(n+1)]
        
        for i in range(n):
            f[i] = f[i-1] + nums[i]

        result = 0
        for i in range(n):
            for j in range(i, n):
                temp = f[j] - f[i-1]
                if temp == k:
                    result += 1
        return result



### test ###
def randomTest():
    import random
    s = Solution()
    pas = 0
    times = 100
    for i in range(times):
        size = 100
        k = 10
        low, up = -10, 10
        nums = [random.randint(low, up) for i in range(size)]
        # k = random.randint(-10 ** 7, 10 ** 7)
        actual = s.subarraySum(nums, k)
        expect = s.slow(nums, k)
        if actual == expect:
            pas += 1
    print(f'pass {pas}/{times}')
    return 

def caseTest():
    s = Solution()
    nums = [1,1,1]
    k = 2
    print(s.subarraySum(nums, k))

    nums = [1,2,3]
    k = 5
    print(s.subarraySum(nums, k))

    nums = [1]
    k = 0
    print(s.subarraySum(nums, k))



caseTest()
# randomTest()
