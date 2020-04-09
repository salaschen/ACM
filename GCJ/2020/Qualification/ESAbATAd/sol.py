'''
GCJ - Qualification Round - ESAb ATAd
Author: Ruowei Chen
Date: 04/Apr/2020
Note: Interaction problem
'''
from functools import *
import sys

class Solution:
    def __init__(self):
        pass 

    def main(self):
        T, B = [int(n) for n in input().split()]
        for i in range(T):
            verdict = False
            try:
                verdict = self.work(B)
                print('verdict:{0}'.format(verdict), file=sys.stderr)
            except:
                print(verdict, file=sys.stderr)
                return 
            # if failed, exit now.
            if verdict == 'N':
                break
        return 

    # tested 
    def done(self, array: [int]) -> bool:
        return len(list(filter(lambda num: num is None, array))) == 0

    # mode: 0:complement, 1:reverse, 2:comp+reverse, 3: nothing
    # bitSet is either same or diff.
    def update(self, array: [int], bitSet: [(int, int)], mode: int): 
        # complement
        if mode == 0:
            for p1, p2 in bitSet:
                array[p1] = (array[p1] + 1) % 2
                array[p2] = (array[p2] + 1) % 2
        # reverse
        elif mode == 1:
            for p1, p2 in bitSet:
                array[p1], array[p2] = array[p2], array[p1]
        # comp+reverse
        elif mode == 2:
            for p1, p2 in bitSet:
                array[p1], array[p2] = (array[p2]+1)%2, (array[p1]+1)%2
        # do nothing
        else:
            return 
    
    def work(self, B: int):
        turn = 1 # record the number query
        result = [None for i in range(B+1)]
        cur = 1
        result[0] = 0 # dummy bit

        # the pair of bits that are the same and different.
        # for example, 0111. then same has (1, 2), and diff has (0,3)
        # because the  
        same, diff = [], []
        while turn < 150:
            # print(result) # debug
            # when we have all the positions, just try the answer.
            if self.done(result) and turn % 10 != 1:
                # output result
                answer = reduce(lambda x,y: str(x)+str(y), result[1:])
                print(answer, flush=True)
                print(answer, file=sys.stderr, flush=True) # debug
                verdict = input()
                return verdict

            # now we know the permutation has occured, we need to determine how to 
            # update the pairs that we already know.
            elif turn % 10 == 1 and turn > 1:
                if len(same) > 0:
                    p1 = same[0][0]
                    print(p1, flush=True)
                    newP1 = int(input())
                    turn += 1
                    if newP1 != result[p1]:
                        # complement
                        self.update(result, same, 0)
                    else:
                        # do nothing.
                        self.update(result, same, 3)

                if len(diff) > 0:
                    p1 = diff[0][0]
                    print(p1, flush=True)
                    newP1 = int(input())
                    turn += 1
                    if newP1 != result[p1]:
                        # complement
                        self.update(result, diff, 0)
                    else:
                        # do nothing.
                        self.update(result, diff, 3)

            elif turn % 10 == 0:
                print(1, flush=True)
                p = int(input())
                turn += 1

            else:
                cur, tail = cur, B - cur + 1
                print(cur, flush=True)
                curVal = int(input())
                print(tail, flush=True)
                tailVal = int(input())
                if curVal == tailVal:
                    same.append((cur, tail))
                else:
                    diff.append((cur, tail))
                result[cur], result[tail] = curVal, tailVal
                turn += 2
                cur += 1

        print('0'*B) # give up
        return False
            

###### test #######
s = Solution()
s.main()

