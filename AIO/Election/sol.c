/**
Prog: Elction
Author: Ruowei Chen
Date: 20/04/2014
Progress: 
    1) Just begin. Think I have some idea.
    Score: 30
    Out of Memory: 7 cases
    2) Rearrange the add_rect function.
*/
#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>
#define MAX 100 

// STRUCT DEFINITION
struct rect {
    int x ;
    int y ; 
    int w ; 
    int h ; 
} ; 

// FUNCTION PROTOTYPE
void print_queue(struct rect *) ; 


// GLOBAL VARIABLES
struct rect win[MAX] ; 
struct rect *rect ;
//int qSize = MAX*10;
int qSize = 200000; // Because I don't know how much memory, just guess.
int qNum = 0 ;
int w, h ; 
int n ; 

// FUNCTION DEFINITION
void add_rect(struct rect **queue, struct rect *newRect, int pos)
{
    //assert(queue && newRect) ; 
    // Queue if full, need to realloc space
    if (qNum == qSize) {
        struct rect *newQ = malloc(sizeof(struct rect)*(qSize+500)) ; 
        memcpy(newQ, *queue, sizeof(struct rect)*qSize) ; 
        qSize += 500 ; 
        free(*queue) ; 
        *queue = newQ ; 
    }
    
//    void *ppos = &(*queue)[pos] ; 
//    memcpy(ppos, newRect, sizeof(struct rect)) ; 
    (*queue)[pos].x = newRect->x ; 
    (*queue)[pos].y = newRect->y ; 
    (*queue)[pos].w = newRect->w ; 
    (*queue)[pos].h = newRect->h ; 
    if (pos == qNum) {
        qNum ++ ; 
    }
}

// unit_test for add_rect
// Passed
void test_add_rect(void) 
{
    struct rect *q ; 
    qSize = 2 ; 
    q = malloc(sizeof(struct rect)*qSize) ; 
    
    struct rect r1,r2,r3 ; 
    r1.x=0 ; r1.y=0 ; r1.w=10 ; r1.h = 20 ; 
    r2.x=20 ; r2.y=30 ; r2.w=15 ; r2.h=40 ; 
    r3.x=50 ; r3.y=20 ; r3.w=12 ; r3.h=16 ; 
    
    struct rect r4,r5 ;
    r4.x=33 ; r4.y=34 ; r4.w=14 ; r4.h=17 ; 
    r5.x=34 ; r5.y=35 ; r5.w=16 ; r5.h=18 ; 

    add_rect(&q,&r1, 0) ; 
    add_rect(&q,&r2, 1) ; 
    add_rect(&q,&r3, 2) ; 
    add_rect(&q,&r4, 3) ; 
    add_rect(&q,&r5, 4) ; 
    add_rect(&q,&r5, 0) ; 
    print_queue(q) ; 
    printf("qNum=%d, qSize=%d\n", qNum, qSize) ; 
}

// Debug print
void print_queue(struct rect * queue)
{
    int i ; 
    printf("*********** Begin **************\n") ; 
    printf("qNum=%d, qSize=%d\n", qNum, qSize) ; 
    for (i=0 ; i<qNum ; i++) {
        printf("rect[%d]: x=%d, y=%d, w=%d, h=%d\n", 
                i, queue[i].x, queue[i].y, queue[i].w, queue[i].h) ; 
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


void Update(struct rect *r, struct rect *w, int pos){
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
    void *src = &new[0] ; 
    void *dest = &(rect[pos]) ; 
    memcpy(dest, src, sizeof(struct rect)) ; 

    int i =1 ; 
    for (; i<num ; i++) {
        add_rect(&rect, &new[i], qNum) ; 
    }
}

// Process window and update rectangle queue
void process(struct rect * w)
{
    // assert(w) ;
    int i ; 
    for (i=0 ; i<qNum ; ) {
        struct rect * r = &rect[i] ; 
        if (isAway(r, w) == 1) {
            i++ ; 
        }
        else if (isFullCover(r,w) == 1) {
            void * src = &rect[qNum-1] ;
            void * dest = &rect[i] ; 
            memcpy(dest, src, sizeof(struct rect)) ; 
            qNum -- ; 
        }
        else {
            Update(r,w,i) ; // update rectangle in the queue
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
    
    printf("memory: %lu KB\n", sizeof(struct rect) * qSize/1000) ; // test

    int i  ;
    for (i=0 ; i<n ; i++) {
        fscanf(fin, "%d %d %d %d\n",
                &win[i].x, &win[i].y,
                &win[i].w, &win[i].h) ; 
    }
    rect = malloc(sizeof(struct rect)*qSize) ; 
    struct rect frame ;
    frame.x = 0 ; 
    frame.y = 0 ; 
    frame.w = w ; 
    frame.h = h ; 
    add_rect(&rect,&frame, qNum) ;  
//    print_queue(rect) ; // test

    // Begin to Process each window
    for (i=0 ; i<n ; i++) {
        process(&win[i]) ;
    }
    int result = 0 ; 
    for (i=0 ; i<qNum ; i++) {
        int temp = rect[i].w*rect[i].h ; 
        if (temp > result) 
            result = temp ; 
    }
//    print_queue(rect) ; // test
    fprintf(fout, "%d\n", result) ; 

#ifdef test // Unit test area
    //test_add_rect() ;  
    test_isAway() ; 
    test_isFullCover() ; 
#endif // End of unit test area

    return 0 ; 
}

