/**
 * Prob: Undraw the Tree, UVa 10562
 * User: Ruowei Chen
 * Date: 31/Dec/2017
 *
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <ctype.h>

char tree[201][201] ; 
int depth ; // depth starts from 1

int readInput(void) 
{

    memset(tree, 0, 201*201) ; 
    int i = 0 ; 
    while (1)
    {
        // read character one-by-one
        char t = getchar() ; 
        if (t == '#') {
            depth = i ; 
            getchar() ; 
            break ; 
        }
        int j = 0 ; 
        while (t != '\n') {
            tree[i][j++] = t ;
            t = getchar() ; 
        }
        tree[i][j] = '\0' ; 
        i++ ; 
    }

    return 0 ;
}

char * readNode(int row, int col)
{
    // row and col starts from 0.
    // The row should always be at the node level,
    // not at '|' or '----' level.
    char name  ; 
    if (isspace(tree[row][col]) || tree[row][col] == '\n' || tree[row][col] == '\0' ||
        tree[row][col] == '-' || tree[row][col] == '|' || tree[row][col] == '#') 
    {
        return NULL ; 
    }
    else 
    {
        name = tree[row][col] ; 
        printf("%c(", name) ; 
        if (row+1 < depth && tree[row+1][col] == '|')
        {
            // the node has child nodes. 
            // First, get the the start and end columns of the child nodes.
            int start = col ; 
            int end = col ; 
            while (start >= 0 && tree[row+2][start] == '-')
                start -= 1 ; 
            while (end < 200 && tree[row+2][end] == '-')
                end += 1 ;
            // loop through all the places.
            int i = start+1 ; 
            for (; i < end ; i++) {
                char * temp = readNode(row+3, i) ;
                free(temp) ; 
            }
        }
    }
    printf(")") ;
    return NULL ;
}


int work(int T)
{
    // printf("Case %d:\n", T) ; // debug
    readInput() ;
    int i ; 
    printf("(") ; 
    for (i=0 ; i < 200 ; i++) 
    {
        if (tree[0][i] != ' ') 
        {
            char * result = readNode(0, i) ; 
            if (result == NULL) {
            }
            else {
                free(result) ;
            }
            break ; 
        }
    }
    printf(")\n") ; 
    return 0 ; 
}

int readNumber(void)
{
    int result = 0 ; 
    char num[201] ; 
    char t = getchar() ; 
    int i = 0;
    while (t != '\n') {
        num[i++] = t ; 
        t = getchar() ;
    }
    num[i] = '\0' ;
    result = atoi(num) ;
    return result ; 
}

int main(void)
{
    int T ; 
    T = readNumber() ;
    // printf("T=%d\n", T) ; // debug

    int i ; 
    for (i=0 ; i < T ; i++) {
        work(i+1) ; 
    }
    return 0 ; 
}
