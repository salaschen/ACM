/**
 * Leetcode - 1018 Binary Prefix Divisible by 5 (Easy)
 * Author: Ruowei Chen
 * Date: 04/Apr/2019
 */
#include <stdio.h>
typedef enum bool {true, false} ; 

bool * prefixesDivBy5(int *A, int ASize, int * returnSize)
{
    bool * result = (bool *)malloc(sizeof(bool)*ASize) ; 
    *returnSize = ASize ;

    int i ; 
    int cur = 0 ; 
    for (i=0 ; i < ASize ; i++) {
        cur = ((cur << 1) + A[i]) % 5  ; 
        if (cur == 0) {
            result[i] = true ; 
        }
        else {
            result[i] = false ; 
        }
    }
    return result ; 
}
