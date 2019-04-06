def work(Case):
    N = input() ; 
    pos = '';
    zero = '' ; 
    for digit in N:
        num = int(digit) ;
        if num == 0:
            pos += '0' ; 
            zero += '0' ; 
        elif num < 5:
            pos += '1' ; 
            zero += str(num - 1) ; 
        elif num < 9:
            pos += '5' ;
            zero += str(num - 5) ;
        else:
            pos += '6' ; 
            zero += '3' ; 

        temp = pos ; 
        pos = zero ; 
        zero = temp ; 
    
    while zero[0] == '0' and len(zero) > 1 :
        zero = zero[1:] ; 

    while pos[0] == '0' and len(pos) > 1 :
        pos = pos[1:] ; 
            
    print('Case #{0}: {1} {2}'.format(Case, zero, pos)) ; 
    return ; 

def main():
    T = int(input()) ;
    for i in range(1, T+1):
        work(i) ; 

if __name__ == "__main__":
    main() ; 
