/**
 * UVa 1374 - Power Calculus, ACM/ICPC Yokohama 2006
 * Date: 01/Jan/2019
 * Author: Ruowei Chen
 * Note:
 * 1) IDA*
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define True 0
#define False 1

int ans[100] ;  

// Prototypes
int test(void) ; 
int dfs(int target, int cur, int depth, int limit, int * result)  ;


// SUB ROUTINES
int dfs(int target, int cur, int depth, int limit, int * result) 
{
    /**
    printf("target=%d,cur=%d,depth=%d,limit=%d,result=%d\n",
            target,cur,depth,limit,*result) ; // debug
    */

    if (ans[depth] == target) {
        if (*result == 0 || *result > depth) {
            *result = depth ; 
        }
        return True ; 
    }

    // Branch prunning.
    {
        int curmax = 0; 
        int i ;
        for (i=0 ; i <= depth ; i++) {
            if (ans[i] > curmax) {
                curmax = ans[i] ;
            }
        }
        if ((int)pow(2, limit-depth)*curmax < target) {
            return False ; 
        }
    }
    
    // Next level search
    int i,j,k ; 
    int r = False ; 
    for (i=0 ; i <= depth ; i++) {
        j = depth ; 
        int temp[3] = {ans[i]+ans[j], ans[i]-ans[j], ans[j]-ans[i]} ; 
        for (k=0 ; k < 3 ; k++) {
            if (temp[k] > 0) {
                ans[depth+1] = temp[k] ; 
                if (dfs(target, temp[k], depth+1, limit, result) == True) 
                    r = True ; 
            }
        }
    }
    return r; 
}

int work(void)
{
    memset(ans, 0, sizeof(int)*100) ; 
    ans[0] = 1 ;
    int num ;
    scanf("%d\n", &num) ; 

    if (num == 0) {
        return 1 ; 
    }

    int result = 0 ; 
    int limit = 1 ; 
    while (1)  {
        if (dfs(num, 1, 0, limit, &result) == True) {
            printf("%d\n", result) ; 
            break ; 
        }
        else {
            limit += 1;
        }
    }
    return 0  ; 
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


// Testing function
int test(void) 
{
    printf("%d\n", (int) pow(2, 10)) ; 
    return 0 ;
}
