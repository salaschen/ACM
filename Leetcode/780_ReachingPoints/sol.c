/**
 * Prob: Leetcode 780 (Hard)
 * Author: Ruowei Chen
 * Date: 27/Mar/2019
 * Note: I'm having a bad day today so tolerate the messy code.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum bool {true, false} bool; 
#define ABS(a) ((a) < 0? (-1*(a)) : (a))

bool reachingPoints(int sx, int sy, int tx, int ty) 
{
    // Quick return
    if (tx < sx || ty < sy) return false ; 
    if (tx <= 0 || ty <= 0) return false ; 

    // keep backtracking (tx, ty) until reach the source.
    while (1) {
        // printf("tx=%d, ty=%d\n", tx, ty) ;  // debug
        if (tx <= 0 || ty <= 0) return false ; 
        if (tx == sx && ty == sy) return true ;  
        
        // if one side is equal, then we study the other side.
        if (tx == sx) {
            if (ty > sy && ((ty-sy) % tx == 0)) {
                return true ; 
            }
        }
        if (ty == sy) {
            if ((tx>sx) && ((tx-sx) % ty == 0)){
                return true ; 
            }
        }
        if (tx == ty) break ;
        // backtrack
        if (tx > ty) {
            tx = tx % ty ; 
            if (tx == 0) tx = ty ; 
        }
        else if (tx < ty) {
            ty = ty % tx ; 
            if (ty == 0) ty = tx ; 
        }
    }
    return false;
}

bool slow(int sx, int sy, int tx, int ty) {
    if (tx < sx || ty < sy) return false ; 
    if (tx == sx && ty == sy) return true ;

    while (1) {
        if (tx == sx && ty == sy) return true ; 
        if (tx > ty) {
            tx = tx - ty ; 
        }
        else if (ty > tx) {
            ty = ty - tx ; 
        }
        else {
            // if tx == ty at this point and it's not the source.
            // it cannot be back tracked any further.
            break ;
        }
    }
    return false ; 
}


int test(void) {
    int sx,sy,tx,ty ; 
    int scanLen = scanf("%d %d %d %d\n", &sx, &sy, &tx, &ty) ; 
    if (scanLen == EOF) return EOF ; 
    bool result = reachingPoints(sx,sy,tx,ty) ; 
    bool expected = slow(sx, sy, tx, ty) ; 
    printf("sx=%d,sy=%d,tx=%d,ty=%d,", sx,sy,tx,ty) ; 
    printf("result=%s, expected=%s\n", result==true? "true" : "false",
            expected==true? "true":"false") ; 

    if (result == expected) return 1 ; 
    else return 0 ; 
}



int main(void)
{
    int pass = 0 ; 
    int total = 0 ;
    while (1) {
        int result = test()  ; 
        if (result == EOF) break ;
        pass += result ; 
        total += 1 ; 
        continue ; 
    } 
    printf("%d/%d cases passed!\n", pass, total) ; 
    return 0 ; 
}
