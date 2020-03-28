// Leetcode 43 Multiply Strings - Medium

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void posMultiply(char * num1, int len1, char digit, char * result, int base)  ;

char * multiply(char * num1, char * num2) 
{

    int len1 = strlen(num1) ;
    int len2 = strlen(num2) ;
    // printf("len1=%d, len2=%d\n", len1, len2) ;
    if ((len1 == 1 && num1[0] == '0') || (len2 == 1 && num2[0] == '0'))
    {
        return "0" ;
    }

    
    char * result = (char *)malloc(sizeof(char)*(len1+len2+1)) ;
    result[len1+len2] = '\0' ;
    

    // initialize the string.
    memset(result, 0, sizeof(char)*(len1+len2)) ;

    int base = len1+len2-1 ; 
    for (int i = len2-1 ; i >= 0 ; i--) {
        posMultiply(num1, len1, num2[i], result, base) ; 
        base -= 1 ;
    }

    // do the left shift if required.
    int leftShift = 0 ; 
    for (int i = 0 ; i <= len1+len2 ; i++) {
        if (result[i] == 0) {
            leftShift ++ ;
        }
        else {
            break ;
        }
    }

    memmove(result, result+sizeof(char)*(leftShift), sizeof(char)*(len1+len2-leftShift)) ;
    result[len1+len2-leftShift] = '\0' ;

    for (int i = 0 ; i < len1+len2-leftShift ; i++) {
        result[i] += '0' ; 
    }

    return result; 
}

// purpose: conduct the multiplication of num1 and digit, and 
// update the result by adding the multiple from the base position.
void posMultiply(char * num1, int len1, char digit, char * result, int base) 
{
    if (digit == 0) {
        return ;
    }
    digit = digit - '0' ;
    int carry = 0 ;
    int temp ; 
    for (int i = len1-1 ; i >= 0 ; i--) {
        int curnd = num1[i] - '0' ; 
        temp = curnd * digit + carry + result[base] ;
        carry = (int)(temp / 10) ; 
        
        result[base] = temp % 10 ;
        // printf("cur=%d, digit=%c, temp=%d, carry=%d\n", curnd, digit, temp, carry) ; // debug
        base -= 1 ;
    }
    if (carry > 0) {
        result[base] += carry ; 
    }
    return ;
}

// test function
int main(void)
{
    // char * num1 = "123451231251353523424121423425346346" ;  
    // char * num2 = "67892834928374721438912492179479817273498719823749" ;
    char * num1 = "0" ;
    char * num2 = "123" ; 
    
    char * result = multiply(num1, num2) ;
    printf("carry out %s*%s\n", num1, num2) ; 
    printf("result=%s\n", result) ; 
    
    return 0 ;
}

