'''
Note: 
    1) 
'''
class Space:
    def __init__(self, point):
        self.length = 0 ;
        self.points = [] ; 
        self.start = point ;
    
    def __str__(self):
        return "start: {2}\n length: {0}, points:{1}".format(self.length, self.points, self.start) ;
    
class Solution:
    def isOut(self, x, y):
        return x < 0 or x >= self.m or y < 0 or y >= self.n ;

    def readVertical(self, startPoint):
        # return a point
        x,y = startPoint ; 
        if self.isOut(x,y):
            return None ; 
        if self.board[x][y] == "#":
            return None ;
        s = Space(startPoint) ; 
        # print("start: ", startPoint) ; # debug
        while x < self.m:
            # print("x,y={0}".format(x,y)) ; # debug
            if self.board[x][y] == "#":
                return s ; 
            s.length += 1 ;
            if self.board[x][y] != " ":
                s.points.append((s.length-1, self.board[x][y])) ; 
            x += 1 ;
        return s ;

    def readHorizontal(self, startPoint):
        # return a point
        x,y = startPoint ; 
        if self.isOut(x,y):
            return None ; 
        if self.board[x][y] == "#":
            return None ;
        s = Space(startPoint) ; 
        while y < self.n:
            if self.board[x][y] == "#":
                return s ; 
            s.length += 1 ;
            if self.board[x][y] != " ":
                s.points.append((s.length-1, self.board[x][y])) ; 
            y += 1 ;
        return s ; 

    def matchSpace(self, word, space: Space):
        if self.wordLen != space.length:
            return False ;
        for point in space.points:
            pos, ch = point ;
            if word[pos] != ch:
                return False ; 



        return True ; 

    def placeWordInCrossword(self, board: [[str]], word: str) -> bool:
        self.board = board ;
        self.m = len(board) ;
        self.n = len(board[0]) ;
        self.wordLen = len(word) ; 
        self.revWord = word[::-1] ;

        # now get the start points
        blocks = [] ; 
        vertical = [] ;
        horizontal = [] ; 
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == "#":
                    blocks.append((i,j)) ;
                    horizontal.append((i,j+1)) ;
                    vertical.append((i+1,j)) ;

        for i in range(self.m):
            horizontal.append((i,0)) ;
        for j in range(self.n):
            vertical.append((0, j)) ; 
       
        spaceList = []  ;
        for point in horizontal:
            temp = self.readHorizontal(point) ;
            if temp is not None:
                if self.matchSpace(word, temp) or self.matchSpace(self.revWord, temp):
                    return True ; 
            
        for point in vertical:
            temp = self.readVertical(point) ; 
            if temp is not None:
                if self.matchSpace(word, temp) or self.matchSpace(self.revWord, temp):
                    return True ;

        return False ; 
        

s = Solution() ; 
board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]] ;
word = "abc" ; 
print(s.placeWordInCrossword(board, word)) ;
board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]];
word = "ac" ; 
print(s.placeWordInCrossword(board, word)) ;
board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]] ;
word = "ca" ;
print(s.placeWordInCrossword(board, word)) ;
board = [["#"," ","#"],["#"," ","#"],["#"," ","c"]]
word = "ca"
print(s.placeWordInCrossword(board, word)) ;
