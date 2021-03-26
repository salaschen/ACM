'''
Prob: ReverseSort
Author: Ruowei Chen
Date: 27/03/2021
'''

# return the index of the smallest number in the list
def findSmallest(numList: [int]) -> int:
    temp = 1000 ;
    pos = -1 ;
    for i in range(len(numList)):
        if numList[i] < temp:
            pos = i ;
            temp = numList[i] ; 
    return pos ; 

def reverseList(numList: [int]) -> [int]:
    result = [] ;
    for i in range(len(numList)-1, -1, -1):
        result.append(numList[i]) ;
    return result ; 

def work(numList: [int]):
    result = 0 ;
    curList = numList[:] ; 
    for i in range(len(curList)-1):
        pos = findSmallest(curList) ; 
        result += (pos+1) ; 
        curList = reverseList(curList[:pos+1]) + curList[pos+1:];
        curList = curList[1:] ;
    return result ; 


T = int(input()) ; 
for i in range(T):
    N = int(input()) ;
    numList = [int(x) for x in input().split()] ;
    result = work(numList) ;
    print("Case #{0}: {1}".format(i+1, result)) ;


