import functools
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s;  
        lines = ['' for x in range(numRows)] ; 
        curLine = 0 ; 
        step = 1 ; 
        for i in range(len(s)):
            lines[curLine] += (s[i]) ; 
            if curLine == numRows-1:
                step = -1 ; 
            elif curLine == 0:
                step = 1 ; 
            curLine += step ; 

        # print(lines) ; # debug
        return functools.reduce(lambda x,y: x+y, lines) ; 

def main():
    sol = Solution() ; 
    s = 'PAYPALISHIRING' ; 
    numRows = 2 ; 
    print(sol.convert(s, numRows)) ; 
    return ;

if __name__ == "__main__":
    main() ;


