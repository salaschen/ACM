'''
GCJ - Qualification - Parenting Partnering Returns
Author: Ruowei Chen
Date: 04/Apr/2020
Note: Simple brute-force (doesn't work)
Note2: sort the task by starting time first then use greedy.
'''
class Solution:
    def __init__(self):
        return

    def main(self):
        T = int(input())
        for i in range(T):
            result = self.work()
            print('Case #{0}: {1}'.format(i+1, result))
        return

    def work(self) -> str:
        N = int(input())
        J,C = [],[]
        result = ""
        tasks = []
        for i in range(N):
            start, end = [int(n) for n in input().split()]
            tasks.append((start, end, i))
        tasks = sorted(tasks) ;
        # print(tasks) # debug
        result = '*' * N
        for i in range(N):
            start, end, index = tasks[i]
            if result ==  'IMPOSSIBLE':
                continue
            if self.canFit(J, (start, end)):
                J.append((start, end))
                result = result[:index] + "J" + result[index+1:]
            elif self.canFit(C, (start, end)):
                C.append((start, end))
                result = result[:index] + "C" + result[index+1:]
            else:
                result = 'IMPOSSIBLE'
        return result

    def collide(self, t1: (int, int), t2: (int, int)) -> bool:
        
        # make sure t1 starts before t2
        tfirst, tsecond = t1, t2
        if t1[0] > t2[0]:
            tfirst, tsecond = t2, t1
        return (tsecond[0] < tfirst[1])

    def canFit(self, tasks: [(int, int)], task: (int, int)) -> bool:
        if len(tasks) == 0:
            return True
        for t in tasks:
            if self.collide(t, task):
                return False
        return True

######## main ###########
s = Solution()
s.main()
