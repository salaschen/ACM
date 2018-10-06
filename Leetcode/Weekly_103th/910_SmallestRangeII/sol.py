class Solution:
    def smallestRangeII(self, A, K):
        A = sorted(A) ; 
        low, up = A[0], A[-1] ;
        ans = up - low ; 

        for i in range(0, len(A)-1):
            temp = max(A[i]+K, up-K) - min(low+K, A[i+1]-K) ;
            ans = min(ans, temp) ;
        return ans ; 

if __name__ == "__main__":
    s = Solution() ; 
    A = [1,3,6] ; 
    K = 3 ; 
    
    print(A,s.smallestRangeII(A,K)) ; 

    A = [1] ; 
    K = 3 ; 
    
    print(A,s.smallestRangeII(A,K)) ; 

    A = [7,8,8]
    K = 5 ;
    print(A,s.smallestRangeII(A,K)) ; 

    A = [9,10,5,9]
    K = 5 ;
    print(A,s.smallestRangeII(A,K)) ; 
    print("expected: 5") ;

    A = [3,4,7,0]
    K = 5 ;
    print(A,s.smallestRangeII(A,K)) ; 
    print("expected: 7") ;

    A = [0,10]
    K = 2 ;
    print(A,s.smallestRangeII(A,K)) ; 


