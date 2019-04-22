'''
GCJ: Golf Gophers
Note: Brute-Force
'''
import sys ;

try:
    input = raw_input; 
except:
    pass;  

def solve(N, M):
    touches = [] ; # 
    for i in range(N):
        output = '18' ;
        for i in range(1, 18):
            output += ' 18' ;
        print(output) ; 
        sys.stdout.flush() ; 
        line = [int(n) for n in input().split()] ; 
        touch = 0 ; 
        for num in line:
            touch += num ; 
        touches.append(touch) ; 
    freq = dict() ; 
    for t in touches:
        if t not in freq:
            freq[t] = 1 ;
        else:
            freq[t] += 1 ; 
    result = None ; 
    for key in freq:
        if result is None or freq[key] > freq[result]:
            result = key ; 
        print(result) ; 
        sys.stdout.flush() ; 
        verdict = int(input()) ; 
    return verdict; 

def work():
    line = input() ; 
    T,N,M = [int(n) for n in line.split()] ; 
    for i in range(T):
        result = solve(N, M) ;  
        if result == -1:
            return -1 ; 

def main():
    work() ; 

if __name__ == "__main__":
    main() ;
