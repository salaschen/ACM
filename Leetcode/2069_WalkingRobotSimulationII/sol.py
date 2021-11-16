'''
Prob: 2069 - Medium
Author: Ruowei Chen
Date: 16/Nov/2021
'''
import random
class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.facing = 'East'
        self.directions = ['East', 'North', 'West', 'South']
        self.steps = dict()
        self.steps['East'] = (1,0)      # (x+1, y+0)
        self.steps['North'] = (0, 1)    # (x+0, y+1)
        self.steps['West'] = (-1, 0)    # (x-1, y+0)
        self.steps['South'] = (0, -1)   # (x, y-1)
        self.pos = [0,0]
        self.roundTrip = height * 2 + width * 2 - 4

    def getPos(self) -> [int]:
        return self.pos

    def getDir(self) -> str:
        return self.facing
    
    def report(self) -> None:
        print('pos:', self.getPos(), ', facing:', self.getDir())

    def isOutOfBound(self, pos: [int]) -> bool:
        x,y = pos
        return x < 0 or x >= self.width or y < 0 or y >= self.height 

    def isAtBorder(self, pos: [int]) -> bool:
        x,y = pos
        return x == 0 or x == self.width - 1 or y == 0 or y == self.height-1

    def rotate(self) -> None: 
        self.facing = self.directions[(self.directions.index(self.facing)+1) % 4]

    def canMove(self) -> (bool, [int]):
        step = self.steps[self.facing]
        newPos = [self.pos[0] + step[0], self.pos[1]+step[1]]
        return not self.isOutOfBound(newPos), newPos

    # try to advance the robot in his facing
    # only move one step
    # return 
    def advance(self) -> bool:
        ok, newPos = self.canMove()
        if ok:
            self.pos = newPos
            return True
        else:
            return False

    def bruteForceMove(self, num:int) -> None:
        while num > 0:
            if self.advance():
                num -= 1
            else:
                self.rotate()
        return

    def move(self, num: int) -> None:
        # phase 1: try to get to the border
        while num > 0 and not self.isAtBorder(self.pos):
            if self.advance():
                num -= 1
            else:
                break
        if num == 0:
            return
        
        # phase 2: at the border, turn to a facing that can move
        '''
        while not self.canMove()[0]:
            self.rotate()
        '''

        # phase 3: now try to do a round trip
        num = num % self.roundTrip
        # need to manually set the facing of the robot when the robot is at the corner
        x,y = self.pos
        if x == 0 and y == 0: # bottom left
            self.facing = 'South'
        if x == self.width - 1 and y == 0: # bottom right
            self.facing = 'East'
        if x == 0 and y == self.height - 1: # top left
            self.facing = 'West'
        if x == self.width-1 and y == self.height-1: # top right
            self.facing = 'North'

        # phase 4: do the rest of the steps
        while num > 0:
            if self.advance():
                num -= 1
            else:
                self.rotate()
        return 

### test ###
def bruteForceTest():
    x,y = (random.randint(2,10), random.randint(2, 10))
    r1 = Robot(x,y)
    r2 = Robot(x,y)
    for i in range(104):
        num = random.randint(1, 10**5)
        r1.move(num)
        r2.bruteForceMove(num)
    print(r1.getPos())
    print(r1.getDir())
    print(r2.getPos())
    print(r2.getDir())



r = Robot(97,98)
r.report()
r.move(88780)
# r.move(88779)
# r.move(1)
r.report()

bruteForceTest()
