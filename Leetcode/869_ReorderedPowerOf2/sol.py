class Solution:
    def __init__(self):
        self.strings = set() ; 
        cur = 1 ; 
        power = 0 ; 
        while power <= 30:
            self.strings.add(str(sorted(str(cur)))) ; 
            cur *= 2 ; 
            power += 1 ;
    

    def reorderedPowerOf2(self, N):
        '''
        :type N: int
        :rtype: bool
        '''
        return str(sorted(str(N))) in self.strings ; 

class Solution2:
    def reorderedPowerOf2(self, N):
        cur = 1 ; 
        strN = sorted(str(N)) ; 
        lN = len(strN) ;
        while True:
            strcur = sorted(str(cur)) ;
            lcur = len(strcur) ; 
            if lcur == lN and strcur == strN:
                return True ;
            elif lcur > lN:
                return False ; 
            else:
                cur *= 2 ; 
        return False ;

import random
import time
if __name__ == "__main__":
    
    '''
    aList = [1,10,16,24,46] ;
    for a in aList:
        print("Input: {0}, Output:{1}".format(a, s.reorderedPowerOf2(a))); 
    '''
    numTest = 2000 ; 
    aList = [] ;
    for i in range(0, numTest):
        aList.append(random.randint(1, 10**9)) ;
        
    start = time.time() ; 
    r1 = [] ;
    for a in aList:
        s = Solution() ;
        r1.append(s.reorderedPowerOf2(a)); 
    end = time.time() ;
    print("old uses {0} milliseconds for {1} cases".format((end-start)*1000, numTest)) ; 

    start = time.time() ; 
    r2 = [] ;
    for a in aList:
        s = Solution2() ;
        r2.append(s.reorderedPowerOf2(a)); 
    end = time.time() ;
    print("new uses {0} milliseconds for {1} cases".format((end-start)*1000, numTest)) ; 
    
    print("new is the same with old {0}".format(r1 == r2)) ; 


