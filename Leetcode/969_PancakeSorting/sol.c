/**
 * Leetcode 969 Panckage Sorting (Medium)
 * Author: Ruowei Chen
 * Date: 18/April/2019
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


// simulate the fliping of the array.
// will "flip" the first k element in A.
// assume A has more than k elements.
void flip(int *A, int k)
{
    // do nothing if only 1 element is flip.
    if (k <= 1) return ; 

    int head = 0 ; 
    int tail = k-1 ; 
    while (head < tail)
    {
        int temp = A[head] ;
        A[head] = A[tail] ;
        A[tail] = temp ;
        head ++ ; 
        tail -- ;
    }
}

void printArray(int *A, int num)
{
    printf("["); 
    int i ;
    for (i=0 ; i < num-1; i++) {
        printf("%d,", A[i]) ;
    }
    printf("%d]\n", A[num-1]) ; 
}

void insertFlip(int *flips, int *numFlip, int action)
{
    if (action <= 1) return ; 
    flips[*numFlip] = action ;
    *numFlip += 1 ; 
}

void Move(int * A, int pos, int * flips, int * numFlip)
{
    // use linear search.   
    int target = A[pos] ; 
    int insPos ; 
    for (insPos = 0 ; insPos < pos ; insPos ++) {
        if (A[insPos] > target) {
            break ; 
        }
    }

    // actually insert the target into the insPos.
    int numToMove = pos - insPos ; 
    memmove(&A[insPos+1], &A[insPos], sizeof(int)*numToMove) ; 
    A[insPos] = target ;
    
    // determine the flip actions
    insertFlip(flips, numFlip, insPos) ;
    // flips[*numFlip] = insPos ; *numFlip += 1 ; 
    insertFlip(flips, numFlip, pos) ; 
    // flips[*numFlip] = pos ; *numFlip += 1 ;
    insertFlip(flips, numFlip, pos+1) ;
    // flips[*numFlip] = pos+1 ; *numFlip += 1 ;
    insertFlip(flips, numFlip, insPos+1) ; 
    // flips[*numFlip] = insPos+1 ; *numFlip += 1 ; 

    return ; 
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int * pancakeSort(int * A, int ASize, int *returnSize)
{
    int * flips = NULL ; 
    if (ASize == 1) 
    {
        *returnSize = 0 ;
        return flips ; 
    }
    flips = (int *)malloc(sizeof(int)*ASize*5) ; 

    int i ;
    for (i=1 ; i < ASize ; i++) 
    {
        int last = A[i-1] ; 
        int cur = A[i];
        if (cur < last) {
            Move(A,i, flips, returnSize) ;  
        }
    }
    return flips ; 
}

int test(void)
{
    int A[] = {3,2,4,1,10, 9} ; 
    // int A[] = {1,2,5,7,3} ; 
    int ASize = 6 ; 
    int * B = (int *)malloc(sizeof(int)*ASize) ; 
    memcpy(B, A, sizeof(int)*ASize) ; 
    int size = 0 ;
    int *flips = pancakeSort(A, ASize, &size) ; 
    int i ;
    printf("Original:\n") ; 
    printArray(B, ASize); 
    printf("\n") ; 
    for (i=0 ; i < size ; i++) {
        printf("flip[%d]=%d\n", i+1, flips[i]) ; 
        flip(B, flips[i]) ; 
        printArray(B, ASize) ; 
        printf("\n") ; 
    }

    free(flips) ;
    free(B) ; 
    return 0 ;
}

int main(void)
{
    test() ;
    return 0 ;
}
