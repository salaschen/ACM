/**
 * Prob: 357 - Count Numbers with Unique Digits
 * Date: 10/Mar/2019
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>

// all numbers of n digits that with unique digits
int countDigits(int n) {
    if (n == 1) {
        return 10 ; 
    }
    else if (n > 10 || n < 1) {
        return 0 ; 
    }
    else {
        int result = 9 ;
        int digits ; 
        for (digits = 1 ; digits < n ; digits ++) {
            result *= (10-digits) ; 
        }
        return result ; 
    }
}

int countNumbersWithUniqueDigits(int n) {
    if (n == 0) return 1 ; 
    if (n > 10) {
        n = 10 ; 
    }
    int i = 1 ; 
    int result = 0 ;
    for (i=1 ; i <= n ; i++) {
        result += countDigits(i) ; 
    }
    return result ; 
}

int main(void)
{
    int i = 0 ; 
    for (i=0 ; i <= 10 ; i++) {
        printf("[%d]=%d\n", i, countNumbersWithUniqueDigits(i)) ; 
    }
    return 0 ; 
}
