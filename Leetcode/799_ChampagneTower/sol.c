/**
 * Leetcode: 799 Champagne Tower - Medium
 * Author: Ruowei Chen
 * Date: 30/Mar/2019
 * Note: Brute Force
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Return the last row which is all full after pouring 
// the designated number of wines.
// return -1 if no row is full.
// assuming poured is non-negative.
int lastFullRow(int poured)
{
    if (poured == 0) return -1 ; 
    // get the potential start row.
    int N = (int) sqrt((double)(2*((double)poured))) ; 

    while ((N+N*N)/2 < poured ) {
        N += 1  ;
    }
    if ((N+N*N)/2 > poured) {
        N -= 1 ;
    }
    return N-1 ; // 0-based
}

// return the fraction of a glass of wine that
// a glass at (row,col) gets
double fraction(int row, int col)
{
    double * prev = (double *)malloc(sizeof(double)*(row+1)) ; 
    double * cur = (double *)malloc(sizeof(double)*(row+1)) ;

    memset(prev, 0, sizeof(double)*(row+1)) ; 
    memset(cur, 0, sizeof(double)*(row+1)) ; 
    
    prev[0] = 1.0 ; 
    int i,j ;
    for (i=1 ; i <= row ; i++) {
        cur[0] = pow(0.5, (double)i) ; 
        cur[i] = cur[0] ; 
        for (j=1 ; j < i ; j++) {
            cur[j] = 0.5*(prev[j-1]+prev[j]) ;
        } 
        double * temp = prev; 
        prev = cur ; 
        cur = temp ; 
    }
    
    double result = prev[col] ;

    // free memory at last
    free(prev) ; 
    free(cur) ; 

    return result ; 
}

double excessOfOne(double value)
{
    if (value > 1.0) {
        return value - 1.0 ; 
    }
    else 
        return 0.0 ; 
}

/* Target Function */
double champagneTower(int poured, int query_row, int query_glass)
{
    double * cur = (double *)malloc(sizeof(double)*(query_row+1)) ; 
    double * prev = (double *)malloc(sizeof(double)*(query_row+1)) ; 
    prev[0] = poured ; 
    int i,j ; 
    for (i=1 ; i <= query_row ; i++) {
        cur[0] = excessOfOne(prev[0])/2 ; 
        for (j=1 ; j < i; j++) {
            cur[j] = (excessOfOne(prev[j-1]) + excessOfOne(prev[j]))/2 ; 
        }
        cur[i] = excessOfOne(prev[i-1])/2 ;

        double * temp = cur ; 
        cur = prev ; 
        prev = temp ; 
    }

    double result = prev[query_glass] ;
    free(cur) ; 
    free(prev) ; 
    if (result > 1.0) result = 1.0 ; 
    return result ; 
}

// Wrong
double champagneTowerOld(int poured, int query_row, int query_glass) 
{
    if (poured == 0) return 0.0 ;       
    
    int fullRow = lastFullRow(poured) ; 
    if (query_row <= fullRow) {
        return 1.0 ; 
    }
    if (query_row > fullRow+1) return 0.0 ; 

    int overflow = poured - ((fullRow+1)*(fullRow+1)+fullRow+1)/2 ;   
    double frac = fraction(query_row, query_glass) ; 
    double result = overflow * frac ; 
    if (result >= 1.0) result = 1.0 ; 

    return result ; 
}


// Testing function
void testTower(void)
{
    int poured = 9 ;
    int query_glass = 3 ; 
    int query_row = 3 ; 
    double result = champagneTower(poured, query_row, query_glass) ; 
    printf("result=%f\n", result) ; 
}

void testFraction(void)
{
    int row, col ; 
    for (row = 0 ; row <= 5 ; row++) {
        for (col=0 ; col <= row ; col++) {
            double f = fraction(row, col) ; 
            printf("[%d,%d]=%f\n", row, col, f) ; 
        }
    }
}

void testLastFullRow(void)
{
    int poured = 0 ; 
    int max = 101 ;
    while (poured <= max) {
        printf("poured=%d, last full row=%d\n", poured, \
            lastFullRow(poured)) ; 
        poured += 1 ; 
    }
}

int main(void)
{
    testTower() ;
    // testLastFullRow() ; 
    // testFraction() ; 
    return 0 ;
}
