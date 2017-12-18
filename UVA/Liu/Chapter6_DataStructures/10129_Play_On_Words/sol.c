/**
 * Prob: UVA 10129 Play On Words
 * Date: 18/Dec/2017
 * Note: Treat character as a node, a word as an edge. Generate a directed map
 * from input and determine if an Euler path (or Euler cycle) can be formed.
 * The property of an Euler path(cycle) can be seen on Wikipedia.
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int N ;
int d[26][26] ;
int u[26][26] ; 
int in[26] ; 
int out[26] ;

int readInput(void)
{
    scanf("%d\n", &N) ; 
    int i ; 
    memset(d, 0, 26*26*sizeof(int)) ; 
    memset(u, 0, 26*26*sizeof(int)) ; 
    memset(in, 0, 26*sizeof(int)) ; 
    memset(out, 0, 26*sizeof(int)) ;

    for (i=0 ; i < N ; i++) {
        char buf[1001] ;    
        scanf("%s\n", buf) ; 
        // printf("%s\n", buf) ; // debug
        int head = buf[0] - 'a' ; 
        int tail = buf[strlen(buf)-1] - 'a' ; 
        d[head][tail] = 1 ;
        u[head][tail] = 1 ; u[tail][head] = 1 ;
        in[tail] += 1 ; 
        out[head] += 1 ; 
    } 
    // debug
    /**
    for (i=0 ; i < 26 ; i++) {
        printf("in[%c]=%d, out[%c]=%d\n", 
                i+'a', in[i], i+'a', out[i]) ;
    }
    */

    return 0 ; 
}

int getOdd(int * neg, int *pos)
{
    int i = 0 ; 
    int result = 0 ; 
    for (i=0 ; i < 26 ; i++) {
        if (in[i] != out[i]) {
            result += 1 ;
            if (in[i] == out[i]+1) {
                *pos += 1 ; 
            }
            else if (out[i] == in[i] + 1) {
                *neg += 1 ; 
            }
            else {
                return 100 ; // fail
            }
        }
    }
    return result ; 
}

int hasCorrectDegree(void)
{
    int neg = 0 ; int pos = 0 ; 
    int numOdd = getOdd(&neg, &pos) ; // in degree not equal to out degree
    if (numOdd == 0) {
        return 0 ; 
    }
    else if (numOdd == 1 || numOdd > 2)
        return 1 ;

    // when numOdd == 2, make sure one has positive and
    // the other has negative (in - out)
    if (neg != pos)
        return 1 ;

    // the neg need to have one more out than in
    // and vice versa for the pos


    return 0 ; 
}


int bfs(int node, int id, int * searched, int * ids)
{
    searched[node] = 1 ; 
    ids[node] = id ;
    int i ; 
    for (i=0 ; i < 26 ;i ++) {
        if (u[node][i] && searched[i] == 0) {
            ids[i] = id ; 
            searched[i] = 1 ; 
            bfs(i, id, searched, ids) ; 
        }
    }
    return 0 ; 
}

int allConnected(void)
{
    int id = 1 ; 
    int ids[26] ; 
    memset(ids, 0, 26*sizeof(int)) ; 
    int i = 0 ; 
    int searched[26] ; 
    memset(searched, 0, 26*sizeof(int)) ; 
    for (i=0 ; i < 26 ; i++) {
        if (in[i] != 0 || out[i] != 0) {
            bfs(i, id, searched, ids) ; 
            break ; 
        }
    }
    for (i=0 ; i < 26 ; i++) {
        if (in[i] != 0 || out[i] != 0) {
            if (ids[i] != id) {
                // printf("node %c is not connected\n", i+'a') ; 
                return 1 ; 
            }
        }
    }
    return 0 ; 
}

int isEuler(void)
{
    int degree = hasCorrectDegree() ; 
    int connected = allConnected() ; 
    // printf("degree=%d, connected=%d\n", degree, connected) ; // debug
    
    return (degree == 0 && connected == 0)? 0: 1 ; 
}

int work(void)
{
    readInput() ; 
    if (isEuler() == 0)
    {
        printf("Ordering is possible.\n") ;
    }
    else {
        printf("The door cannot be opened.\n") ; 
    }
    return 0 ;
}

int main(void)
{
    int T ; 
    scanf("%d\n", &T) ; 
    int i ; 
    for (i=0 ; i < T ; i++) {
        work();  
    }
    return 0 ;
}
