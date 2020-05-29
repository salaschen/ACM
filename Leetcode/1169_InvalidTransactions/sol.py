'''
Prob: Leetcode 1169 - Invalid Transations
Author: Ruowei Chen
Date: 29/May/2020
'''
class Solution:
    # return a list of invalid transactions
    def invalidTransactions(self, transactions: [str]) -> [str]:
        result = set()
        tranDict = dict()
        for t in transactions:
            name, time, amount, city = t.split(',')
            if name not in tranDict:
                tranDict[name] = []
            tranDict[name].append((int(time), amount, city))
            if int(amount) > 1000:
                result.add(t)

        for key in tranDict:
            name = key
            queue = sorted(tranDict[key], key=lambda item: item[0])
            qlen = len(queue)
            for i in range(0, qlen-1):
                cur = queue[i]
                for j in range(i+1, qlen):
                    nex = queue[j]
                    if cur[2] != nex[2] and cur[0]+60 >= nex[0]:
                        result.add(self.makeTrans(name, cur[2], cur[0], cur[1]))
                        result.add(self.makeTrans(name, nex[2], nex[0], nex[1]))
                    elif cur[0]+60<nex[0]:
                        break
                    
        print(tranDict) # debug
            
        return list(result)
    
    def makeTrans(self, name, city, time, amount):
        return '{0},{1},{2},{3}'.format(name, time, amount, city)


#### test ######
s = Solution()
transactions = ["alice,20,800,mtv","alice,50,1200,mtv", 'bob,20, 800, beijing'\
        ,'bob, 30, 1000, beijing', 'bob, 50, 800, shanghai']
print(s.invalidTransactions(transactions))

