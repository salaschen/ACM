/**
 * Author: Ruowei Chen
 * Date: 21/Jun/2019
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int intCmp(const void *i1, const void *i2) {
    return *(int *)i1 - *(int *)i2 ;
}

int getLast(int *num, int start, int numsSize, int target) ;

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* searchRange(int* nums, int numsSize, int target, int* returnSize)
{
    int * result = (int *)malloc(sizeof(int)*2) ;

    int * posPtr = bsearch(&target, nums, numsSize, sizeof(int), intCmp) ;
    if (posPtr == NULL) {
        result[0] = -1 ;
        result[1] = -1 ;
        return result ;
    }

    int pos = ((char *)posPtr - (char *)nums) / sizeof(int) ;
    while ((pos-1) >= 0 && nums[pos-1] == target) {
        pos -= 1 ; 
    }
    int last = getLast(nums, pos, numsSize, target) ;
    result[0] = pos ;
    result[1] = last ;
    return result ;
}

int getLast(int *num, int start, int numsSize, int target) 
{
    // start is 0-indexed.
    int up = numsSize - 1 ; 
    int low = start ; 
    
    while (up > (low+1)) {
        int mid = (up+low)/2 ; 
        if (num[mid] == target && num[mid+1] < target) {
            return mid ;
        }
        if (num[mid] > target) {
            up = mid ; 
        }
        else {
            low = mid ; 
        }
    }
    
    if (num[low] > target) {
        return start ; 
    }
    if (num[up] == target) {
        return up ; 
    }
    if (num[low] != target) {
        return start ; 
    }
    else {
        return low ; 
    }
}

// test function
int main(void)
{
    int nums[6] = {5,7,7,8,8,10} ; 
    int size = 6 ; 
    int target = 8 ; 
    int returnSize = 2 ; 

    int * result = searchRange(nums, size, target, &returnSize) ; 
    printf("[%d,%d]\n", result[0], result[1]) ; 
    free(result) ; 

    target = 6 ; 
    result = searchRange(nums, size, target, &returnSize) ; 
    printf("[%d,%d]\n", result[0], result[1]) ; 
    free(result) ; 
    
    target = 2 ; 
    nums[0] = 2 ; nums[1] = 2 ;
    result = searchRange(nums, 2, target, &returnSize) ; 
    printf("[%d,%d]\n", result[0], result[1]) ; 

    return 0;  
}
