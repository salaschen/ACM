#include <stdio.h>

int hammingDistance(int x, int y)
{
    int result = 0 ; 
    while (x > 0 || y > 0) {
        if ((x & 1) != (y & 1)) {
            result += 1 ;
        }
        x = x >> 1 ; 
        y = y >> 1 ; 
    }
    return result ; 
}

void printBits(int num)
{
    printf("%d: ", num) ; 
    while (num > 0)
    {
        printf("%d ", num & 1) ; 
        num = num >> 1 ; 
    }
    printf("\n") ;

}

int main(void)
{
    int x = 10 ; 
    int y = 50 ; 
    printBits(x) ; 
    printBits(y) ; 
    int result = hammingDistance(x,y) ; 
    printf("result=%d\n", result) ; 
    return 0 ; 
}
