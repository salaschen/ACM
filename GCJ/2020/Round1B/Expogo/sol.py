'''
GJC 2020 - Round 1B - Expogo
Author: Ruowei Chen
Date: 25/Apr/2020
Note:
    1) Use some math to solve the problem.
'''
import heapq
import random
class Solution:
    def __init__(self):
        return

    def main(self):
        T = int(input())
        for i in range(T):
            X, Y = [int(n) for n in input().split()]
            result = self.work(X,Y)
            print("Case #{0}: {1}".format(i+1, result))
        return

    def correct(self, mx, my, path):
        m = dict()
        m['S'] = 'N'
        m['N'] = 'S'
        m['E'] = 'W'
        m['W'] = 'E'
        x, y = ['E','W'], ['N','S']
        result = ''
        for ch in path:
            if (mx and ch in x) or (my and ch in y):
                result += m[ch]
            else:
                result += ch
        return result
    
    def work(self, X, Y):
        heap = []
        mirrorX, mirrorY = False, False
        if X < 0:
            mirrorX = True
            X = -1 * X
        if Y < 0:
            mirrorY = True
            Y = -1 * Y

        # each item in the heap is (depth+mahattan dist, depth, X,Y,curPath)
        heapq.heappush(heap, (X+Y+0, 0, X,Y,'')) 
        while len(heap) > 0:
            _, depth, x,y, path = heapq.heappop(heap)
            # print(depth, x,y,path) # debug
            if x == 0 and y == 0:
                return self.correct(mirrorX, mirrorY, path)
            elif x % 2 == y % 2:
                continue
            elif x % 2 == 1:
                # go east
                item1 = ((x-1)/2+y/2+depth+1, depth+1, (x-1)/2, y/2, path+'E')
                # go west
                item2 = ((x+1)/2+y/2+depth+1, depth+1, (x+1)/2, y/2, path+'W')
                heapq.heappush(heap, item1) 
                heapq.heappush(heap, item2)
            elif y % 2 == 1:
                # go south
                item1 = (x/2+(y-1)/2+depth+1, depth+1, x/2, (y+1)/2, path+'S')
                # go north
                item2 = (x/2+(y+1)/2+depth+1, depth+1, x/2, (y-1)/2, path+'N')
                heapq.heappush(heap, item1) 
                heapq.heappush(heap, item2)
            else:
                print('something wrong here')
                return 'IMPOSSIBLE'
        return 'IMPOSSIBLE'   

#### test ######
def test():
    T = 100
    Pass = 0
    imp = 0
    s = Solution()
    for i in range(T):
        X = random.randint(-1*(10**9), 10**9)
        Y = random.randint(-1*(10**9), 10**9)
        result = s.work(X, Y)
        if result == 'IMPOSSIBLE':
            Pass += 1
            imp += 1
            continue
        a,b = 0, 0
        depth = 0
        for ch in result:
            step = 2 ** depth
            mod = dict()
            mod['E'] = (step, 0)
            mod['W'] = (-step, 0)
            mod['N'] = (0, step)
            mod['S'] = (0, -step)
            a,b = a+mod[ch][0], b+mod[ch][1]
            depth += 1
        if a == X and b == Y:
            Pass += 1
    print('test {0}/{1} passed, {2} impossible'.format(Pass, T, imp))
    return 

##### main program #####
# test()
s = Solution()
s.main()




