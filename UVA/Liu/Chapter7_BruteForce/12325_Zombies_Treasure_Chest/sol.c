/**
 * UVa 12325 Zombie's Treasure Chest, Shanghai 2011
 * Date: 26/Dec/2018 (Happy Boxing Day)
 * Author: Ruowei Chen
 * Note 1: fast brute force already solves all the simple cases.
 * Note 2: Use different enumeration methods to solve different cases.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int hasSeen(int modnum)  ;
const int maxnum = 100000 ; 
int seen[maxnum] ; 
int num ;
long long solve(int N, int S1, int V1, int S2, int V2)
{
    // printf("N=%d,S1=%d,V1=%d,S2=%d,V2=%d\n", N,S1,V1,S2,V2) ; // debug
    num = 0 ; 
    long long result = 0 ; 
    int n1 = N/S1 ; 
    result = (long long)n1*V1 ; 
    
    int n2 = (N-n1*S1)/S2 ; 
    result += (long long)n2*V2 ; 
    // printf("n1=%d,n2=%d,result=%lld\n", n1, n2, result) ; // debug
    while (n1 > 0 && (N-n1*S1-n2*S2) > 0) {
        n1 -= 1 ; 
        n2 = (N-n1*S1)/S2 ; 
        int modnum = N-n1*S1-n2*S2 ; 
        if (hasSeen(modnum)) {
            break ; 
        }
        else {
            if (num < maxnum) {
                seen[num++] = modnum ; 
            }
        }
        long long temp = (long long)n1*V1+(long long)n2*V2 ; 
        // printf("n1=%d,n2=%d,temp=%lld\n", n1, n2, temp) ; // debug
        if (temp > result) {
            result = temp ; 
        }
        
    }

    return result ; 
}

int hasSeen(int modnum) 
{
    // return 1 if true, 0 if not.
    int i ; 
    for (i=0 ; i < num ; i++) {
        if (seen[i] == modnum) {
            return 1 ; 
        }
    }
    return 0 ; 
}


// For when both S1 and S2 are small. Then enumerate either
// at most (S2-1) item1 or (S1-1) item2, depend on their values.
long long method1(int N, int S1, int V1, int S2, int V2)
{
    // swap item1 and item2 if S2*V1 > S1*V2
    if ((long long)S2*V1 > (long long)S1*V2) 
    {
        int ts=S1, tv=V1 ; 
        S1=S2 ; V1=V2 ; 
        S2=ts ; V2=tv ;
    }

    // now item1 can only be 0 to S2-1
    long long result = 0 ; 
    int n1 = 0 ; 
    for (n1=0 ; n1 <= S2-1 ; n1++) {
        long long temp = (long long)n1 * V1 ;
        int n2 = (N-(long long)S1*n1)/S2 ; 
        temp += (long long)n2 * V2 ;
        if (temp > result) {
            result = temp ; 
        }
    }
    return result ;
}

// if S1 is quite big, then enumerate item1 from 0 to N/S1.
// or enumerate item2 from 0 to N/S2.
long long method2(int N, int S1, int V1, int S2, int V2)
{
    // swap item 1 and item 2 if S1 < S2.
    if (S1 < S2) {
        int ts = S1, tv=V1 ; 
        S1=S2 ; V1=V2 ;
        S2=ts ; V2=tv ;
    }
    
    // now always enumerate item 1
    long long result = 0 ;
    int n1 = 0 ; 
    // printf("method2: %d loops\n", N/S1+1) ; // debug
    for (n1=0 ; n1 <= N/S1 ; n1++) {
        int n2 = (N-(long long)n1*S1)/S2 ; 
        long long temp = (long long)n1*V1+(long long)n2*V2 ;
        if (temp > result) {
            result = temp ; 
        }
    }
    return result ; 
}

long long solve2(int N, int S1, int V1, int S2, int V2) 
{
    // if both s1 and s2 are small, use method 1.
    // printf("%d %d %d %d %d\n", N, S1, V1, S2, V2) ; // debug
    if ((long long)S1*(long long)S1 < (long long )N 
        && (long long)S2*(long long)S2 < (long long)N) { // potentially overflow bug!
        return method1(N,S1,V1,S2,V2) ; 
    }
    else {
        return method2(N,S1,V1,S2,V2) ; 
    }
}

void work(int Case)
{
    int N,S1,V1,S2,V2 ;
    scanf("%d %d %d %d %d\n", &N, &S1, &V1, &S2, &V2) ; 
    // printf("%d %d %d %d %d\n", N, S1, V1, S2, V2) ; // debug
    
    // use item 1 as the higher value/size ratio item.
    double r1=V1*1.0/S1, r2=V2*1.0/S2 ; 
    if (r1 < r2) {
        int ts=S1,tv=V1 ; 
        S1 = S2 ; V1 = V2 ; 
        S2 = ts ; V2 = tv ; 
    }

    long long result = solve2(N, S1,V1,S2,V2) ; 
    printf("Case #%d: %lld\n", Case, result) ; 
}

int main(void)
{
    int N ; 
    scanf("%d\n", &N) ; 
    int i; 
    for (i=1; i <= N ; i++) {
        work(i) ; 
    }
    return 0 ; 
}
