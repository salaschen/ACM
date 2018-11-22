'''
UVa 725 Division
Date: 19/Nov/2018
'''
import time

def HasDuplicate(string):
    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return True ;
    return False ;

def HasInterSection(string1, string2):
    for s in string1:
        if s in string2:
            return True ;
    return False ; 

def work(Case, FList, FNumList):
    N = int(input()) ; 
    if N == 0:
        return 1 ; 

    if Case > 1:
        print() ; 
    if N > 79: 
        print("There are no solutions for {0}.\n".format(N)) ;
        return 0 ; 
    
    num = 0 ; 
    line = "" ;
    for i in range(len(FList)):
        F = FList[i] ; 
        fnum = FNumList[i] ; 
        anum = fnum * N ; 
        A = str(anum) ;
        if '0' not in A and '0' not in F:
            A = '0' + A ; 
        if HasDuplicate(A):
            continue ; 
        if len(A) != 5:
            continue ;
        # if len((set(A)).intersection(set(F))) == 0:
        if not HasInterSection(A, F):
            line = "{0} / {1} = {2}".format(A,F,N) ; 
            print(line) ; 

    if line == "":
        print("There are no solutions for {0}.".format(N)) ; 
    return 0 ;

def expand(digits, level):
    if len(digits) == 0:
        return [] ; 
    if len(digits) == 1:
        return digits ; 
    if level == 5:
        return [""] ;
    else:
        result = [] ; 
        if level == 10:
            R = range(0, 5); 
        else:
            R = range(len(digits)) ; 
        for i in R:
            head = digits[i] ; 
            subArrays = digits[0:i] + digits[i+1:] ; 
            for d in expand(subArrays, level-1):
                result.append(head+d) ; 
        return result ; 

def main():
    start = time.time() ; 
    FList = expand(\
            list(map(lambda n: str(n),\
                list(range(10)))), 10) ; 
    # print('FList:', FList); # debug
    end = time.time() ; 

    FNumList = list(map(lambda n: int(n), FList)) ; 
    # print("len(FList)={0}".format(len(FList))) ; # debug
    Case = 1 ; 
    while work(Case, FList, FNumList) == 0:
        Case += 1 ;
        continue ; 

if __name__ == "__main__":
    main() ;
