/**
 * Prob: Self-Assembly, ACM/ICPC World Finals 2013, UVa 1572
 * Date: 03/Jan/2018
 * Note: Time limit for python solution, this is the c solution.
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

#define MAXN 53
#define UNMARK 0
#define TEMP 1
#define PERMANENT 2
#define TRUE 1
#define FALSE 0

int edges[MAXN][MAXN] ; 
int marks[MAXN] ; 
int colors[MAXN] ;

int getIndex(char * mark)
{
    assert(mark) ;
    int main = (mark[0] - 'A')*2 ;
    if (mark[1] == '-') main += 1 ; 
    return main ; 
}

char * getReversed(char * original, char * result)
{
    assert(original && result) ; 
    result[0] = original[0] ;
    result[1] = original[1]=='+'? '-' : '+' ; 
    return result ;
}

void parseEdges(char * temp)
{   
    int i, j ; 
    for (i=0 ; i < 4 ; i++) {
        char head[2] ; 
        memcpy(head, temp+(i*2), 2*sizeof(char)) ; 
        if (head[0] == '0') continue ; 
        marks[getIndex(head)] = 1 ;
        int s = getIndex(getReversed(head, head)) ;
        for (j=0 ; j < 4 ; j++) {
            if (i == j) continue ; 
            char tail[2] ; 
            memcpy(tail, temp+(j*2), 2*sizeof(char)) ; 
            if (tail[0] == '0') continue ; 
            int t = getIndex(tail) ; 
            edges[s][t] = 1 ; // mark the edge
        }
    }
}

void printEdges(void)
{
    int i,j ; 
    for (i=0 ; i < 52 ; i++) {
        if (marks[i] == 0) continue ; 
        char head[2] ;
        head[0] = i/2+'A' ; 
        head[1] = i%2==0? '+' : '-' ; 
        printf("[%d]%c%c: ", i, head[0], head[1]) ; 
        for (j=0 ; j < 52 ; j++) {
            char tail[2] ;
            tail[0] = j/2+'A' ; 
            tail[1] = j%2==0? '+' : '-' ;
            if (edges[i][j] == 1) {
                printf("%c%c ", tail[0], tail[1]) ; 
            }
        }
        printf("\n") ;
    }
}

int readInput(void)
{
    int numTypes = 0 ; 
    if (scanf("%d\n", &numTypes) == EOF)
        return 1 ; 
    int i = 0 ; 
    char temp[9] ;
    for (i=0 ; i < numTypes ; i++) {
        scanf("%s", temp) ; 
        // printf("%s\n", temp) ; // debug
        parseEdges(temp) ; 
    }
    // printEdges() ; // debug
    // printf("readinput finished\n") ; // debug
    return 0 ;
}


int visit(int mark) {

    if (colors[mark] == PERMANENT)
        return FALSE ; 
    if (colors[mark] == TEMP)
        return TRUE ; 
    colors[mark] = TEMP ; 
    int i ;
    for (i=0 ; i < 52 ; i++) {
        if (edges[mark][i] == 1) {
            if (visit(i) == TRUE)
                return TRUE ;
        }
    }
    colors[mark] = PERMANENT ;
    return FALSE ;
}

int work(void)
{
    memset(edges, 0, sizeof(int)*MAXN*MAXN) ; 
    memset(marks, 0, sizeof(int)*MAXN) ; 
    memset(colors, UNMARK, sizeof(int)*MAXN) ; 

    if (readInput() == 1)
        return 1 ;   
      
    int i ; 
    int unbound = FALSE ; 
    for (i=0 ; i < 52 ; i++) {
        if (marks[i] == 0) continue ; 
        if (visit(i) == TRUE) {
            unbound = TRUE ;
            break ; 
        }
    }

    if (unbound == TRUE) {
        printf("unbounded\n") ; 
    }
    else {
        printf("bounded\n") ; 
    }
    return 0 ; 
}

int main(void)
{
    while (work() == 0) ; 
    return 0 ;
}
