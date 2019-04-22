/**
 * Try to use C for the interative solution.
 * Implementing the Chinese Remainder Theorem.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int T, N, M ; 

// return 0 if all ok.
int solve(void)
{
    int numbers[7] = {5, 7, 9, 11, 13, 16, 17} ; 
    int i ; 
    int remain[7] ; 
    int limit = 7 ; // need to change to 7

    // just use 7 nights to figure out.
    for (i=0 ; i < limit ; i++) {
        // set up the windmills
        int num = numbers[i] ; 
        int j ; 
        printf("%d", num) ; 
        for (j=1 ; j < 18 ; j++) {
            printf(" %d", num) ; 
        }
        printf("\n") ; 
        fflush(stdout) ; 

        // read back the result
        int temp = 0; 
        remain[i] = 0 ; 
        for (j=0 ; j < 18 ; j++) {
            scanf("%d", &temp)  ; 
            remain[i] += temp ; 
        }
        remain[i] = remain[i] % numbers[i] ; 
        // printf("remain[%d] = %d\n", i, remain[i]) ; // debug
    }

    // use chinese remainder theorem to calculate the actual number
    int base = numbers[0] ; 
    int start = remain[0] ; 
    for (i=1 ; i < limit ; i++) {
        while ((start % numbers[i]) != remain[i]) {
            start += base ; 
        }
        base = base * numbers[i] ; 
    }
    printf("%d\n", start) ; // debug
    fflush(stdout) ; 

    int verdict ; 
    scanf("%d", &verdict) ; 
    return verdict ;
}

int work(void) 
{
    scanf("%d %d %d", &T, &N, &M) ; 
    int i ; 
    for (i=0 ; i < T ; i++) {
        int temp = solve() ; 
        // printf("temp=%d\n", temp) ; // debug
        if (temp != 1) {
            break ; 
        }
    }
    return 0 ;
}

int main(void)
{
    work() ;
    return 0 ;
}
