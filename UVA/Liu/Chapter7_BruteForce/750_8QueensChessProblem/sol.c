/**
 * UVa 750 - 8 Queens Chess Problem
 * Date: 23/Nov/2018
 * Author: Ruowei Chen
 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
int search(int board[9], int curLevel, int reservedCol, int reservedRow) ;
int IsBoardValid(int board[9]) ;
void PrintHeading() ;

int num ; // number of solution
int work(int Case)
{
    if (Case > 1) {
        printf("\n") ;
    }
    int r,c  ;
    num = 0 ; 
    scanf("\n%d %d\n", &r,&c) ; 
    int board[9] ; 
    memset(board, 0, sizeof(int)*9) ;
    board[c] = r ; 
    
    PrintHeading() ; 
    search(board, 1, c, r) ; 
    
    return 0 ;
}

void PrintHeading()
{
    printf("SOLN       COLUMN\n") ; 
    printf(" #      1 2 3 4 5 6 7 8\n\n") ; 
}

// debug only
void printBoard(int board[9])
{
    int i ; 
    for (i=1 ; i <= 8 ; i ++) {
        printf(" %d", board[i]) ; 
    }
    printf("\n") ;
}

int search(int board[9], int curLevel, int reservedCol, int reservedRow)
{
    if (curLevel == 9) {
        if (IsBoardValid(board) == FALSE) {
            return 0;
        }

        // print out solution
        num ++ ; 
        printf("%2d     ", num) ; 
        int i ; 
        for (i=1 ; i <= 8 ; i++) {
            printf(" %d", board[i]) ; 
        }
        printf("\n") ; 
        return 0 ; 
    }
    else if (curLevel == reservedCol)
    {
        board[curLevel] = reservedRow ; 
        search(board, curLevel+1, reservedCol, reservedRow) ; 
    }
    else {
        int i = 1 ; 
        for (i=1 ; i <= 8 ; i++) {
            if (i == reservedRow) continue ; 
            int j = 1 ; 
            int before = FALSE ;
            for (j=1 ; j < curLevel ; j++) {
                if (board[j] == i) {
                    before = TRUE ; 
                    break ;
                }
            }
            if (before == TRUE) continue ; 

            board[curLevel] = i ; 
            if (IsBoardValid(board) == TRUE)
                search(board, curLevel+1, reservedCol, reservedRow) ; 
            else {
                // printf("curLevel=%d:", curLevel) ; // debug
                // printBoard(board) ; // debug
            }
        }
    }
    
    board[curLevel] = 0 ; // reset before return 
    return 0 ;
}

int IsBoardValid(int board[9])
{    
    int i = 0 ; 
    int j = 0 ; 
    // Check the diagonal attack
    for (i=1 ; i <= 8 ; i ++) {
        int ri = board[i] ; 
        int ci = i ; 
        for (j=i+1 ; j <= 8 ; j++) {
            int rj = board[j] ;
            int cj = j ;
            if (rj == 0 || ri == 0) continue ;
            if (ri-rj == ci-cj || ri-rj == cj-ci) {
                // printf("ri=%d,rj=%d,ci=%d,cj=%d\n", ri,rj,ci,cj) ; // debug
                return FALSE ;
            }
        }
    }
    return TRUE ; 
}

void TestIsBoardValid()
{
    int board[9] = {0,2,0,1,0,0,0,0,0} ;
    int result = IsBoardValid(board) ; 
    printf("result=%d\n", result) ; // debug   

}
int mainFunc(void) ;

int main(void)
{
    mainFunc(); 
    // TestIsBoardValid() ;
    return 0 ;
}

int mainFunc(void)
{
    int N ; 
    scanf("%d\n", &N) ; 
    int i ; 
    for (i=0 ; i < N ; i++) {
        work(i+1) ; 
    }
    return 0 ;
}
