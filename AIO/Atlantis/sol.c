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


// Check if the node is link to the outside edge
void check_link(int id) 
{
    if (land[id].height < f) return ;
    char hasSearched[MAX] ; 
    int i ; 
    for (i=0 ; i<r*c ; i++) {
        hasSearched[i] = 0 ; 
    }
//    printf("After allocation hasSearched.\n") ; // test
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
                land[nid[i]].height <= land[id].height) {
                // Early Exit
                if (link[nid[i]] == 1)  {
                    link[id] = 1 ; 
                //    int j ; 
                //    for (j=0 ; j<num ; j++) 
               //         link[queue[j]] = 1 ;  // mark all as link

                    return ; 
                }

                queue[num++] = nid[i] ; 
                hasSearched[nid[i]] = 1 ; 

                if (nid[i]/c == 0 || 
                    nid[i]/c == r-1 ||
                    nid[i]%c == 0 ||
                    nid[i]%c == (c-1)) {
                    link[id] = 1 ;
           //         int j ; 
            //        for (j=0 ; j<num ; j++) 
             //           link[queue[j]] = 1 ;  // mark all as link
                   return ; 
                }
            }
        }
        cur++ ; 
    }
}

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
        }
    }

    int queue[MAX] ; 
    int num =0 ; 
    // Add all edge lands into queue if possible.
    for (j=0; j<c ; j++) {
        for (i=0 ; i<r ; i+= r-1) {
            if (land[j].height < f) {
                land[j].isWet = 1 ; 
                land[j].status = VISITED ; 
                queue[num++] = land[j].id ; 
            }
        }
    }
    for (i=1 ; i<r-1 ; i++) {
        for (j=0 ; j<c ; j+= c-1) {
            int id = i*c+j ; 
            if (land[id].height < f) {
                land[id].isWet =1 ;
                land[id].status = VISITED ; 
                queue[num++] = land[id].id ; 
            }
        }
    }
    while (num > 0) {
        int id = queue[num-1] ; 
        num -- ; 
        land[id].status = SEARCHED ; 
        search(queue, &num, id) ;  
    }
    // Debug print
//    print_land() ; // test

    // Water falls
    for (i=0 ; i<r*c ; i++) {
        land[i].status = UNVISITED ; 
        link[i] = 0 ; 
    }
    
    for (i=0 ; i<r*c ; i++) {
       if (link[i] == 0) 
            check_link(i) ; 
       if (land[i].height>f && link[i]==1)
           land[i].isWet = 0 ;
//       printf("i=%d in check_link\n", i) ; // test
    }
//    printf("land[%d].link = %d, height=%d\n",
//          22, link[22], land[22].height) ; // test

 //   printf("finish check_link\n") ; // test
//    print_land() ;  // test

    int total = 0 ; 
    for (i=0 ; i<r*c ; i++) {
        if (land[i].isWet == 1)
            total ++ ; 
    }

    fprintf(fout, "%d\n", total) ; 

#ifdef DEBUG
//    test_get_nid() ; // PASSED
    test_search() ; 
#endif

    return 0;
}
