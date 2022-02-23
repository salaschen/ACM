'''
Prob: Leetcode Hard
Author: Ruowei Chen
Date: 23/Feb/2022
'''
class Solution:
    def __init__(self):
        self.primes = [2,3,5]
        # self.getPrimes()

    # fill up the prime list
    def getPrimes(self, limit=1000):
        cur = self.primes[-1]+2
        while cur <= limit:
            for p in self.primes:
                if p ** 2 > cur:
                    self.primes.append(cur)
                    break
                elif cur % p == 0:
                    break
            cur = cur + 2
        # print(self.primes) # debug
        return

    def countPairs(self, nums: [int], k: int) -> int:
        self.getPrimes(k+1)
        # stage 1:
        factors, powers = self.factorize(k)
        # debug
        # print(f'factors: {factors}')
        # print(f'powers: {powers}')
    
        # stage 2:
        class Comp:
            def __init__(self, power:[int], size=1):
                self.size = size 
                self.power = power

            def __str__(self):
                return f'size: {self.size}, power: {self.power}'
            
            # larger or equal to other component
            def larger(self, other):
                return len(list(filter(lambda n: n < 0, \
                        list(map(lambda p: p[0]-p[1], zip(self.power, other.power)))))) == 0

            # return a new Comp object as the sum of the two added Comp objects
            def add(self, other):
                p = list(map(lambda p: p[0]+p[1], zip(self.power, other.power)))
                s = self.size + other.size
                return Comp(p, s)

        mem = dict()
        for num in nums:
            temp = self.getPowers(num, factors)
            if tuple(temp) in mem:
                comp = mem[tuple(temp)]
                comp.size += 1
            else:
                mem[tuple(temp)] = Comp(temp, 1)
        
        target = Comp(powers)
        compList = []
        for key in mem.keys():
            compList.append(mem[key])
        
        # stage 3:
        result = 0
        # print(f'complist has {len(compList)} elements') # debug
        # print(f'original nums has {len(nums)} elements') # debug
        for i in range(len(compList)):
            m = compList[i]
            for j in range(len(compList)):
                n = compList[j]
                # print(f'target: {target}, m: {m}, n: {n}, result: {result}') # debug
                # print(f'm.add(n): {m.add(n)}') # debug
                if m.add(n).larger(target):
                    if i == j:
                        result += (m.size*(m.size-1))
                    else:
                        result += (m.size * n.size)
        
        result = result // 2
        return result

    def getPowers(self, num: int, factors: [int]) -> [int]:
        result = [0 for i in range(len(factors))]
        cur = num
        for i in range(len(factors)):
            f = factors[i]
            p = 0
            while cur % f == 0:
                p += 1
                cur = cur // f
            result[i] = p
        return result


    def factorize(self, k: int) -> int:
        factors, powers = [], []
        cur = k
        for p in self.primes:
            if p > k:
                break

            if cur % p == 0:
                factors.append(p)
                powers.append(1)
                cur = cur // p

            while cur % p == 0:
                powers[-1] += 1
                cur = cur // p

        return factors, powers

    def bruteForce(self, nums: [int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                temp = nums[i]*nums[j]
                # print(f'{nums[i]}*{nums[j]}={temp}')
                # print(f'{temp} % {k} = {temp%k}') 
                if (nums[i]*nums[j]) % k == 0:
                    result += 1
        return result

### test ###
def randomTest():
    import random
    import time
    times = 3
    size = 5000
    slow, fast = 0, 0
    pas = 0

    sslow = Solution()
    for i in range(times):
        # generate nums
        nums = [random.randint(1, 10**5) for j in range(size)]
        k = random.randint(1, 10 ** 5)
        start = time.time()
        expect = sslow.bruteForce(nums, k)
        slow = slow + (time.time() - start)
        start = time.time()
        s = Solution()
        actual = s.countPairs(nums, k)
        fast = fast + (time.time() - start)
        if actual == expect:
            pas += 1
        else:
            print(f'{nums}, k:{k}, expect: {expect}, actual: {actual}')
    print(f'pass {pas}/{times}')
    print(f'slow: {slow:.3} seconds, fast: {fast: .3} seconds')
    return

def caseTest():
    s = Solution()
    '''
    nums = [1,2,3,4,5]
    k = 2
    print(s.coutPairs(nums, k))

    nums = [1,2,3,4]
    k = 5
    print(s.coutPairs(nums, k))

    nums = [37, 36, 70, 98, 51, 22, 49, 54, 79, 20]
    k = 16
    print(s.coutPairs(nums, k))
    nums = [71691, 67236, 17789, 12813, 89971, 94912, 22327, 83111, 3353, 565, 12625, 76785, 76500, 2521, 14418, 57166, 23833, 18949, 71195, 83244]
    k = 69380
    print(s.bruteForce(nums, k))
    print(s.coutPairs(nums, k))
    '''
    nums = [95,100,67,5,37,61,52,69,95]
    k = 5
    print(s.countPairs(nums, k))

# caseTest()
randomTest()
