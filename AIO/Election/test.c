/**
Generate the maximum test case.
*/
#include <stdio.h>
#include <assert.h>
#include <time.h>
#include <stdlib.h>
#define MAX 40000

int w=MAX ; 
int h=MAX ; 
int n=100 ; 
struct rect 
{
    int x ; 
    int y ; 
    int h ;
    int w ;
} ; 

struct rect win[100] ; 

int gen_win(i)
{
    win[i].x = rand()%MAX ; 
    win[i].w = rand()%(MAX-win[i].x) ; 
    win[i].y = rand()%MAX ; 
    win[i].h = rand()%(MAX-win[i].y) ; 
    return 0 ;
}

// Return 1 if no overlap, 0 otherwise.
int isAway(struct rect *r1, struct rect *r2)
{
    if (r1->x >= r2->x+r2->w ||
        r2->x >= r1->x+r1->w ||
        r1->y >= r2->y+r2->h ||
        r2->y >= r1->y+r1->h) {
        return 1 ;    
    }
    return 0 ; 
}

int rectCmp(const void *r1, const void *r2) 
{
    struct rect * rr1 = (struct rect *)r1 ; 
    struct rect * rr2 = (struct rect *)r2 ; 
    return (rr1->x - rr2->x) ; 
}

// Not 100% correct
void rePost(void)
{
    for (int i = 1 ; i<n-1 ; i++) {
        if (isAway(&win[i-1], &win[i]) == 0) {
            win[i-1].w = 3 ; 
            win[i].x = win[i-1].x + win[i-1].w ; 
        }
    }
}

int main(void)
{
    FILE *fout ;
    fout = fopen("maximumcase.txt", "w") ;
    assert(fout) ; 

    int w, h,n ; 
    w = MAX ;
    h = MAX ;
    n = 100 ;
    fprintf(fout, "%d %d\n%d\n", w, h, n) ; 

    srand(time(NULL)); 
    int i ; 
    for (i=0 ; i<n ; i++) {
        gen_win(i) ; 
    }
    qsort(win, n, sizeof(struct rect), rectCmp) ; 
    
    rePost() ; 
    
    for (i=0 ; i<n ; i++) {
        fprintf(fout, "%d %d %d %d\n", 
                win[i].x, win[i].y, win[i].w, win[i].h) ; 
    }
    fclose(fout) ; 
    return 0 ;
}
