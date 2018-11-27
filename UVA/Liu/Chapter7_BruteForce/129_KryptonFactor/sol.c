/**
 * UVa 129 - Krypton Factor
 * Brute Force
 * Date: 27/Nov/2018
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE 1
#define FALSE 0
int IsHard(char * str, int len) ;
int count = 0 ; 

void search(char * buf, int level,int n, int L)
{
    int i ; 
    for (i=0 ; i < L ; i++) {
        buf[level] = 'A' + i ; 
        if (IsHard(buf, level+1) == TRUE) {
            count ++ ; 
            if (count == n) return ; 
            search(buf, level+1, n, L) ; 
            if (count == n) return ; 
        }
    }
    buf[level] = '\0' ;
    return ;
}

void printBuf(char * buf, int len)
{
    int i; 
    for (i=0; i < len ; i++) {
        if (i != 0 && i % 64 == 0) {
            printf("\n") ; 
        }
        else if (i > 0 && i % 4 == 0) {
            printf(" ") ; 
        }
        printf("%c", buf[i]) ; 
    }
    printf("\n") ;
}

int work(int n, int L)
{
    char buf[90]  ;
    memset(buf, 0, 90*sizeof(char)) ;
    // buf[0] = 'A' ;
    count = 0 ; 
    search(buf, 0, n, L) ; 
    
    // print out the buf
    int len = strlen(buf) ; 
    // printf("buf:%s\n", buf) ; 
    printBuf(buf, len) ; 
    printf("%d\n", len) ; 
    
    return 0 ; 
}

int IsHard(char * str, int len)
{
    if (len == 0) return FALSE ; 
    int start = len-1 ; 
    while (start >= (len-start)) {
        int cmpLen = len-start ; 
        char * second = &str[start] ;
        char * first = (char *)(second - sizeof(char)*cmpLen) ;
        if (strncmp(first, second, cmpLen) == 0)
            return FALSE ; 
        start -- ; 
    }
    return TRUE ;
}

int main(void)
{
    int n, L ;
    while (1) {
        scanf("%d %d\n", &n, &L) ; 
        if (n == 0 && L == 0) {
            break ; 
        }
        else {
            work(n, L) ; 
        }
    }

    return 0; 
}
