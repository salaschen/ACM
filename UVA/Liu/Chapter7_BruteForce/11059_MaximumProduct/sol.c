#include <stdio.h>
#include <stdlib.h>

int S[18] ;

int work(int Case, int N)
{
    int i ; 
    for (i=0 ; i < N ; i++) {
        scanf("%d", &S[i]); 
    }
    scanf("\n") ; 
    
    long long result = 0 ; 
    int j ; 
    for (i=0 ; i < N ; i++) {
        long long temp = S[i] ;
        result = (temp > result)? temp : result ; 
        for (j=i+1; j < N ; j++) {
            temp = temp * S[j] ; 
            result = (temp > result)? temp : result ; 
        }
    }
    printf("Case #%d: The maximum product is %lld.\n\n", Case, result) ; 
    return 0 ;
}


int main(void)
{
    int N ; 
    int Case = 1 ; 
    while (1) {
        if (scanf("%d\n", &N) == EOF) {
            break ; 
        }
        else {
            work(Case, N) ; 
            Case ++ ;
        }
    }
    return 0 ;
}
