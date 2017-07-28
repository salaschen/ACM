/**
Prog: Elction
Author: Ruowei Chen
Date: 20/04/2014
Progress: 
    1) Just begin. Think I have some idea.
    Score: 30
    Out of Memory: 7 cases
    2) Rearrange the add_rect function.
    3) Use different method to shorten windows search time.
*/
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#define MAX 40000 


// STRUCT DEFINITION
struct rect {
    int x ;
    int y ; 
    int w ; 
    int h ; 
} ; 

// FUNCTION PROTOTYPE
void print_queue(struct rect *, int) ; 
void subprocess(struct rect * w, int qNdx) ; 

// GLOBAL VARIABLES
struct rect win[MAX] ; 
struct rect *rect[MAX] ;
//int qSize = MAX*10;

short qSize[MAX]  ; // Because I don't know how much memory, just guess.
short qNum[MAX];
int initQsize = 20 ; 
int w, h ; 
int n ; 

// FUNCTION DEFINITION
void add_rect(struct rect **queue, struct rect *newRect, int qIndex)
{
    //assert(queue && newRect) ; 
    // Queue if full, need to realloc space
    if (qNum[qIndex] == qSize[qIndex]) {
        struct rect *newQ = malloc(sizeof(struct rect)*(qSize[qIndex]+20)) ; 
        memcpy(newQ, queue[qIndex], sizeof(struct rect)*qSize[qIndex]) ; 
        qSize[qIndex] += 20 ; 
        free(queue[qIndex]) ; 
        queue[qIndex] = newQ ; 
    }
    
//    void *ppos = &(*queue)[pos] ; 
//    memcpy(ppos, newRect, sizeof(struct rect)) ; 
    void *ppos = &(queue[qIndex][qNum[qIndex]]) ; 
    memcpy(ppos, newRect, sizeof(struct rect)) ; 
    qNum[qIndex] += 1 ; 
}

// unit_test for add_rect
// Passed
void test_add_rect(void) 
{
    struct rect *q[2] ;   
    int numQ = 2 ; 
    
    printf("before malloc\n") ; 
    int i ; 
    for (i=0 ;i<numQ ; i++) {
        q[i] = malloc(sizeof(struct rect)*2) ; 
    }
    printf("finish malloc\n") ; // test

    struct rect r1,r2,r3 ; 
    r1.x=0 ; r1.y=0 ; r1.w=10 ; r1.h = 20 ; 
    r2.x=20 ; r2.y=30 ; r2.w=15 ; r2.h=40 ; 
    r3.x=50 ; r3.y=20 ; r3.w=12 ; r3.h=16 ; 
    
    struct rect r4,r5 ;
    r4.x=33 ; r4.y=34 ; r4.w=14 ; r4.h=17 ; 
    r5.x=34 ; r5.y=35 ; r5.w=16 ; r5.h=18 ; 

    add_rect(q, &r1, 0) ; 
    add_rect(q, &r2, 1) ; 
    add_rect(q, &r3, 0) ; 
    add_rect(q, &r4, 1) ; 
    add_rect(q, &r5, 0) ; 
    add_rect(q,&r5, 1) ; 
    print_queue(q[0], 0) ;
    print_queue(q[1], 1) ; 
//    printf("qNum=%d, qSize=%d\n", qNum, qSize) ; 
}

// Debug print
void print_queue(struct rect *queue, int Ndx)
{
    int i ; 
    printf("qNum=%d, qSize=%d\n", qNum[Ndx], qSize[Ndx]) ; 
    for (i=0 ; i<qNum[Ndx] ; i++) {
        printf("rect[%d]: x=%d, y=%d, w=%d, h=%d\n", 
                i, queue[i].x, queue[i].y, queue[i].w, queue[i].h) ; 
    }
}
void printAll_queue(void) 
{
    printf("*********** Begin **************\n") ; 
    int i ; 
    for (i=0 ; i<MAX ; i++) {
        if (qNum[i] > 0) {
            printf("Queue[%d]:\n", i) ; 
            print_queue(rect[i], i) ; 
        }
    }
    printf("************* End ***************\n") ; 
}


// If the rectangle and window is away
// 1 means yes, 0 otherwise
int isAway(struct rect *r, struct rect *w) 
{
    //assert(r && w) ; 
    if (r->x+r->w <= w->x ||
        w->x+w->w <= r->x ||
        r->y+r->h <= w->y ||
        w->y+w->h <= r->y) {
        return 1 ; 
    }
    return 0 ; 
}
// unit_test for isAway
// Passed
void test_isAway(void)
{
    struct rect r ; 
    struct rect w ; 
    r.x = 0 ; r.y = 10 ; r.w = 20 ; r.h = 10 ; 
    w.x = 30 ; w.w = 5 ; w.y = 12 ; w.h = 5 ; 
    assert(isAway(&r, &w)==1) ;

    w.x = 2 ; w.w = 10 ; w.y = 20 ; w.h = 1 ; 
    assert(isAway(&r, &w) == 1) ; 

    r.x = 10 ; r.w = 5 ; r.y = 10 ; r.h = 10 ; 
    w.x = 5 ; w.w = 5 ; w.y = 6 ; w.h = 20 ; 
    assert(isAway(&r, &w) == 1) ; 

    r.x =10 ; r.w = 5 ; r.y = 10 ; r.h = 10 ; 
    w.x = 11 ; w.w = 4 ; w.y = 5 ; w.h = 5 ; 
    assert(isAway(&r, &w)==1) ; 
    // This case will overlap.
    r.x = 10 ; r.w = 5 ; r.y = 10 ; r.h = 10 ; 
    w.x = 8 ; w.w = 4 ; w.y = 12 ; w.h = 8  ;
    assert(isAway(&r, &w) == 0) ; 
}

// return 1 if w has fully cover r.
// return 0 otherwise
int isFullCover(struct rect *r, struct rect *w)
{
    //assert(r && w) ; 
    if (w->x <= r->x &&
        w->x+w->w >= r->x+r->w &&
        w->y <= r->y &&
        w->y+w->h >= r->y+r->h) {
        return 1 ;
    }
    return 0 ; 
}
// unit_test for isFullCover
void test_isFullCover(void)
{
    struct rect r ;
    struct rect w ; 
    
    r.x = 10 ; r.w = 56 ; r.y = 20 ; r.h = 10 ; 
    w.x = 8 ; w.w = 80 ; w.y = 20 ; w.h = 10 ; 
    assert(isFullCover(&r, &w) == 1) ; 
    
    r.x = 10 ; r.w = 50 ; r.y = 20 ; r.h = 10 ; 
    w.x = 10 ; w.w = 50 ; w.y = 20 ; w.h = 10 ; 
    assert(isFullCover(&r, &w) == 1) ; 

    r.x = 10 ; r.w = 50 ; r.y = 20 ; r.h = 10 ; 
    w.x = 10 ; w.w = 50 ; w.y = 20 ; w.h = 9 ; 
    assert(isFullCover(&r, &w) == 0) ; 
}


void Update(struct rect *r, struct rect *w){
//    assert(r && w) ; 
    struct rect new[4] ; 
    int num = 0 ;
    if (r->x < w->x) {
        new[num].x = r->x ;
        new[num].w = (w->x-r->x) ; 
        new[num].y = r->y ; 
        new[num].h = r->h ; 
        num++ ; 
    }
    if (r->y+r->h > w->y+w->h) {
        new[num].x = r->x ; 
        new[num].w = r->w ; 
        new[num].y = w->y+w->h ; 
        new[num].h = (r->y+r->h - (w->y+w->h)) ; 
        num++ ; 
    }
    if (r->x+r->w > w->x+w->w) {
        new[num].x = w->x+w->w ; 
        new[num].w = (r->x+r->w - (w->x+w->w)) ; 
        new[num].y = r->y ; 
        new[num].h = r->h ; 
        num++ ; 
    }
    if (r->y < w->y) {
        new[num].x = r->x ; 
        new[num].w = r->w ; 
        new[num].y = r->y ; 
        new[num].h = (w->y - r->y) ; 
        num++; 
    }

    // copy the first one in the spot.
//    assert(num > 0) ; 
//    void *src = &new[0] ; 
//    void *dest = &(rect[pos]) ; 
//    memcpy(dest, src, sizeof(struct rect)) ; 

    int i =0 ; 
    for (; i<num ; i++) {
        add_rect(rect, &new[i], new[i].x) ; 
    }
}
void test_Update(void)
{
    int i ; 
    for (i=0 ; i<MAX ; i++) {
        rect[i] = malloc(sizeof(struct rect) * 20) ; 
        qSize[i] = 20 ; 
        qNum[i] = 0 ; 
    }
    struct rect r1, w1; 
    r1.x = 200 ; r1.y = 200 ; r1.w = 600 ; r1.h = 400 ;
    w1.x = 400 ; w1.y = 500 ; w1.w = 50 ; w1.h = 50 ; 
    Update(&r1, &w1) ; 
    printAll_queue() ; 
}


// Process window and update rectangle queue
void process(struct rect *w) {
    int end = w->x + w->w ;
    int i = 0 ; 
    for (i=0 ; i<end ; i++) {
        subprocess(w, i) ; 
    }
}
void subprocess(struct rect * w, int qNdx)
{
    // assert(w) ;
    int i ; 
    for (i=0 ; i<qNum[qNdx] ; ) {
        struct rect * r = &(rect[qNdx][i]) ; 
        if (isAway(r, w) == 1) {
            i++ ; 
        }
        else if (isFullCover(r,w) == 1) {
            if (qNum[qNdx] > 1) {
                void * src = &(rect[qNdx][qNum[qNdx]-1]) ;
                void * dest = &(rect[qNdx][i]) ; 
                memcpy(dest, src, sizeof(struct rect)) ; 
            }
            qNum[qNdx] -- ; 
        }
        else { // Overlap
            struct rect r1 ;
            void * src = &(rect[qNdx][qNum[qNdx]-1]) ;
            void * dest = &(rect[qNdx][i]) ; 
            memcpy(&r1, dest, sizeof(struct rect)) ;
            if (qNum[qNdx] > 1) {
                memcpy(dest, src, sizeof(struct rect)) ; 
            }
            qNum[qNdx] -- ;
            Update(&r1,w) ; // update rectangle in the queue
        }
    }
}


int main(void) 
{
    FILE *fin, *fout ; 
    fin = fopen("elecin.txt", "r") ; 
    fout = fopen("elecout.txt", "w") ;
    //assert(fin) ; 
    //assert(fout) ; 
    
    fscanf(fin, "%d %d\n%d\n", &w, &h, &n) ; 

    int i  ;
    for (i=0 ; i<n ; i++) {
        fscanf(fin, "%d %d %d %d\n",
                &win[i].x, &win[i].y,
                &win[i].w, &win[i].h) ; 
    }
//#ifdef work
    for (i=0 ; i<MAX ; i++) {
        rect[i] = malloc(sizeof(struct rect)*initQsize) ; 
        qSize[i] = initQsize ; 
    }
    struct rect frame ;
    frame.x = 0 ; 
    frame.y = 0 ; 
    frame.w = w ; 
    frame.h = h ; 
    add_rect(rect,&frame, 0) ;  
//    printAll_queue() ; // test
    // Begin to Process each window
    for (i=0 ; i<n ; i++) {
        process(&win[i]) ;
//        printf("win[%d]: x=%d, y=%d, w=%d, h=%d\n", 
 //               i, win[i].x, win[i].y, win[i].w, win[i].h) ; // test
  //      printAll_queue() ; // test
    }
    int result = 0 ; 
    int j ; 
    for (i=0 ; i<MAX  ; i++) {
        for (j=0 ; j<qNum[i] ; j++) {
            struct rect * r = &(rect[i][j]) ; 
            int temp = r->h * r->w ; 
            if (result < temp) result = temp ; 
        }
    }
    fprintf(fout, "%d\n", result) ; 
//#endif
#ifdef test // Unit test area
//    test_add_rect() ;  
    test_Update() ; 
#endif // End of unit test area

    return 0 ; 
}

