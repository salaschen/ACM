#include <string.h>
#include <stdio.h>

void moveZeroes(int *nums, int numsSize)
{
    if (numsSize == 0) return ; 
    int * tail = &(nums[numsSize-1]); 
    int * head ; 
    while (*tail == 0) {
        if (tail == nums) return ; 
        tail -= 1 ; 
    }
    head = tail ; 
    while (1)
    {
        if (*head != 0) {
            if (head == nums) break; 
            head -= 1 ; 
        }
        else {
            // We encounter a zero.
            int length = ((char *)tail-(char*)head)/sizeof(int) + 1 ; 
            void * dest = (void *)(head) ;
            void * src = (void *)(head+1) ; 
            memmove(dest, src, length*sizeof(int)) ;
            *tail = 0 ; 

            if (head == nums) 
                break ;

            head -= 1 ; 
            tail -= 1 ; 
        }
    }

}

void PrintArray(int *nums, int numsSize)
{
    int i ;
    for (i=0 ; i < numsSize ; i++) {
        printf("%d ", nums[i]) ; 
    }
    printf("\n") ;
}

int main(void)
{
    const int numSize = 5 ; 
    int nums[numSize] = {0,1,0,3,12} ; 
    PrintArray(nums, numSize) ; 
    
    moveZeroes(nums, numSize) ;
    PrintArray(nums, numSize) ;
    return 0 ; 
}
