/**
 * Prob: 639 - Decode Ways II (Hard)
 * Date: 10/Mar/2019
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int modNum = (1000000000) + 7 ; 
#define MAXLEN 100100
long long mem[MAXLEN] ; 

// return a number if valid, 0 not valid.
// s is guaranteed to be NULL terminated string
// the return number is the possible representation.
int isValid(char * s) 
{
    /**
    if (s[0] == '*' && s[1] == '*') {
        return 15 ;
    }
    */

    if (s[0] == '*')  {
        char temp[3] = {'1', s[1], '\0'} ; 
        int result = isValid(temp) ; 
        temp[0] = '2' ;
        result += isValid(temp) ; 
        return  result; 
    }
    if (s[0] == '1') {
        if (s[1] == '*') return 9 ; 
        else return 1 ; 
    }
    else if (s[0] == '2') {
        if (s[1] == '*') return 6 ; 
        else if (atoi(&s[1]) <= 6) {
            return 1 ; 
        }
        else return 0 ;
    }
    return 0 ; 
}

// Return the number of representation that a single character can decode into.
int singleRep(char * s)
{
    if (s[0] == '*') return 9 ; 
    if (s[0] == '0') return 0 ;
    else return 1 ; 
}

// helper function
// does the same thing of numDecodings
// just with string length provided
// so it's easier to make recursive calls.
// Note: Stack overflow for really large case.
long long helper(char *s, int len) 
{
    if (len <= 0) return 1 ; 

    if (mem[len] != 0) return mem[len] ; 

    // considering the first letter
    long long result = 0 ; 
    if (s[0] == '0') { // invalid
        return 0 ; 
    }
    else if (s[0] == '*') {
        result = (9 * helper(&s[1], len-1))  ; 
    }
    else { // '1' - '9'
        result = (1 * helper(&s[1], len-1))  ; 
    }

    mem[len] = result % modNum; 
    if (len == 1) return result % modNum ; 

    // now consier the first two letters
    char num[3] = {s[0], s[1], '\0'} ; 
    int base = isValid(num) ; 
    if (base > 0) {
        result = (result + base * helper(&s[2], len-2)) ;
    }
    mem[len] = result % modNum; 


    printf("old: len=%d, result=%lld\n", len, result % modNum) ; // debug
    return result % modNum; 
}

// Iterative version of the helper to avoid the stack overflow 
// problem.
long long helperIter(char *s, int len) 
{
    if (len == 0) return 0 ; 
    if (len == 1) return singleRep(s) ; 

    // Solve for the last character   
    mem[len] = singleRep(&s[len-1]) ; 

    // Solve for the second last character
    mem[len-1] = singleRep(&s[len-2]) * mem[len] + isValid(&s[len-2]) ; 

    // Solve for the rest.
    int i ; 
    for (i=len-2 ; i >= 1 ; i--) {
        long long temp = singleRep(&s[i-1]) * mem[i+1] ; 
        char c[3] = {s[i-1], s[i], '\0'} ;
        temp = temp + ((isValid(c)*mem[i+2]) % modNum) ;
        mem[i] = temp % modNum ;
    }

    return mem[1] % modNum; 
}

int numDecodings(char * s)
{
    memset(mem, 0, sizeof(long long)*MAXLEN) ; 
    // return (int)helper(s, strlen(s)) ; 
    return (int)helperIter(s, strlen(s)) ; 
}

int main(void)
{
    FILE *fin = stdin ; 
    
    char * temp = (char *)malloc(sizeof(char)*100100) ; 
    while (fscanf(fin, "%s", temp) != EOF) {
        memset(mem, 0, sizeof(long long)*MAXLEN) ; 
        //int old = helper(temp, strlen(temp)) ; 
        // printf("Input:%s\n", temp) ; // debug
        printf("Input length:%lu\n", strlen(temp)) ; // debug
        printf("Input: %s\nOutput: %d\n",temp, numDecodings(temp)) ; 
        // printf("Old:    %d\n",old) ; 
        printf("\n") ; 
    }
    return 0 ;
}
