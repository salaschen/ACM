class Solution:
    def getDescentPeriods(self, prices:[int]) -> int:
        periods = []
        result = 0
        for i in range(len(prices)):
            cur = prices[i]
            plen = len(periods)
            if plen == 0:
                result += 1
                periods.append(cur)
            elif periods[-1] - 1 == cur:
                result += (plen + 1)
                periods.append(cur)
            else:
                periods = [cur]
                result += 1
        return result


### test ###
s = Solution()
prices = [3,2,1,4]
print(s.getDescentPeriods(prices))

prices = [8,6,7,7]
print(s.getDescentPeriods(prices))

prices = [1]
print(s.getDescentPeriods(prices))

