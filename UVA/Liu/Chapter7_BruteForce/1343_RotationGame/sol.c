/**
 * UVa 1343 The Rotation Game, Shanghai 2004.
 * Use Iterative Deepening.
 * Date: 30/Dec/2018
 * Note: 
 * 1) Test the diff and h function. 
 * 2) Write the move line function and test.
 * 3) write the revert function and test.
 * 4) Write the dfs with depth limit. Set up True and False value 
 * 5) Use dfs interative deepening in the work function.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MIN(a,b) ((a) < (b)? (a) : (b))
#define True 0
#define False 1

const int maxn = 25 ; 
char board[25]; 
const int lines[8][7] = 
{
 {0,2,6,11,15,20,22},   // A 0
 {1,3,8,12,17,21,23},   // B 1
 {10,9,8,7,6,5,4},      // C 2
 {19,18,17,16,15,14,13},// D
 {23,21,17,12,8,3,1},   // E 4
 {22,20,15,11,6,2,0},   // F
 {13,14,15,16,17,18,19},// G
 {4,5,6,7,8,9,10}       // H 7
} ;    

const int converse[8] = 
{
    5, /* A => F */
    4, /* B => E */
    7, /* C => H */
    6, /* D => G */
    1, /* E => B */
    0, /* F => A */
    3, /* G => D */
    2, /* H => C */
} ; 

const int c[8] = {6,7,8,11,12,15,16,17} ;
char ans[1000] ; // string that stores the path

// PROTOTYPES
void test(void) ; 
void moveLine(char * board, int line, char * ans, int depth) ; 
void revert(char * board, int line, char * ans, int depth) ;
void printBoard(char * board)  ;
void printSpace(int num)  ; 
int dfs(char * board, char * ans, int depth, int limit) ; 
int isGoal(char * board)  ;
int h(char * board) ; 

// SUB ROUTINES
int readInput(void)
{
    int i ;
    for (i=0 ; i <= 23 ; i++) {
        int temp ; 
        scanf("%d", &temp) ; 
        if (temp == 0) {
            return 1 ; 
        }
        else {
            board[i] = temp + '0' ;
        }
    }
    scanf("\n") ; 
    return 0 ;
}
// how many steps away for a board to have all the nums in the centre
int diff(char * board, int num) 
{
    int result = 0 ; 
    int i ; 
    char target = num + '0' ;
    for (i=0 ; i < 8 ; i++) {
        if (board[c[i]] != target) {
            result += 1 ; 
        }
    }
    return result ; 
}

// the heuristic function of the board
int h(char * board)
{
    return MIN(diff(board, 1), MIN(diff(board, 2), diff(board, 3))) ; 
}

// return True if goal, False otherwise
int isGoal(char * board) 
{
    if (h(board) == 0) {
        return True; 
    }
    else {
        return False;
    }
}

// Move the nth line in the board. 0->A, 1->B, ... , 7->H.
// record the move in the ans to form the path.
// the depth starts from 0.
void moveLine(char * board, int line, char * ans, int depth) 
{
    const int * config = lines[line] ;
    char temp = board[config[0]] ; 
    int rowSize = 7 ; 
    int i ; 
    for (i=0 ; i < rowSize ; i++) {
        if (i == rowSize-1) {
            board[config[i]] = temp ; 
        }
        else {
            board[config[i]] = board[config[i+1]] ; 
        }
    }
    char move = 'A'+line ; 
    ans[depth] = move ; 
}

// revert the move line action.
void revert(char * board, int line, char * ans, int depth)
{
    moveLine(board, converse[line], ans, depth) ; 
    ans[depth] = '\0' ; 
}

// Return True of False
int dfs(char * board, char * ans, int depth, int limit) 
{
    // If it's a goal state, just return.
    if (isGoal(board) == True) {
        return True ; 
    }
    
    // If the expected distance is larger than the limit
    // return False
    if (h(board) + depth > limit) {
        // printf("h=%d, depth=%d, limit=%d\n", h(board), depth, limit) ; // debug
        return False ; 
    }

    // Try all different lines with DFS recursively
    int i ; 
    for (i=0 ; i <= 7 ; i++ ) 
    {
        moveLine(board, i, ans, depth) ; 
        int temp = dfs(board, ans, depth+1, limit) ; 
        if (temp == True) {
            return True ;
        }
        else {
            revert(board, i, ans, depth) ; 
        }
    }

    return False ; 
}

int work() 
{
    memset(board, 0, sizeof(char)*maxn) ; 
    memset(ans, 0, sizeof(char)*1000) ; 
    if (readInput() == 1) {
        return 1 ; 
    }; 
    if (isGoal(board) == True) {
        printf("No moves needed\n") ; 
        printf("%c\n", board[c[0]]) ; 
    }
    else {
        int limit = 1 ; 
        while (1) {
            if (dfs(board, ans, 0, limit) == True) {
                printf("%s\n", ans) ; 
                printf("%c\n", board[c[0]]) ; 
                break ;
            }
            else {
                limit += 1 ; 
            }
        }
    }

    return 0 ;
}

int solve(void)
{
    while (work() == 0) {
        continue ; 
    }
    return 0 ;
}

int main(void)
{
    solve() ; 
    // test() ; 
    return 0 ;
}

// TESTING FUNCTIONS
//
void dfsTest(void) 
{
    memset(ans, 0, sizeof(char)*1000) ; 
    char * board = (char *) malloc(sizeof(char)*25) ; 
    char * original = "111111112222222233333333" ;
    // char * original = "111132323132231222312133";
    memcpy(board, original,sizeof(char)*25) ;
    
    int result = dfs(board,ans,0,4) ; 
    if (result == True) {
        printf("%s\n", ans) ; 
        printf("%c\n", board[c[0]]) ; 
    }
}

void basicTest(void) 
{
    memset(ans, 0, sizeof(char)*1000) ; 
    char * board = (char *) malloc(sizeof(char)*25) ; 
    char * original = "111111112222222233333333" ;
    // char * original = "111132323132231222312133";
    memcpy(board, original,sizeof(char)*25) ;
    printBoard(board) ; 
    
    moveLine(board, 3, ans, 1) ; // D
    printBoard(board) ; 
    moveLine(board, 3, ans, 2) ; // D
    printBoard(board) ; 
    moveLine(board, 7, ans, 3) ; // H
    printBoard(board) ;
    moveLine(board, 7, ans, 4) ; // H
    printBoard(board) ; 
    printf("ans: %s\n", ans) ; 

    printf("Begin reverting...\n") ; 
    revert(board, 7, ans, 4) ; 
    printBoard(board) ;
    revert(board, 7, ans, 3) ; 
    printBoard(board) ;
    revert(board, 3, ans, 2) ; 
    printBoard(board) ;
    revert(board, 3, ans, 1) ; 
    printBoard(board) ;
    printf("ans: %s\n", ans) ; 

}

void test(void)
{
    dfsTest() ;   
}

void printSpace(int num) 
{
    if (num <= 0) return ; 
    int i = 0 ; 
    for (; i < num ; i++) {
        putchar(' ') ; 
    }
}

// debug: print out the board
void printBoard(char * board) 
{
    printSpace(4) ;
    printf("A B\n") ;    
    int lineStart[7] = {0,2,4,11,13,20,22} ;
    int row = 0 ; 
    for (row = 0 ; row < 7 ; row ++) {
        if (row != 2 && row != 4) {
            printSpace(4) ; 
            printf("%c %c\n", board[lineStart[row]], board[lineStart[row]+1]) ; 
        }
        else {
            if (row == 2) {
                printf("H ") ; 
            }
            else {
                printf("G ") ; 
            }
            int i ; 
            for (i=0 ; i < 7 ; i++) {
                printf("%c", board[lineStart[row]+i]) ; 
            }
            if (row == 2) {
                printf(" C\n") ; 
            }
            else {
                printf(" D\n") ; 
            }
        }
    }
    printSpace(4) ;
    printf("F E\n") ;    
    printf("h=%d, diff(1)=%d, diff(2)=%d, diff(3)=%d, isGoal=%s\n",
            h(board), diff(board, 1), diff(board, 2), diff(board, 3), 
            isGoal(board)==0? "yes":"no") ; 
    printf("\n") ; 
}


