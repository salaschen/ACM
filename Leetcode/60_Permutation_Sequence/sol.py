import math ; 

class Solution:
    def getPermutation(self, n, k):
        result = self.helper([x for x in range(1, n+1)], k) ; 
        return result ; 

    def helper(self, numList, k):
        if len(numList) == 1:
            return str(numList[0]) ; 
        else:
            start, rem = self.getStartNumber(numList, k) ; 
            numList.pop(numList.index(start)) ; 
            return str(start) + self.helper(numList, rem);  


    def getStartNumber(self, numList, k):
        # print("numList: ", numList) ; # debug
        f = math.factorial(len(numList)-1) ;
        multi = math.floor((k-1)/f) ;
        rem = k- (multi*f)  ; 
        # print("multi: " , multi, "; rem: ", rem) ; # debug
        return numList[multi], rem  ; 

    def printPermutation(self, n):
        resultList = self.helpPrint([x for x in range(1, n+1)]) ; 
        for i in range(1, len(resultList)+1):
            print(i, resultList[i-1]) ;
    
    def helpPrint(self, numList):
        if len(numList) == 1:
            return [str(numList[0])] ;
        else:
            result = [] ; 
            for i in range(0, len(numList)):
                num = numList[i] ; 
                newList = numList[:] ; 
                newList.pop(newList.index(num)) ; 
                returnList = self.helpPrint(newList) ;
                for s in returnList:
                    result.append(str(num)+s) ;
            return result ;


if __name__ == "__main__":
    s = Solution() ; 
    n, k = 5, 100;
    # print( s.getStartNumber([x for x in range(1, n+1)], k) ) ; 
    s.printPermutation(n) ; 
    # print("n={0}, k={1}".format(n,k)) ; 
    print("-------------") ; 
    print(k, s.getPermutation(n,k) ) ; 
    
