'''
Prob: Leetcode 38 - Count and Say
Level: Easy
Author： Ruowei Chen
Date: 19/Oct/2019
Note: 
    Basically this simple problem is used to help me configure the VS Code on my windows machine.
    AC and commited.
'''
import profile ; 
class Solution:
    def countAndSay(self, n: int) -> str:
        cur = '1' ; 
        result = '1' ;
        for i in range(n-1):
            result = self.sayNum(cur) ; 
            cur = result; 
        return result;

    def sayNum(self, num: str) -> str:
        count = 1 ; 
        curIndex = 1 ; 
        result = '' ; 
        N = len(num) ; 
        while curIndex < N:
            if num[curIndex] == num[curIndex-1]:
                count += 1 ; 
            else:
                result += '{0}{1}'.format(count, num[curIndex-1]) ; 
                # result += str(count) + str(num[curIndex-1]) ; 
                count = 1 ; 
            curIndex += 1 ; 
        if count > 0:
           result += '{0}{1}'.format(count, num[curIndex-1]) ; 
           # result += str(count) + str(num[curIndex-1]) ; 

        return result ; 
    
############ Testing ##########
def test():
    s = Solution() ; 
    for i in range(1, 31):
        print(i, s.countAndSay(i)) ; 
    return ;

def main():
    test() ; 
    return ;

if __name__ == "__main__":
    profile.run('main()') ; 
