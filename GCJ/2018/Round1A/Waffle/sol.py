'''
Contest: Code Jam 18 Round 1A
Prob: Waffle Chopper
Author: Ruowei Chen
Date: 16/Mar/2019
Note: Version 1 - Brute Force
'''
def solve():
    cake = [] ; # list of list
    R,C,H,V = [int(n) for n in input().split()] ;
    for i in range(R):
        cake.append(input()) ; 
    # print(R,C,H,V) ; # debug
    # print(cake) ; # debug

    # Get the number of chocolates
    numChoco = 0 ; 
    for i in range(R):
        numChoco += len(list(filter(lambda n: n == '@', cake[i]))) ; 
    
    # do some initial quick checking.
    if numChoco == 0:
        return True ; 
    if numChoco % ((H+1)*(V+1)) != 0:
        return False ; 
    unitChoco = numChoco // ((H+1)*(V+1)) ;

    # try the horizontal Cuts
    hCuts = HorizontalCuts(cake, H, numChoco) ;
    if len(hCuts) == 0:
        return False ; 

    # try the vertical cuts 
    # transpose the cake so columns become rows.
    tcake = ['' for n in range(0, len(cake[0]))] ;
    for i in range(0, len(cake)):
        row = cake[i] ; 
        for j in range(0, len(row)):
            tcake[j] += row[j] ; 

    # try the vertical cut as the horizontal cut on the transposed cake
    vCuts = HorizontalCuts(tcake, V, numChoco) ; 
    if len(vCuts) == 0:
        return False ; 

    # now check every piece has the same number of chocolates
    for hCut in hCuts:
        for vCut in vCuts:
            num = numChocolates(cake, hCut, vCut) ; 
            if num != unitChoco:
                return False ; 

    return True ; 

def numChocolates(cake, rowNums, colNums):
    rows = cake[rowNums[0]-1:rowNums[-1]] ; 
    result = 0 ; 
    for row in rows:
        col = row[colNums[0]-1:colNums[-1]] ; 
        result += len(list(filter(lambda n: n == '@', col))) ; 
    return result ; 

# return a list of rows that represent the H+1 slices 
# after the cut.
# for example, [[1,2], [3,4], [5],[6]]
# return [] if non is possible.
def HorizontalCuts(cake, H, numChoco):
    accu = [] ; 
    cur = 0 ; 
    for row in cake:
        cur += len(list(filter(lambda n: n == '@', row))) ; 
        accu.append(cur) ; 

    # if you cannot evenly divide the chips in H+1 rows, it's IMPOSSIBLE.
    if numChoco % (H+1) != 0:
        return [] ; 

    rowUnit = numChoco // (H+1) ; 
    result = [] ; 
    temp = 0 ; 
    cur = [] ; 
    for i in range(1, len(cake)+1):
        temp += len(list(filter(lambda n: n == '@', cake[i-1]))) ; 
        cur.append(i) ; 
        if temp == rowUnit:
            result.append(cur) ; 
            cur = [] ; 
            temp = 0 ; 
        elif temp > rowUnit:
            return [] ; 
    
    if len(result) != H+1:
        return [] ;
    else:
        return result ; 

def work():
    T = int(input()) ; 
    for i in range(1, T+1):
        if solve():
            print("Case #{0}: POSSIBLE".format(i)) ; 
        else:
            print("Case #{0}: IMPOSSIBLE".format(i)) ; 
    return ;

def main():
    work() ; 

if __name__ == "__main__":
    main() ; 
