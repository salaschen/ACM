'''
Problem: 155 Min Stack - Leetcode Easy
Author: Ruowei Chen
Date: 22/Jan/2021
Note: 
    1) Inspired by another user's solution. While pushing the actual number, 
    we also push the current min element as a second element to the stack.
'''


class MinStack:

    def __init__(self):
        '''
        Initialize data structure
        '''
        self.stack = []
        self.curMin = None
        self.size = 0

    def push(self, x: int) -> None:
        if self.curMin is None or self.curMin > x:
            self.curMin = x ;
        self.stack.append((x, self.curMin)) ;
        self.size += 1 ;

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None ;
        self.stack.pop() ; 
        self.size -= 1  ;
        if self.size > 0:
            self.curMin = self.stack[self.size-1][1] ;
        else:
            self.curMin = None
    
    def top(self) -> int: 
        if self.size == 0:
            return None ;
        return self.stack[self.size-1][0] ;

    def getMin(self) -> int:
        return self.curMin ;


### Testing
stack = MinStack() ;
stack.push(-2) ; 
stack.push(0) ; 
stack.push(-3) ; 
print(stack.getMin()) ; 
print(stack.stack, stack.top()); 
stack.pop() ;
print(stack.stack, stack.getMin(), stack.top()) ;
