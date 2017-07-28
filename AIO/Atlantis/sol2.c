/**
Site: Australian Informatic Olympiad
Problem: Atlantis
Author: Ruowei Chen
Date: 19/04/2014
Progress: 
1) Score: 84
   Timeout: #2, #8, #9
   incorrect: #21, #23
   note: First improve timeout problem.
2) Score: 89
   Timeout: #2
   incorrect: #21, #23
   note: Now focus on debug on rare case.
3) Date: 20/04/2014
   Branch out to sol2.c
   Try to use refactor all the code.
   Score: 95
   Timeout: #8, #9
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

struct land 
{
    int id ; 
    int height ; 
    char isWet ;

#define UNVISITED 0
#define VISITED 1
#define SEARCHED 2
    int status ; 
} ; 

int f, h ; 
int r,c ;

#define MAX 10000

struct land land[MAX] ; 
char link[MAX] ; 
int block[MAX] ; // record the lowest block to block from edge

void get_nid(int id, int *nids, int *n) 
{
    int x = id/c ;
    int y = id%c ; 
    int num = 0 ; 
    // upper three lands 
    if (x != 0) {
        if (y != 0) nids[num++] = (x-1)*c+y-1 ; 
        nids[num++] = (x-1)*c+y ; 
        if (y != c-1) nids[num++] = (x-1)*c+y+1 ; 
    }
    // middle two lands
    if (y != 0)  nids[num++] = id-1 ; 
    if (y != c-1) nids[num++] = id+1 ; 

    // Bottom three lands
    if (x != r-1) {
        if (y!=0) nids[num++] = (x+1)*c+y-1 ; 
        nids[num++] = (x+1)*c+y ;
        if (y!=c-1) nids[num++] = (x+1)*c+y+1 ; 
    }
    *n = num ; 
}
// unit test for get_nid
void test_get_nid(void)
{
    int nids[8] ; 
    int num = 0 ;
    int id[9] ; 
    // Corner points
    id[0] = 0 ; 
    id[1] = 0*c+c-1 ; 
    id[2] = (r-1)*c ; 
    id[3] = r*c-1 ; 

    // Four edge points
    id[4] = (r/2)*c ; 
    id[5] = (c/2) ; 
    id[6] = (r/2)*c + c-1 ;
    id[7] = (r-1)*c + c/2 ; 

    // One center point
    id[8] = (r/2)*c + (c/2)-1 ; 

    int i ; 
    for (i=0 ; i<9 ; i++) {
        num = 0 ;
        get_nid(id[i], nids, &num) ; 
        printf("Run %d:\n", i) ; 
        printf("land[%d] has %d neighbours.\n", id[i],num) ; 
        int j ; 
        printf("\t") ; 
        for (j=0 ; j<num ; j++) {
            printf("%d ", nids[j]) ; 
        }
        printf("\n") ; 
    }
}


int search(int *queue,int *num, int id) 
{
    int nid[8] ;
    int n = 0 ; 
    // Get all neighbour land of land[id]
    get_nid(id, nid, &n); 
    
    land[id].status = SEARCHED ; 

    int i ;
    for (i=0 ; i<n ; i++) {
        if (land[nid[i]].status == UNVISITED &&
            land[nid[i]].height < h) {
            land[nid[i]].isWet = 1 ; 
            queue[*num] = nid[i] ; 
            *num += 1 ; 
        }
    }

    return 0 ;
}
// unit test for search
int test_search(void) 
{
    int queue[10] ; 
    int num = 0 ;
    
    int id = 3*c+3 ; 
    //search(queue, &num, 2*c+11) ;
    int tempf = f ; 
    f = 55 ; 
    search(queue, &num, id) ; 
    f = tempf ; 

    int i ; 
    printf("land[%d].height=%d, has %d neighbours.\n", 
            id, land[id].height, num) ; 
    for (i=0 ; i<num ; i++) {
        printf("neighbour id=%d, height=%d\n", 
                queue[i], land[queue[i]].height) ; 
    }

    return 0 ;
}

void print_land(void) 
{
    int i,j ;
    printf("*********** LANDSCAPE ***********\n") ; 
    for (i=0 ; i<r ; i++) {
        for (j=0 ; j<c ; j++) {
            int id = i*c + j ; 
            if (land[id].isWet == 1) 
                printf("~~~ ") ; 
            else
                printf("%3d ", land[id].height) ; 
        }
        printf("\n") ; 
    }
    printf("*********** END OF LAND **********\n") ; 
}


// Check if the land has link to the outside edge
// Link means a land has a path linking to the edge
// where on the path all the lands has a height either
// smaller than or equal to the target land.
void check_link(int id, int block_height) 
{
    // Early exit
//    if (land[id].height < f) return ;
    
//    block[id] = 1001 ; // the maximum height will be 999

    char hasSearched[MAX] ; 
    int i ; 
    for (i=0 ; i<r*c ; i++) {
        hasSearched[i] = 0 ; 
    }
    int queue[MAX] ; 
    int num = 1 ; 
    queue[num-1] = id ; 

    int cur = 0 ; 
    while (cur < num) {
        int nid[8] ; 
        int n = 0 ; 
        get_nid(queue[cur], nid, &n) ; 
        for (i=0 ; i<n  ; i++) {
            if (hasSearched[nid[i]] == 0 &&
                land[nid[i]].height < block_height) {

                if (block_height == h && link[nid[i]] == 1) {
                    int j ;
                    // In water rise mode
                    // You can take all the neighbour 
                    // lands are linked.
                    for (j=0 ; j<num ; j++) 
                        link[j] = 1 ; 
                    link[id] = 1 ; 
                    return ; 
                }
                // In water fall mode
                else if (link[nid[i]] == 1) {
                    link[id] = 1 ; 
                    return ;
                }

                queue[num++] = nid[i] ; 
                hasSearched[nid[i]] = 1 ; 

                if (nid[i]/c == 0 || 
                    nid[i]/c == r-1 ||
                    nid[i]%c == 0 ||
                    nid[i]%c == (c-1)) {
                    link[id] = 1 ;
                    return ; 
                }
            }
        }
        cur++ ; 
    }
} // end of check_link

int main(void) 
{
    FILE *fin, *fout ; 
    fin = fopen("atlanin.txt", "r") ; 
    fout = fopen("atlanout.txt", "w") ;
    assert(fin && fout) ; 
    
    fscanf(fin, "%d %d\n", &h, &f) ; 
    fscanf(fin, "%d %d\n", &r, &c) ; 

    int i,j ; 
    for (i=0 ; i<r ; i++) {
        for (j=0 ; j<c ; j++) {
            int id = i*c+j ; 
            land[id].id = id ; 
            fscanf(fin, "%d", &land[id].height) ; 
            land[id].isWet = 0 ; 
            land[id].status = UNVISITED ; 
            link[id] = 0 ; 
        }
    }
//    print_land() ; // test
    // Water rise
    for (i=0 ; i<r*c ; i++) {
//        link[i] = 0 ; 
        if (land[i].height > h) continue ; 
        if (link[i] == 0) {
            check_link(i,h) ; 
        }
        if (link[i]==1 && 
            land[i].height < h) {
            land[i].isWet = 1 ; 
        }
    }
//    print_land() ; // test

    for (i=0 ; i<r*c ; i++) {
        link[i] = 0 ; 
    }
    // Water falls
    int total = 0 ;
    for (i=0 ; i<r*c ; i++) {
        if (land[i].isWet == 0) continue ; 
        check_link(i, land[i].height+1) ; 
        if (link[i] == 1 &&
            land[i].height > f) {
            land[i].isWet = 0 ; 
        }
        else {
            total ++ ; 
        }
    }
    
//    print_land() ;  // test

    fprintf(fout, "%d\n", total) ; 

#ifdef DEBUG
//    test_get_nid() ; // PASSED
    test_search() ; 
#endif

    return 0;
}
