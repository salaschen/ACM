'''
GCJ Qualification Round - Nesting Depth
Author: Ruowei Chen
Date: 04/Apr/2020
'''
class Solution:
    def __init__(self):
        pass

    def main(self):
        T = int(input())
        for i in range(1, T+1):
            S = input()
            Sapo = self.work(S)
            print('Case #{0}: {1}'.format(i, Sapo))
        return
    
    def work(self, S: str) -> str:
        depth = 0
        result = ''
        for c in S:
            num = int(c)
            if num >= depth:
                result = result + (num-depth) * '(' + c
            elif num < depth:
                result = result + (depth-num) * ')' + c
            depth = num

        result += depth * ')'
        return result


###### main ######
s = Solution()
s.main()
