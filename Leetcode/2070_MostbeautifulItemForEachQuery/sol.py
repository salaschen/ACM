'''
Prob: 2070 Medium, acceptance rate 1579/2353
Author: Ruowei Chen
Date: 19/Nov/2021
'''
import random
class Solution:
    def maximumBeauty(self, items: [[int]], queries: [int]) -> [int]:
        items = sorted(items, key=lambda item: item[0]) # sort the list of items by price

        pb = [items[0]] # price-beauty
        for i in range(1, len(items)):
            price, beauty = items[i]
            prev = pb[-1]
            if price == prev[0]:
                if beauty >= prev[1]:
                    prev[1] = beauty
            else:
                if beauty >= prev[1]:
                    pb.append(items[i])
                else:
                    pb.append([price, prev[1]])

        # print('pb:', pb) # debug
        result = []
        for query in queries:
            # when the query is outside of the price range
            if query < pb[0][0]: 
                result.append(0)
            elif query > pb[-1][0]:
                result.append(pb[-1][1])
            elif query == pb[0][0]:
                result.append(pb[0][1])
            elif query == pb[-1][0]:
                result.append(pb[-1][1])
            else:
                low, up = 0, len(pb)-1
                added = False
                while (up-low) > 1:
                    mid = (up+low)//2
                    if query == pb[mid][0]:
                        result.append(pb[mid][1])
                        added = True
                        up = low
                    elif query > pb[mid][0]:
                        low = mid
                    else:
                        up = mid
                if not added:
                    result.append(pb[low][1])
        return result

    def bruteForce(self, items, queries):
        items = sorted(items, key=lambda item: item[0])
        result = []
        for query in queries:
            cur = 0 
            for i in range(len(items)):
                if items[i][0] <= query:
                    cur = max(cur, items[i][1])
            result.append(cur)
        return result

### test ###
def normalTest():
    s = Solution()
    items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
    queries = [1,2,3,4,5,6]
    print(s.maximumBeauty(items, queries))

    items = [[1,2],[1,2],[1,3],[1,4]]
    queries = [1]
    print(s.maximumBeauty(items, queries))

    items = [[10,1000]]
    queries = [5]
    print(s.maximumBeauty(items, queries))

def randomTest():
    upper = 1000
    itemSize, querySize = random.randint(1, upper), random.randint(1,upper)
    items = [[random.randint(1, 1000), random.randint(1, 1000)] for i in range(itemSize)]
    query = [random.randint(1, 1000) for i in range(querySize)]
    s = Solution()
    expect = s.bruteForce(items, query)
    output = s.maximumBeauty(items, query)
    # print(items)
    # print(query)
    # print('expect:', expect)
    # print('output:', output)

    if expect != output:
        print(items)
        print(query)
        print('expect:', expect)
        print('output:', output)
    return expect == output

# normalTest()
total = 100
count = 0
for i in range(total):
    if randomTest():
        count += 1
print("pass {0}/{1}".format(count, total))
