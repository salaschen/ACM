'''
Prob: 225 - Easy
Author: Ruowei Chen
Date: 25/Jan/2022
'''
class MyStack:
    def __init__(self):
        self.storeQueue, self.readyQueue = [], []

    def push(self, x: int) -> None:
        self.readyQueue.append(x)

    def pop(self) -> int:
        if self.empty():
            raise Exception('stack is empty')
        if len(self.readyQueue) == 1:
            result = self.readyQueue.pop(0)
            self.readyQueue, self.storeQueue = self.storeQueue, self.readyQueue
            return result
        else:
            self.top()
            return self.pop()

    def top(self) -> int:
        if self.empty():
            raise Exception('stack is empty')
        if len(self.readyQueue) == 1:
            return self.readyQueue[0]
        else:
            for i in range(1, len(self.readyQueue)):
                self.storeQueue.append(self.readyQueue.pop(0))
            return self.readyQueue[0]


    def empty(self) -> bool:
        return len(self.readyQueue) == 0 and len(self.storeQueue) == 0

### test ###
s = MyStack()
s.push(10)
s.push(5)
print(s.top(), 5) # 10, 5
print(s.pop(), 5) # 10
s.push(15) # 10, 15
s.push(20) # 10, 15, 20
print(s.pop(), 20) # 10, 15 
print(s.pop(), 15) # 10

