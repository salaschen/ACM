def CanMove(p1, p2):
    # return bool
    # p1 and p2 are two piles
    if len(p1) == 0 or len(p2) == 0:
        return False ;
    c1, c2 = p1[len(p1)-1], p2[len(p2)-1] ; 
    if c1[0] == c2[0] or c1[1] == c2[1]:
        return True ; 
    else:
        return False ; 

def work(l1, l2):
    whole = l1 + ' ' + l2 ; 
    piles = [ [card] for card in whole.split()]

    curPile = 1 ; 
    while True:
        if len(piles) == 1 or curPile >= len(piles):
            break ; 
        movePile = -1 ; 
        if curPile-1 >= 0 and CanMove(piles[curPile], piles[curPile-1]):
            movePile = curPile-1 ; 
        if curPile-3 >= 0 and CanMove(piles[curPile], piles[curPile-3]):
            movePile = curPile-3 ; 

        # no card can be moved
        if movePile == -1:
            curPile += 1 ; 
        else:
            card = piles[curPile].pop() ; 
            piles[movePile].append(card) ; 
            if len(piles[curPile]) == 0:
                piles.pop(curPile) ; 
            curPile = movePile ; 

    # print answers
    if len(piles) == 1:
        print("1 pile remaining: 52"); 
    else:
        result = "{0} piles remaining:".format(len(piles)) ; 
        for i in range(len(piles)):
            result += " {0}".format(len(piles[i])) ; 
        print(result) ;
    return ; 

def main():
    while True:
        try:
            l1 = input() ; 
            l2 = input() ; 
            work(l1, l2) ; 
        except:
            return ; 
    return ; 

if __name__ == "__main__":
    main() ; 
