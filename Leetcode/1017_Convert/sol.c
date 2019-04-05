/**
 * Leetcode - 1017 Convert to Base -2 (Medium)
 * Author: Ruowei Chen
 * Date: 04/Apr/2019
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * baseNeg2(int N) 
{
    char * result = (char *)malloc(sizeof(char)*64) ; 
    memset(result, 0, sizeof(char)*64) ; 

    if (N == 0) {
        result[0] = '0' ; 
        result[1] = '\0' ; 
        return result ;
    }

    int cur = N ;
    int base = 1 ; 
    int index = 0 ; 
    while (cur > 0) 
    {
        if ((cur & 0x1) == 1) {
            result[index++] = '1' ; 
            cur += (-1)*base ; 
        }
        else {
            result[index++] = '0' ;
        }

        base *= -1 ; 
        cur = cur >> 1 ; 
    }
    result[index] = '\0' ;
    
    // now reverse the 
    int len = strlen(result) ;
    char * buf = (char *)malloc(sizeof(char)*(len+1)) ;
    buf[len] = '\0' ; 
    int i ; 
    for (i=0 ; i < len ; i++) 
    {
        buf[i] = result[len-i-1] ; 
    }
    free(result) ; 
    return buf ; 
}


int main(void)
{
    int i ; 
    for (i=0 ; i <= 10 ; i++) {
        char * result = baseNeg2(i) ; 
        printf("i=%d, result=%s\n", i, result) ; 
        free(result) ; 
    }

    return 0 ; 
}
