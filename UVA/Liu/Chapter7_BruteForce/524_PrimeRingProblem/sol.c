/**
 * UVa 524 Prime Ring Problem
 * Backtracking
 * Date: 26/Nov/2018
 * Author: Ruowei Chen
 * Note: Try to get a better run time/rank than Python.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE 0
#define FALSE 1

int oddCand[] = {3,5,7,9,11,13,15} ;
int evenCand[] = {2,4,6,8,10,12,14,16} ;
int primes[] = {2,3,5,7,11,13,17,19, 23,29,31,37,41} ;
int numPrimes = 13 ;

int count = 0 ;
char ** buf ; 

int IsPrime(int num) ; 
int search(int *lst, int level, int N) ;
int work(int Case, int N) ;

/**
 *   sub-routines
 *
 */
int search(int *lst, int level, int N)
{
    if (level == N) {
        if (IsPrime(lst[level-1]+1) == TRUE)
        {
            char * front = (char *)malloc(sizeof(char)*(N+1)) ; 
            int i ;
            for (i=0 ; i < N ; i++) {
                front[i] = 'A' + (lst[i]-1) ;
            }
            front[N] = '\0' ;
            buf[count++] = front ; 
        }
    }
    else {
        int * cand ; 
        int limit = N/2 ; 
        if (level % 2 == 1) {
            cand = evenCand ; 
        }
        else {
            cand = oddCand ;
            limit -=1 ;
        }
        int i ; 
        for (i=0 ; i < limit ; i++) {
            int j;  
            int ok = TRUE ; 
            for (j=0 ; j < level;  j++) {
                if (lst[j] == cand[i])  {
                    ok = FALSE ; 
                    break ; 
                }
            }
            if (ok == TRUE && IsPrime(cand[i] + lst[level-1]) == TRUE)
            {
                lst[level] = cand[i] ; 
                search(lst, level+1, N) ; 
            }
            /*
            printf("level=%d, cand=%d, prev=%d, IsPrime=%d\n", 
                    level, cand[i], lst[level-1],
                    IsPrime(cand[i]+lst[level-1])) ; // debug
            */
        }
        lst[level] = 0 ; 
    }
    return 0 ; 
}

int StrCmp(const void *s1, const void *s2) {
    const char * ss1 = (char *)s1 ;
    const char * ss2 = (char *)s2 ; 

    int i = 0 ;
    for (; ss1[i] != '\0' && ss2[i] != '\0' ; i++) {
        if (ss1[i] > ss2[i])
            return 1; 
        if (ss1[i] < ss2[i])
            return -1 ; 
    }
    return 0 ;
}

void PrintString(char * str)
{
    int i = 1 ; 
    printf("%d", str[0]-'A'+1) ;
    for (; str[i] != '\0' ; i++) {
        printf(" %d", str[i]-'A'+1) ;
    }
    printf("\n") ; 
}

int work(int Case, int N)
{
    int *lst = (int *)malloc(sizeof(int)*N) ; 
    memset(lst, 0, sizeof(int)*N) ;
    lst[0] = 1 ; 
    count = 0 ; 
    
    search(lst, 1, N) ;   

    // qsort doesn't work for some reason.
    // qsort(buf, count, sizeof(char *), StrCmp) ; 

    int i = 0 ; 
    if (Case > 1) {
        printf("\n") ; 
    }
    printf("Case %d:\n", Case) ; 
    for (; i < count ; i++) {
        // printf("%s\n", buf[i]) ;  // debug
        PrintString(buf[i]) ;
    }

    {
        int i = 0 ; 
        for (; i < count ; i++) {
            free(buf[i]) ; 
        }
    }

    return 0 ;
}


int IsPrime(int num)
{
    int i = 0 ; 
    for (; i < numPrimes ; i++) {
        if (primes[i] == num)
            return TRUE ; 
    }
    return FALSE ; 
}

int main(void)
{
    int N ; 
    int Case = 1 ;
    buf = (char **)malloc(sizeof(char *)*100000) ; 

    while (1) {
        if (scanf("%d\n", &N) == EOF) {
            break ;
        }
        else {
            work(Case, N) ; 
            Case ++ ; 
        }
    }
    free(buf) ; 
    return 0 ;
}

