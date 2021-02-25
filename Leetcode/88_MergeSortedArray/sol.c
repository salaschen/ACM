/**
 * Problem: Merge Sorted Array - Leetcode Easy
 * Author: Ruowei Chen
 * Date: 25/Feb/2021
 */

#include <stdio.h>
#include <math.h>
#include <string.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    // move the elements in nums1 backwards n position
    void * newPos = (void *) ((char *)nums1 + sizeof(int) * n) ;
    memmove(newPos, nums1, sizeof(int)*m) ;

    int i = 0 ; 
    int j = 0 ; 
    int *num1Ptr = (int *) ((char *)nums1 + (sizeof(int) * n)) ;
    int *num2Ptr = nums2 ; 
    int *curPtr = nums1 ;
    while (i < m && j < n) {
        int num1 = *num1Ptr ;
        int num2 = *num2Ptr ; 
        // printf("num1=%d,num2=%d\n", num1, num2) ; // debug
        if (num1 < num2) {
            *curPtr = num1 ;
            num1Ptr = (int *) ((char *)num1Ptr + sizeof(int)) ; 
            i += 1 ;
        }
        else {
            *curPtr = num2 ;
            num2Ptr = (int *) ((char *)num2Ptr + sizeof(int)) ;
            j += 1 ; 
        }
        curPtr = (int *) ((char *) curPtr + sizeof(int)) ;
    }

    if (j == n) {
        // do nothing
    }
    else if (i == m) {
        // copy what ever is left in nums2 to the nums1
        memcpy(curPtr, num2Ptr, sizeof(int)*(n-j)) ;
    }
}

void print(int * array, int size) {
    for (int i = 0 ; i < size ; i++) {
        if (i > 0 && i % 20 == 0)
            printf("\n") ; 
        printf("%d,", array[i]) ;
    }
    printf("\n") ;
}
// debug program
int main(void)
{
    int m = 5 ; 
    int n = 5 ; 
    int nums1[10] = { 1, 3, 5, 7, 9} ;
    int nums2[5] = {20,40,60,80,100} ;
    print(nums1, 5) ; 
    print(nums2, 5) ; 

    merge(nums1, m, m, nums2, n, n) ;
    print(nums1, 10) ; 
    return 0 ; 
}

