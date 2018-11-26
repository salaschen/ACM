'''
UVa 524 - Prime Ring Problem
Date: 23/Nov/2018
'''

evenCandidates = [];
oddCandidates = [] ;

def MakePrimes(up):
    primes = [2,3]; 
    cur = 5 ; 
    while cur <= up:
        isPrime = True ;
        for p in primes:
            if cur % p == 0:
                isPrime = False ;
                break ;         
        if isPrime:
            primes.append(cur) ;
        cur += 2 ;
    return set(primes) ; 

def work(Case, N, primes):
    ResultSet = set() ; 
    lst = [1] ; 
    lst.extend([0 for n in range(N-1)]) ;
    evenCand = list(range(2, N+1, 2)) ;
    oddCand = list(range(3, N+1, 2)) ; 

    search(lst,1, N, primes, ResultSet, evenCand, oddCand);
    
    resultList = list(sorted(list(ResultSet))) ; 
    resultList = list(\
            map(lambda lst: \
            list(map(lambda char: ord(char)-ord('A')+1, lst)), \
            sorted(list(ResultSet)))) ; 

    if Case > 1:
        print() ; 
    print('Case {0}:'.format(Case)) ; 
    for lst in resultList:
        line = str(lst[0]) ; 
        for i in range(1, len(lst)):
            line += ' ' + str(lst[i]) ; 
        print(line) ;
    return ; 

def search(lst, level, N, primes, ResultSet, evenCand, oddCand):
    if level >= N :
        if (lst[-1] + 1) in primes:
            ResultSet.add(lstJoin(list(map(lambda n: chr(ord('A')+n-1), lst)))) ; 
            ResultSet.add(lstJoin(list(map(lambda n: chr(ord('A')+n-1), \
                    lst[0:1] + ReverseList(lst[1:]))))) ; 
    else:
        candidates = [] ; 
        if level % 2 == 1:
            # candidates = list(range(2, N+1, 2)) ; 
            candidates = evenCand ; 
        else:
            # candidates = list(range(3, N+1, 2)) ; 
            candidates = oddCand ;
        # print('candidates:', candidates) ; # debug
        for cand in candidates:
            if cand not in lst and (cand+lst[level-1]) in primes:
                lst[level] = cand ;
                search(lst, level+1, N, primes, ResultSet, evenCand, oddCand) ; 
        lst[level] = 0 ; 
    return ;

def lstJoin(strList, separator=''):
    result = "" ; 
    for s in strList:
        result += s + separator;
    return result.strip(separator) ; 
        
def ReverseList(lst):
    lst.reverse() ; 
    return lst ;

def main():
    primes = MakePrimes(50) ;
    Case = 1 ; 
    while True:
        try:
            N = int(input()) ; 
            work(Case, N, primes) ;
        except Exception as inst:
            # print(inst) ; # debug
            break ;
        Case += 1 ;
    return ;

if __name__ == "__main__":
    main() ; 
