class Solution:
    def __init__(self):
        self.mem = dict() ; 

    def maxUncrossedLines(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return 0 ; 
        
        if (len(A), len(B)) in self.mem:
            return self.mem[(len(A), len(B))] ; 

        if A[0] == B[0]:
            self.mem[(len(A),len(B))] = 1 + self.maxUncrossedLines(A[1:], B[1:]) ; 
            return 1 + self.maxUncrossedLines(A[1:], B[1:]) ; 

        m1 = 0 ; 
        if A[0] in B[1:]:
            bindex = B.index(A[0]) ; 
            m1 = 1 + self.maxUncrossedLines(A[1:], B[bindex+1:]) ; 
         
        m2 = 0 ; 
        if B[0] in A[1:]:
            aindex = A.index(B[0]) ;
            m2 = 1 + self.maxUncrossedLines(A[aindex+1:], B[1:]) ; 

        m3 = self.maxUncrossedLines(A[1:], B[1:]) ;
        result = max(m1,m2,m3) ; 
        self.mem[(len(A), len(B))] = result ; 
        return result ; 

def main():
    s = Solution() ; 
    A = [1,4,2] ; B = [1,2,4] ; 
    result = s.maxUncrossedLines(A,B) ; 
    print(result) ; 
    
   
    A = [2,5,1,2,5] ; B = [10,5,2,1,5,2] ; 
    result = s.maxUncrossedLines(A,B) ; 
    print(result) ; 

    s = Solution() ;
    A = [1,3,7,1,7,5] ; B = [1,9,2,5,1] ; 
    result = s.maxUncrossedLines(A,B) ; 
    print(result) ; 

    return ;

if __name__ == "__main__":
    main() ; 
