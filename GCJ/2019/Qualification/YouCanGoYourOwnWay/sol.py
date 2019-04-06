def IsCrossOver(moves):
    if moves[0] == moves[-1]:
        return True ; 
    else:
        return False ; 

def opposite(move):
    if move == 'S':
        return 'E' ; 
    else:
        return 'S' ;

def work(Case):
    N = int(input()) ; 
    lmoves = input() ; 
    mymoves = '' ; 
    if IsCrossOver(lmoves):
        # do something
        moveToLook = opposite(lmoves[0]);
        seen = 0 ; 
        for i in range(0, len(lmoves)-1):
            if lmoves[i] == moveToLook and lmoves[i+1] == moveToLook:
                seen += 1 ; 
                break ; 
            elif lmoves[i] == moveToLook:
                seen += 1 ; 
        mymoves = moveToLook * seen ; 
        mymoves = mymoves + (lmoves[0] * (N-1)) ; 
        mymoves = mymoves + moveToLook * (N-1-seen) ; 
    else:
        # do something else
        first = opposite(lmoves[0]) ; 
        mymoves = first * (N-1) ; 
        mymoves = mymoves + (lmoves[0] * (N-1)) ; 

    print('Case #{0}: {1}'.format(Case, mymoves)) ; 
    return ;

def main():
    T = int(input()) ; 
    for i in range(1, T+1):
        work(i) ; 

if __name__ == "__main__":
    main() ; 
