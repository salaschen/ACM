/**
Generate the maximum test case.
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <time.h>

int main(void) 
{
    FILE *fout ; 
    fout = fopen("testtxt.in", "w")  ;
    assert(fout) ; 

    srand(time(NULL)) ; 

    int h, f ;
    h = rand()%1000 ; 
    h = (h%2==1)? h+1 : h ;  
    
    f = h-(rand()%h) ; 
    f = (f%2==1)? f+1 : f ; 
    assert(h > f) ; 
    fprintf(fout, "%d %d\n", h, f) ; 
    
    int r=100, c=100 ; 
    fprintf(fout, "%d %d\n", r,c) ; 
    int i,j ; 
    for (i=0 ; i<r ; i++) {
        for (j=0 ; j<c ; j++) {
            int temp = rand()%999 ; 
            temp = (temp%2==0)? temp+1 : temp ; 
            fprintf(fout, "%d ", temp) ; 
        }
        fprintf(fout, "\n") ; 
    }
    fclose(fout) ; 
    return 0 ; 
}
