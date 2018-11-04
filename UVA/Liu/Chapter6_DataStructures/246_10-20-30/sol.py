'''
UVa246 ACM/ICPC World Finals 1996, 10-20-30
Date: 03/Nov/2018
'''
def TestCheckPile():
    pile = [5,8,7,7,3] ; 
    cards = [1,2,3] ;
    print('Before:') ; 
    print('pile:', pile) ; 
    print('cards:', cards) ; 

    result = CheckPile(pile, cards) ; 
    print('pile:', pile) ; 
    print('cards:', cards) ; 
    print('result:', result) ;
    return ; 

def CheckPile(pile, cards):
    # Try to pick up cards from pile and put back to the cards
    # return True if such pick up is possible.
    if len(pile) < 3: 
        return False ; 

    # Check the first two and last one.
    if (pile[0]+pile[1]+pile[-1]) % 10 == 0:
        cards.append(pile.pop(0)) ; 
        cards.append(pile.pop(0)) ; 
        cards.append(pile.pop(-1)) ; 
        return True ; 
    
    # check the first one and last two.
    if (pile[0]+pile[-1]+pile[-2]) % 10 == 0:
        cards.append(pile.pop(0)) ; 
        cards.append(pile.pop(-2)) ; 
        cards.append(pile.pop(-1)) ; 
        return True ; 

    # check the last three cards
    if (pile[-3]+pile[-2]+pile[-1]) % 10 == 0:
        cards.append(pile.pop(-3)) ; 
        cards.append(pile.pop(-2)) ; 
        cards.append(pile.pop(-1)) ; 
        return True ;

    return False; 

def PlayCard(cards):
    # cards is List[int]
    result, count = "Loss", 0 ; 
    piles = [[] for n in range(7)]; 
    memory = set() ; # to capture the state of the game.
    # Deal the initial piles
    for i in range(7):
        piles[i].append(cards.pop(0)) ;
        count += 1 ;
    memory.add(MakeSnapShot(cards, piles)) ; 
    targetPile = 0 ; 
    while True:
        # if no card is remaining in the cards stack, then it's a loss.
        if len(cards) == 0:
            result = "Loss" ;
            break ; 

        # deal a card to the target Pile
        card = cards.pop(0) ; 
        piles[targetPile].append(card) ; 
        count += 1 ;
        snapshot = MakeSnapShot(cards, piles) ; 
        # print('snapshot:', snapshot) ; # debug
        # print('memory:', memory) ; # debug
        # print('snapshot in memory:', snapshot in memory) ; # debug
        if snapshot in memory:
            result = "Draw" ; 
            break ; 
        else:
            memory.add(snapshot) ; 
        
        # check the pile to see any card can be picked up.
        pickedUpCard = False ;
        while CheckPile(piles[targetPile], cards):
            pickedUpCard = True ; 
            continue ; 

        if pickedUpCard:
            snapshot = MakeSnapShot(cards, piles) ; 
            if snapshot in memory:
                result = "Draw" ; 
                break ; 
            else:
                memory.add(snapshot) ; 

        # check if the target pile becomes empty
        # if so, delete from the piles and clear the memory.
        if len(piles[targetPile]) == 0:
            piles.pop(targetPile) ; 
            if len(piles) == 0:
                result = 'Win' ; 
                break ; 
            targetPile = targetPile ; 
            # memory = set() ;
        else:
            targetPile += 1 ; 
            
        # Set the correct targetPile
        if targetPile >= len(piles):
            targetPile = 0 ; 
        
        continue ; # continue the next loop

    return (result, count) ; 

def MakeSnapShot(cards, piles) :
    '''
    return a string represents the state of the game.
    Each pile is enclosed within ().
    For example a pile has card 5,3,4 from first to last.
    Then its representation is (5,3,4).
    Cards are enclosed within () as well, from top to bottom.
    It will begin with the piles snapshot then the cards.
    '''
    result = [] ; 
    for p in piles:
        result.append('(' + JoinListToString(p) + ')') ; 
    result.append('(' + JoinListToString(cards) + ')') ;
    return JoinListToString(result) ; 

def JoinListToString(lst, sep = ','):
    if len(lst) == 0: return '' ; 
    result = str(lst[0]);
    for i in range(1, len(lst)):
        result += sep + str(lst[i]) ; 
    return result ; 
       

def GetToWork(line1):
    cards = [int(n) for n in line1.split()] ;
    while len(cards) < 52:
        line = input() ;
        cards.extend([int(n) for n in line.split()]) ; 
    # print(cards) ; # debug
    
    result, count = PlayCard(cards) ; 
    print("{0:4}: {1}".format(result, count)) ;
    return ;

def work():
    while True:
        l1 = input() ; 
        if l1[0] == '0':
            return ; 
        else:
            GetToWork(l1) ;
    return ; 

def main():
    work() ; 

if __name__ == "__main__":
    main() ; 
