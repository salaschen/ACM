'''
Interactive problem
Author: Ruowei Chen
Date: 04/May/2019
Note:
    1) Brute force to solve the first one.
    2) Update: 08/May/2019. Solve the harder case after reading the 
    analysis.
'''
import sys ;
import random ;

try:
    input = raw_input;
except NameError:
    pass 

def helper(path, level):
    if level == 5:
        return path; 
    else:
        choices = ['A','B','C','D','E'] ;           
        for _ in range(len(path)):
            cur = path.pop(0) ; 
            for c in choices:
                if c not in cur:
                    path.append(cur+c) ; 
        return helper(path, level+1) ; 

def genPermutations():
    result = helper(['A','B','C','D','E'], 1) ; 
    return result ; 

def shelfPos(setNum, setPos):
    return (setNum-1)*5+setPos ; 

def factorial(num):
    if num < 0:
        return 0 ; 
    if num == 0:
        return 1 ; 
    else:
        return num * factorial(num-1) ; 

# setNum: List[int], the number of set to be queried.
# posNum: the position of each set to be queried.
# return: tuple(string, List[int]) where the first string
# is the missing figure on the posNum of the missing set.
# and List[int] is the list of set number to look into for
# the next round of querie. If it's empty, meaning all the figures
# have been figured out.
def queryPos(result, setNum, posNum):
    # print('setNum', setNum, file=sys.stderr) ; # debug
    # special case:
    team = ['A','B','C','D','E'] ;

    # remove all the figures that are already in the result.
    for c in result:
        team.remove(c) ; 

    if len(setNum) == 1:
        pos = shelfPos(setNum[0], posNum) ;
        print(pos) ; 
        sys.stdout.flush() ; 
        fig = input() ; 
        
        for t in team:
            if t not in result and t not in fig:
                fig = t + fig ;         
                break ;

        return (fig, []) ; 

    
    mem = dict() ; 
    for member in team:
        mem[member] = [] ; 

    # query all the positions and record the result.
    for sn in setNum:
        pos = shelfPos(sn, posNum) ; 
        print(pos) ; 
        sys.stdout.flush() ; 
        fig = input() ; 
        mem[fig].append(sn) ;   
        
    target = factorial(5-posNum) ; 
    for member in team:
        if len(mem[member]) < target:
            return (member, mem[member]) ; 
    
    return ('', []) ; 

# to guess the missing set using 150 queries.
def work2():
    result = '' ; 
    queue = [i for i in range(1, 120)] ;
    pos = 1 ;
    while len(result) < 4:
        member, newQueue = queryPos(result, queue, pos) ; 
        # print(member, newQueue, file=sys.stderr) ; # debug
        result = result + member ; 
        queue = newQueue ; 
        pos += 1 ; 

    team = ['A','B','C','D','E'] ;
    for t in team:
        if t not in result:
            result = result + t ; 
            break ; 

    print(result) ; 
    # print(result, file=sys.stderr) ; # debug
    sys.stdout.flush() ; 
    verdict = input() ; 
    return verdict ; 

def work():
    fullSet = genPermutations() ; 

    # get the first 118 set

    ignoreSet = random.randint(1, 119) ; 
    ignore = '' ;
    
    for i in range(0, 119):
        cur = '' ;
        num = 4 ; 
        if i+1 == ignoreSet:
            num = 3 ; 
        for j in range(1, 1+num):
            pos = i*5 + j ;
            print(pos) ; 
            sys.stdout.flush() ; 
            f = input() ; 
            cur = cur + f ; 

        choices = ['A','B','C','D','E'] ;
        if len(cur) == 4:
            for c in choices:
                if c not in cur:
                    cur = cur + c ; 
                    break ;
        else:
            ignore = cur ; 
        
        if len(cur) == 5 and cur in fullSet:
            fullSet.remove(cur) ; 

    # get the last set on the shelf 
    last = ignore ; 
    first = fullSet[0] ;
    if first[0] == last[0] and first[1] == last[1] and first[2] == last[2]:
        print(fullSet[1]) ; 
    else:
        print(first) ; 
    sys.stdout.flush() ;

    # get the verdict
    verdict = input() ; 
    return verdict ;

def solve():
    T, F = [int(n) for n in input().split()] ; 
    '''
    if F == 150:
        print(-1) ; # give up straight away.
        sys.stdout.flush() ; 
        return ;
    '''

    for i in range(T):
        result = work2() ; 
        if result == 'N':
            return ;

def main():
    solve() ;
    return ;

if __name__ == "__main__":
    main() ; 
