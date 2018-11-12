'''
UVa 810 - A Dicey Problem

'''
class Dice:
    def __init__(self):
        # order: top, bottom, face, back, left, right.
        self.faces = [6,1,4,3,2,5] ;
        return ; 

    def __init__(self, top=5, face=1):
        # rotate so that top and face is set as required.
        if top not in [1,2,3,4,5,6] or face not in [1,2,3,4,5,6]:
            return None ;

        self.faces = [6,1,4,3,2,5] ;
        while top not in [self.top(), self.bottom(), self.left(), self.right()]:
            self.RotateY() ; 

        while top != self.top():
            self.RotateX() ; 

        while face != self.face():
            self.RotateZ() ;
        return  ;

    def __str__(self):
        faces = ['top', 'bottom', 'face', 'back', 'left', 'right'] ;
        result = 'dice:[' ;
        for i in range(6):
            result += '({0},{1})'.format(faces[i], self.faces[i]) ; 
        return result ;
    
    def FlipRight(self):
        self.RotateX() ; 
        return self ; 

    def FlipLeft(self):
        for i in range(3):
            self.RotateX() ;
        return self ; 
        
    def FlipForward(self):
        self.RotateY() ; 
        return self ;

    def FlipBackward(self):
        for i in range(3):
            self.RotateY() ;
        return self ; 

    def RotateY(self):
        '''
        Rotate the dice around the y-axis.
        fashion. The y-axis is seen as goes parallel with the 
        edge of the maze.

        It looks like the dice is flips forward
        left and right remains the same. And
        top=>face, face=>bottom, bottom=>back, back=>top.
        '''
        self.faces[:4] = [self.back(), self.face(), self.top(), self.bottom()] ;
        return ; 

    def RotateZ(self):
        # rotate the dice around the 
        # z-axis in a clock-wise fasion
        # top and bottom remains the same
        # face=>left, left=>back, back=>right, right=>face
        self.faces[2:] = [self.right(), self.left(), self.face(), self.back()] ; 
        return ; 
        
    def RotateX(self):
        '''
        rotate the dice around the x-axis in a clock-wise 
        fashion. The x-axis is seen as goes perpendicularly 
        with the edge of the maze. (coming into player's eyes)
        It can be seen the dice flips to the right.
        '''
        # face and back stays the same
        # top=>right, right=>bottom, bottom=>left, left=>top
        self.faces = [self.left(), self.right(), self.face(), \
                      self.back(), self.bottom(), self.top()] ; 
        return ; 

    def top(self):
        return self.faces[0] ; 
    def bottom(self):
        return self.faces[1] ; 
    def face(self):
        return self.faces[2] ; 
    def back(self):
        return self.faces[3] ; 
    def left(self):
        return self.faces[4] ;
    def right(self):
        return self.faces[5] ;

def getNextMoves(maze, dice, pos, R, C):
    points = [] ;
    d = (Dice(dice.top(), dice.face()).FlipBackward())  ; 
    points.append((pos[0]-1, pos[1], d.top(), d.face())) ; 

    d = (Dice(dice.top(), dice.face()).FlipForward())  ; 
    points.append((pos[0]+1, pos[1], d.top(), d.face())) ; 
  
    d = (Dice(dice.top(), dice.face()).FlipLeft())  ; 
    points.append((pos[0], pos[1]-1, d.top(), d.face())) ;

    d = (Dice(dice.top(), dice.face()).FlipRight())  ; 
    points.append((pos[0], pos[1]+1, d.top(), d.face())) ;

    points = list(filter(lambda p: p[0] > 0 and p[0] <= R and p[1] > 0 and p[1] <= C, \
                        points)) ; 
    points = list(filter(lambda p: maze[p[0]-1][p[1]-1] == -1 or \
                                   maze[p[0]-1][p[1]-1] == dice.top(), points)) ; 
    return points ; 

def TestGetNextMoves():
    maze = [[-1,2,4],[5,5,6],[6,-1,-1]] ;
    dice = Dice(5, 1) ; 
    R, C = 3,3 ;
    result = getNextMoves(maze, dice, (1,2,dice.top(), dice.face()), R, C) ;
    print(result) ; 
    return ; 

def PrintRoute(name, c,prev, parent):
    result = [] ; 
    result.append('({0},{1})'.format(c[0], c[1])) ;
    result.insert(0, '({0},{1})'.format(prev[0], prev[1])) ; 
    cur = prev ; 
    while parent[cur] != None:
        cur = parent[cur] ; 
        result.insert(0, '({0},{1})'.format(cur[0], cur[1])) ; 

    print(name) ;
    line = "" ;
    for i in range(len(result)):
        if i == 0 or i % 9 == 0:
            line = "  " + result[i]; 
        else:
            line += ","+result[i] ;
            if i % 9 == 8:
                if i < len(result)-1:
                    line += ',' ;
                print(line) ; 
                line = "" ; 
    if line != "":
        print(line) ;

    return ; 

def solve(name, maze, dice, R, C, startRow, startCol):
    target = (startRow, startCol, dice.top(), dice.face()) ; 
    mem = set() ;
    parent = dict() ; 
    parent[target] = None ;
    queue = [target] ;
    while len(queue) > 0:
        # print('queue:', queue) ; # debug
        prev = queue.pop(0) ;
        childs = getNextMoves(maze, Dice(prev[2], prev[3]), prev, R,C) ;
        # print('childs:', childs) ; # debug
        for c in childs:
            if c not in mem:
                mem.add(c) ; 
                if c[0] == target[0] and c[1] == target[1]:
                    # print('Try to print Route') ; # debug
                    PrintRoute(name, c,prev, parent) ; 
                    return ; 
                else:
                    parent[c] = prev ; 
                    queue.append(c) ;
        continue ;
    print(name) ;
    print('  No Solution Possible') ; 
    return  ;

def work(name):
    R,C,startRow,startCol,top,face = [int(n) for n in input().split()] ; 
    maze = [] ;
    for i in range(R):
        line = [int(n) for n in input().split()] ;
        maze.append(line) ;

    dice = Dice(top, face); 
    result = solve(name, maze, dice, R,C, startRow, startCol) ; 
    return ; 

def main():
    while True:
        mazeName = input() ;
        if mazeName == 'END':
            return ; 
        else:
            work(mazeName) ; 
    return ; 

if __name__ == "__main__":
    main() ; 
