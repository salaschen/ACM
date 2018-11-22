#include <stdio.h>
int work(int k)
{
    int x, y ;
    int num = 0 ; 
    
    int xlist[10001], ylist[10001] ; 

    for (y = k+1 ; y <= 2*k ; y++) {
        if (((k*y) % (y-k)) == 0) {
            x = k*y/(y-k) ; 
            ylist[num] = y ; 
            xlist[num] = x ; 
            num ++ ;
               
        }
    }

    int i =0 ; 
    printf("%d\n", num) ; 
    for (i=0 ; i < num ; i++) {
        printf("1/%d = 1/%d + 1/%d\n", k, xlist[i], ylist[i]) ; 
    }

    return 0 ;
}
int main(void)
{
    int k ; 
    while (1) 
    {
        if (scanf("%d\n", &k) == EOF) {
            break ;
        }
        else {
            work(k) ; 
        }
    }
    return 0 ; 
}
