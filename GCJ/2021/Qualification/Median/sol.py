'''
Prob: Google Code Jam 2021 Qualification - median sort
Author: Ruowei Chen
Date: 03/May/2021
Note: 
    1) Implentation of the Test Set 1 & 2 iaw the official solution.
'''
import random 
from functools import reduce
import sys
import suit

class Solution:
    def __init__(self, T, N, Q, QFunc=None):
        self.T = T ; 
        self.N = N ; 
        self.Q_limit = Q ; 
        self.Q = 0 ;
        self.QFunc = QFunc ; 
    
    def listToString(self, aList):
        return reduce((lambda a,b: str(a)+' '+str(b)), \
                      aList, '').strip() ; 

    # main solve function.
    def solve(self):
        for i in range(self.T):
            result = self.work() ;
            print(self.listToString(result)) ; 
            sys.stdout.flush() ;
            output = int(input()) ; 
            if output == -1:
                break ;
        return ;

    # return the mid point of the given number list
    # will return -1 if any thing goes wrong.
    def query(self, numList):
        if self.QFunc is not None:
            result = self.QFunc(numList) ;
            return result ; 
        else:
            a,b,c = numList ; 
            print(self.listToString([a,b,c])) ;           
            sys.stdout.flush() ;
            result = int(input()) ; 
            if result == -1:
                sys.exit() ; 
            return result ; 

    # return -1 if any error, otherwise return [boundA, boundB] ;
    # tested
    def getbounds(self):
        candidates = [i for i in range(1, self.N+1)] ;
        while len(candidates) > 2:
            a,b,c = candidates[0:3] ;
            candidates = candidates[3:] ;
            mid = self.query([a,b,c]) ;
            if mid == -1:
                return -1 ;
            else:
                temp = set([a,b,c]) ;
                temp.discard(mid) ; 
                candidates += list(temp) ;
        # print('query: {0}'.format(q)) ; 
        return candidates ; 

    # compare numA and numB, return True if numA < numB, False otherwise.
    def lessThan(self, lower, numA, numB):
        result = self.query([lower, numA, numB]); 
        return result == numA ; 

    # sort the numList
    def mergeSort(self, numList, lower):
        nlen = len(numList) ; 
        if nlen >= 2: 
            l1 = numList[:nlen//2] ; 
            l2 = numList[nlen//2:] ;
            l1 = self.mergeSort(l1, lower) ; 
            l2 = self.mergeSort(l2, lower) ; 
            result = [] ; 
            while len(l1) > 0 and len(l2) > 0:
                if self.lessThan(lower, l1[0], l2[0]):
                    result.append(l1[0]) ; 
                    l1 = l1[1:] ;
                else:
                    result.append(l2[0]) ; 
                    l2 = l2[1:] ;
            result = result + l1 + l2 ; 
            return result ; 
        else:
            return numList ;

    # function for solving a single case
    # return 1 if successful, -1 otherwise.
    def work(self):
        # get the bounds first. 
        bounds = self.getbounds() ; 
        if bounds == -1:
            return -1 ; 
        lower, upper = bounds[0], bounds[1] ; # just pick any number as the lower bound.
        
        # use the lessThan function for the merge sort.
        numList = list(set([i for i in range(1, self.N+1)]) - set([lower, upper])) ; 
        numList = self.mergeSort(numList, lower) ;
        return [lower] + numList + [upper]; 

##### main #####
def main():
    T, N, Q = [int(i) for i in input().split(" " )] ;
    s = Solution(T, N, Q) ; 
    s.solve() ;
    return ;

def test():
    N = 50 ;
    t = suit.tester(N) ;
    s = Solution(1, N, 300, t.query); 
    print(s.getbounds()) ; 
    print(s.work()) ;
    print(t.numList) ; 

if __name__ == "__main__":
    main() ; 
    # test(); 

