'''
UVa 11853: Paint Ball
Date: 2018-10-19
Author: Ruowei Chen
'''
import math ; 

class Oppo:
    def __init__(self, x,y, r):
        self.x = x ; 
        self.y = y ; 
        self.r = r ; 
    
    def isConnected(self, other):
        '''
        other: another Oppo object
        '''
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2) \
                <= (self.r + other.r) ;

    def __str__(self):
        return "(x:{0}, y:{1}, range:{2})".format(self.x, self.y, self.r) ; 
        
def work(oppos):
    '''
    oppos: list of Oppo
    '''

    # First, get a list of connected components.
    compList = getComponents(oppos) ; 

    # Second, For each of the components, test if they connect the 
    # north to south. If so, return 'IMPOSSIBLE'. 
    westY, eastY = 1000.0, 1000.0 ; 
    for comp in compList:
        touchN, touchS, touchWestY, touchEastY = checkComponent(comp) ; 
        if touchN and touchS:
            return 'IMPOSSIBLE' ;
        elif touchN:
            if touchWestY is not None:
                westY = min(touchWestY, westY) ;
            if touchEastY is not None:
                eastY = min(touchEastY, eastY) ; 
    
    # Third, If none is connected, 
    # then return the southest intersection point for the right and left
    # border with the component(s) that reaches the north border.
    return '0.00 {:.2f} 1000.00 {:.2f}'.format(westY, eastY);

def testCheckComponent():
    o1 = Oppo(900,900, 100) ; 
    o2 = Oppo(900,800, 100) ; 
    o3 = Oppo(900,700, 300) ; 
    comp = [o1,o2,o3] ; 
    check = checkComponent(comp) ; 
    printComponent(comp) ; 
    print(check) ; 
    return ;

def checkComponent(component):
    '''
    :type component: 
    :rtype (bool: touchNorth, bool: touchSouth, float: touchWestY, float: touchEastY)
    :Note: if the component doesn't touch west, then it's None. Same for the touchEastY.
    '''
    touchNorth, touchSouth = False, False ;
    touchWestY, touchEastY = None, None ;
    for c in component:
        if c.y + c.r >= 1000.0:
            touchNorth = True ;
        if c.y - c.r <= 0.0:
            touchSouth = True ;
        if c.x - c.r <= 0.0:
            # calculate the intersection point 
            points = calTouch(c.x,c.y,c.r, 0.0) ; 
            if len(points) > 0:
                westY = min(points) ; 
                if touchWestY is None: 
                    touchWestY = westY ;
                else: 
                    touchWestY = min(touchWestY, westY) ; 
        if c.x + c.r >= 1000.0:
            points = calTouch(c.x,c.y,c.r, 1000.0) ; 
            if len(points) > 0:
                eastY = min(points) ; 
                if touchEastY is None:
                    touchEastY = eastY ;
                else:
                    touchEastY = min(touchEastY, eastY) ; 
    return (touchNorth, touchSouth, touchWestY, touchEastY) ;  

def calTouch(x,y,r,lx):
    '''
    :type x: float, x for the circle's center point.
    :type y: float, y for the circle's center point.
    :type r: float, radius for the circle. r should be always non-negative.
    :type lx: float, x value for the vertical line.
    :rtype: [float], y values for the intersection points. Potentially no intersection.
    '''
    if (x-abs(r) > lx and x > lx) or (x+abs(r) < lx and x < lx):
        return [] ; 
    diff = math.sqrt(r**2 - (lx-x)**2) ;    
    result = [] ;
    if diff == 0.0:
        result = [y] ;
    else:
        result = [y+diff, y-diff] ; 
    return list(filter(lambda n: n >= 0.0, \
            list(map(lambda n: 0 if n < 0 else n, result)))) ; 

def getComponents(oppos):
    result = [] ; 
    while len(oppos) > 0:
        cur = getSingleComponent(oppos);   
        if len(cur) > 0:
            result.append(cur) ;
    return result ;

def getSingleComponent(oppos):
    result = [] ; 
    if len(oppos) == 0:
        return result ; 
    queue = [oppos.pop(0)] ;
    while len(queue) > 0:
        cur = queue.pop(0) ; 
        result.append(cur) ; 
        connected = [] ; 
        for o in oppos:
            if cur.isConnected(o):
                connected.append(o) ; 
        for c in connected:
            oppos.remove(c) ; 
            queue.append(c) ; 
    return result ; 
        
def printComponent(comp):
    if len(comp) == 0:
        return ; 
    line = str(comp[0]) ; 
    for i in range(1, len(comp)):
        line += ","+str(comp[i]) ;
    print(line) ;  
    return ; 

def testGetSingle():
    o1 = Oppo(0,0,10) ;
    o2 = Oppo(1,1,5) ; 
    oppos = [o1,o2] ;
    result = getSingleComponent(oppos) ; 
    printComponent(result) ; 

    oppos = [o1] ; 
    result = getSingleComponent(oppos) ; 
    printComponent(result) ; 

    o3 = Oppo(10, 10, 2) ;
    oppos = [o1, o2, o3] ; 
    result = getSingleComponent(oppos) ; 
    printComponent(result) ; 
    return ;

def real():
    try:
        while True:
            num = int(input()) ; 
            oppos = [] ; 
            for i in range(0, num):
                x,y,r = [int(n) for n in input().split()] ;
                oppos.append(Oppo(x,y,r)) ; 
            result = work(oppos) ; 
            print(result) ;
    except:
        return ; 

def main():
    # testCheckComponent() ;
    # testGetSingle() ; 
    real() ; 
    return ; 
    
if __name__ == "__main__":
    main() ; 
