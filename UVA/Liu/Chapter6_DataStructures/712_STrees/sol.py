def work(num, Case):
    ordering = [int(n[1])-1 for n in input().split()] ; 
    tree = input() ; 
    num  = int(input()) ; 
    result = "" ; 
    for i in range(num):
        vv = input() ; 
        result += evaluate(tree, ordering, vv) ; 
    print('S-Tree #{0}:'.format(Case)) ; 
    print(result) ; 
    print() ; 
    return ; 

def evaluate(tree, ordering, vv):
    t = tree[:] ; 
    for o in ordering:
        # print(t) ; # debug
        value = vv[o] ; 
        tlen = len(t) ; 
        # print('tlen:', tlen) ; # debug
        if value == '1':
            t = t[tlen//2:] ;
        else:
            t = t[:tlen//2] ;
    return t[0] ; 

def main():
    Case = 1 ;
    while True:
        num = int(input()) ; 
        if num == 0:
            break; 
        work(num, Case) ; 
        Case += 1 ; 
    return ;


if __name__ == "__main__":
    main() ;
