import heapq ; 

class Solution:
    def __init__(self):
        self.DigitDistDict = dict() ; 
        digits = '0123456789' ; 
        for i in range(0, len(digits)):
            for j in range(i+1, len(digits)):
                dist = self.DigitDist(digits[i], digits[j]) ;
                self.DigitDistDict[(digits[i], digits[j])] = dist ; 
                self.DigitDistDict[(digits[j], digits[i])] = dist ;
            self.DigitDistDict[(digits[i], digits[i])] = 0 ; 
        
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        : Version 1: brute force DFS
        """
        searched = set() ; 
        dist = 0 ; 
        # result = self.DFS(deadends, target, "0000", 0, searched) ; 
        # result = self.BFS(deadends, target, "0000") ; 
        result = self.AStar(deadends, target, "0000") ; 
        # result = self.AStar(deadends, "0000", target) ; 
        return result ; 
        
    # TLE on case 40. Passed 39/43
    def BFS(self, deadends, target, current):
        if current in deadends:
            return -1 ; 
        added = set() ; 
        queue = [(current, 0)] ; 
        added.add(current) ; 
        while len(queue) > 0:
            curString, curDist = queue.pop(0) ; 
            if curString == target:
                return curDist ; 
            nextNodes = self.GetNextNodes(curString) ; 
            for node in nextNodes:
                if node not in added and node not in deadends:
                    queue.append((node, curDist+1)) ; 
                    added.add(node) ; 
        return -1 ; 

    def AStar(self, deadends, target, current):
        queue = [] ; 
        searched = set() ; 
        if current in deadends:
            return -1 ; 
        if target in deadends:
            return -1 ; 

        curNode = (self.ManHattanDist(current, target), 0, current) ; 
        heapq.heappush(queue, curNode) ; 
        searched.add(current) ; 
        while len(queue) > 0:
            curManDist, curDist, current = heapq.heappop(queue) ; 
            nextNodes = self.GetNextNodes(current) ;
            for node in nextNodes:
                if node == target:
                    return curDist + 1 ; 
                elif node not in searched and node not in deadends:
                    newNode = (self.ManHattanDist(node, target)+curDist+1, curDist+1, node) ;
                    heapq.heappush(queue, newNode) ;
                    searched.add(node) ; 

        return -1 ; 

    def ManHattanDist(self, current, target):
        result = 0 ; 
        for i in range(0, len(current)):
            # result += self.DigitDist(current[i], target[i]) ; 
            result += self.DigitDistDict[(current[i], target[i])] ; 
        return result ; 

    def DigitDist(self, d1, d2):
        '''
        both d1 and d2 are characters
        '''
        return abs(int(d1)-int(d2)) ; 


    # stack overflow

    def GetNextNodes(self, current):
        result = [] ;
        plus = lambda n: n + 1 ; 
        minus = lambda n : n - 1 ; 
        for i in range(0, len(current)):
            prev = current[0:i] ;
            after = current[i+1:] ; 
            digit = current[i] ; 
            result.append(prev+self.GetNextDigit(digit, plus)+after) ; 
            result.append(prev+self.GetNextDigit(digit, minus)+after) ; 
        return result ; 

    def GetNextDigit(self, digit, operator):
        return str((operator(int(digit))+10)%10); 
        

def Test1():
    deadends = ["0201", "0101", "0102", "1212", "2002"] ; 
    target = "0202" ; 
    GenTest(deadends, target) ; 

def Test2():
    deadends = ["8888"] ; 
    target = "0009" ; 
    GenTest(deadends, target) ; 

def Test3():
    deadends = ["8887", "8889", "8878", "8898", "8788", \
            "8988", "7888", "9888"] ; 
    target = "8888" ; 
    GenTest(deadends, target) ; 

def Test4():
    deadends = ["0000"] ;
    target = "8888" ; 
    GenTest(deadends, target) ; 

def Test5():
    deadends, target = ReadInput('test.in') ; 
    GenTest(deadends, target, False) ; 

def GenTest(deadends, target, Verbose=True):
    s = Solution() ; 
    result = s.openLock(deadends, target) ; 
    print("*"*20) ; 
    if Verbose:
        print("deadends:", deadends) ; 
    print("target:{0}, result:{1}".format(target, result)) ; 
    print("*"*20) ; 
    return ; 

def ReadInput(File):
    '''
    Returns deadends and target as a Tuple
    '''
    f = open(File, 'r'); 
    line1 = f.readline().strip('\n').strip("[]") ; 
    deadends = [word.strip('\"').strip('\n') for word in line1.split(',')] ; 
    target = f.readline().strip('\n').strip('"')  ; 
    return (deadends, target) ; 

if __name__ == "__main__":
    '''
    Test1() ; 
    Test2() ; 
    Test3() ; 
    Test4() ;
    '''
    Test5() ; 
