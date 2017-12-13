#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int m, n ; 
char edges[101][101] ; 
int state[101] ; // 0 as not touched, -1 as being searched, 1 as search completed.
int top[101] ; 
int t;

int readInput(void)
{
    scanf("%d %d\n", &n, &m) ; 
    if (n == 0 && m == 0)
        return 1 ; 
    int i ; 
    for (i=0 ; i < m ; i++) {
        int a, b ;
        scanf("%d %d\n", &a, &b) ; 
        edges[a][b] = 1 ; 
    }
    return 0 ; 
}

int dfs(int v)
{
    // return 0 if OK, 1 if loop exists.
    int i ; 
    if (state[v] == 1)
        return 0 ; 
    // printf("searching %d\n", v) ; // debug

    state[v] = -1 ; // being searched
    for (i=1 ; i <= n ; i++) {
        if (edges[v][i] == 1) {
            if (state[i] == -1) {
                return 1 ; // loop
            }
            else if (state[i] == 0) {
                dfs(i) ; 
            }
        }
    }
    state[v] = 1 ; // searched finished.
    top[t] = v ; 
    // printf("top[%d]=%d\n", t, v) ; // debug
    t -- ; 
    return 0 ;
}

int work(void)
{
    memset(edges, 0, 101*101*sizeof(char)) ; 
    memset(state, 0, 101*sizeof(int)) ; 
    if (readInput() ==1)
        return 1 ; 
    
    t = n-1 ; 
    int i ; 
    for (i=1 ; i<=n ;i++) {
        dfs(i) ; 
    }
    printf("%d", top[0]) ; 
    for (i=1 ; i < n ; i++) {
        printf(" %d", top[i]) ; 
    }
    printf("\n") ; 
    return 0 ;
}

int main(void)
{
    while (work() == 0)
        ;
    return 0 ; 
}
