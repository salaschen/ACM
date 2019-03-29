/**
 * Leetcode: 518 Coin Change 2
 * Author: Ruowei Chen
 * Date: 29/Mar/2019
 * Note: Classic DP
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int intCmp(const void *i1, const void *i2)
{
    return *(int *)i1 - *(int *)i2 ; 
}

int change(int amount, int * coins, int coinsSize)
{
    if (amount == 0) return 1 ; 
    if (coinsSize == 0) return 0 ;

    qsort(coins, coinsSize, sizeof(int), intCmp) ; 
    int * dp1 = (int *)malloc(sizeof(int)*(amount+1));     
    
    int i ; 
    int curCoin = coins[0] ; 
    for (i=0 ; i <= amount ; i++) 
    {
        if (i % curCoin == 0) {
            dp1[i] = 1 ; 
        }
        else {
            dp1[i] = 0 ; 
        }
        // printf("cur=%d, cur[%d]=%d\n", curCoin, i, dp1[i]) ; // debug
    }
    dp1[0] = 1 ; 
    int * cur = dp1 ; 

    // now use dp to step through all the other coins.
    int j ; 
    for (j=1 ; j < coinsSize ; j++) {
        curCoin = coins[j] ; 
        for (i=curCoin ; i <= amount ; i += 1) {
            cur[i] = cur[i] + cur[i-curCoin]; 
            // printf("cur=%d, cur[%d]=%d\n", curCoin, i, cur[i]) ; // debug
        }
    }

    int result = cur[amount] ; 
    free(dp1) ;

    return result ;
}

int test(void)
{
    int amount = 100 ; 
    int coins[] = {1,2,5, 10} ; 

    int result = change(amount, coins, 4) ; 
    printf("result=%d\n", result) ; 
    return 0 ; 
}

int main(void)
{
    test() ; 
    return 0 ;
}
