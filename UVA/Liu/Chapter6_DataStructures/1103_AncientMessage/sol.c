/**
 * Prob: UVA 1103 - Ancient Messages
 * Date: 20/Nov/2017
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define MAX_H 200
#define MAX_W 50
int H, W ; 

char matrix[MAX_H+5][4*MAX_W+20] ; 

//---------------------------
// The List ADT
typedef struct List 
{
    void * buf ; 
    int elemSize ; // size in bytes of each element
    int length ; // actual number of elements
    int bufLen ; // capacity
    void (*deleteObject) (void *) ; // The function that delete the object
    void (*printObject) (int, void *) ; // method to print the object
} List ; 

// Create a new List
// memory is allocated in the call function
List * newList
(int elemSize, void(*deleteobject)(void *), 
 void (*printObject) (int, void *))
{
    List * result = (List *)malloc(sizeof(List)) ; 
    result->bufLen = 30 ; 
    result->buf = malloc(elemSize * result->bufLen) ; 
    result->deleteObject = deleteobject ; 
    result->length = 0 ; 
    result->elemSize = elemSize ; 
    result->printObject = printObject ; 
    return result ; 
}

void printInt(int pos, void * target)
{
    printf("list[%d] = %d\n", pos, *(int *)target) ; 
}

// n starts from 1.
// Doesn't delete the object
void * getNthObject(List * list, int n)
{
    if (list == NULL) return NULL ; 
    if (list->length < n) return NULL ; 
    void * result = (void *)((char *)list->buf + (n-1)*list->elemSize) ; 
    return result ; 
}

// the list pointer is not freed.
void clearList(List * list)
{
    if (list == NULL)
        return ; 
    // delete each object in the list first
    int i ; 
    if (list->deleteObject != NULL) {
        for (i=0 ; i < list->length ; i++) {
            void * curObject = getNthObject(list, i+1) ; 
            list->deleteObject(curObject) ; 
        }
    }
    
    // delete the whole list
    free(list->buf) ; 
    // free(list) ; 
}

void push(List * list, void * object)
{
    // push the object to the end of the list
    assert(list != NULL) ; 
    if (list->bufLen == list->length) // list is full
    {
        int newbufLen = list->bufLen + 20 ; 
        void * newBuf = malloc(list->elemSize * newbufLen) ; 
        memcpy(newBuf, list->buf, list->elemSize * list->length) ; 
        clearList(list) ; 
        list->buf = newBuf ;
        list->bufLen = newbufLen ; 
    }
    void * space = (void *)( (char *)list->buf + list->elemSize*list->length ) ;
    memcpy(space, object, list->elemSize) ; 
    list->length += 1 ; 
}
int pop(List * list, void * result)
{
    // return  the last object in the list and delete it
    // return NULL if the list is already empty
    // store the reuslt into the result pointer, assuming it has enough memory
    assert(list != NULL && result != NULL); 
    if (list->length == 0) return 1; // return 1 if fails
    void * target = (void *) ((char *)list->buf + list->elemSize*(list->length-1)) ; 
    memcpy(result, target, list->elemSize) ; 

    if (list->deleteObject != NULL) {
        list->deleteObject(target) ; 
    }
    list->length -= 1 ; 
    return 0 ; 
}


void concat(List * list, List * tail)
{
    assert(list && tail) ; 
    // push all objects in tail into target
    int i ; 
    for (i=0 ; i < tail->length ; i++) {
        void * target = (void *)((char *)tail->buf+tail->elemSize*i ) ; 
        push(list, target) ; 
    }
}

void printList(List * list)
{
    assert(list != NULL) ; 
    printf("list length is %d\n", list->length) ; 
    if (list->printObject)
    {
        int i ; 
        for (i=0 ; i < list->length ; i++) {
            void * target = (void *)((char *)list->buf + list->elemSize * i) ;
            list->printObject(i, target) ; 
        }
    }
}

void testList()
{
    List * intList = newList(sizeof(int), NULL, printInt) ;    
    int i ; 
    for (i=0 ; i < 50 ; i++) {
        push(intList, &i) ; 
        printf("%d has been pushed into list.\n", i) ; 
    }
    for (i=0 ; i < 10 ; i++) {
        int result ; 
        pop(intList, &result) ; 
        printf("%d has been poped from the list.\n", result) ; 
    }
    printList(intList) ; 
    clearList(intList) ; 
    free(intList) ;    
}

//---------------------------

typedef struct Point
{
    int x ; 
    int y ;
} Point ; 

void printPoint(int pos, void * point)
{
    printf("list[%d]: [%d,%d]\n", pos,
            ((Point *)point)->x, ((Point *)point)->y) ; 
}

//---------------------------------
// Actual program

void translate(int num, char *result)
{
    int i = 0 ; 
    while (i < 4) {
        result[3-i] = num % 2 + '0' ; 
        num /= 2 ;
        i += 1 ; 
    }
    return ;
}

int readInput(void)
{
    scanf("%d %d\n", &H, &W) ; 
//    printf("H=%d, W=%d\n", H, W) ; // debug
    if (H == 0 && W == 0)
        return 1 ;
    int i, j ;
    int temp ; 
    char t[5] ; t[4] = '\0' ;
    for (i=0 ; i < H ; i++) 
    {
        for (j=0 ; j < W ; j++)
        {
            char c[2] ;
            c[0] = getchar() ; c[1] = '\0' ; 
            sscanf(c, "%x", &temp) ; 
            translate(temp, t) ; 
            memcpy(&matrix[i][4*j], t, 4) ; 
        }    
        matrix[i][4*W] = '\0' ; 
        // printf("%s\n", matrix[i]) ; // debug
        getchar() ; // skip the '\n'
    }
    return 0 ;
}

void printMatrix(void)
{
    int i,j ; 
    for (i=0 ;i < H ; i++)
    {
        for (j=0 ; j < 4*W ; j++) {
            putchar(matrix[i][j]) ; 
        }
        printf("\n") ; 
    }
}

#define Outside ('o')

int IsOnBoard(Point * p)
{
    // return 0 if point is onboard (valid), 1 otherwise
    if (p == NULL) return 1 ; 
    if (p->y < 0 || p->y >= 4*W) return 1 ;
    if (p->x < 0 || p->x >= H) return 1 ; 
    return 0 ;
}

void getNeighbors(List * list, Point * point)
{
    // Doesn't do any sanity check at all
    assert(list != NULL && point != NULL) ; 
    Point p ; 
    p.x = point->x ; p.y = point->y - 1 ; push(list, &p) ; // top
    p.x = point->x ; p.y = point->y + 1 ; push(list, &p) ; // bottom
    p.x = point->x-1 ; p.y = point->y ; push(list, &p) ; // left ; 
    p.x = point->x+1 ; p.y = point->y ; push(list, &p) ; // right ;
}

void printMark(int * mark, int H, int W)
{
    int i,j ;
    for (i=0 ; i < H ; i++) {
        for (j=0 ; j < 4*W ; j++) {
            printf("%+2d ", *(mark+4*i*W+j)) ; 
        }
        printf("\n") ; 
    }
}

void sweepOuterWhite(int * mark)
{
    // Search all the white space that's connected to the outside.
    // Mark them as IsOut.
    List * points = newList(sizeof(Point), NULL, printPoint) ; 
    int i ; 
    Point p ; 
    for (i=0 ; i < 4*W ; i++) {
        p.x = 0 ; 
        p.y = i ; 
        push(points, &p) ; 
        p.x = H-1 ; 
        push(points, &p) ; 
    }
    for (i=0 ; i < H ; i++) {
        p.x = i ; p.y = 0 ; push(points, &p) ;
        p.y = 4*W-1 ; push(points, &p) ; 
    }
    // printList(points) ; // debug
    List * neighbors = newList(sizeof(Point), NULL, printPoint) ; 
    while (points->length > 0)
    {
        // printf("points length=%d\n", points->length) ; // debug
        Point point  ; 
        pop(points, &point) ; 
        if (IsOnBoard(&point) == 1)
            continue ; 
        else if (matrix[point.x][point.y] == '1')
            continue ; 
        else if (matrix[point.x][point.y] == Outside) 
            continue ;
        else {
            matrix[point.x][point.y] = Outside ; 
            *(mark+point.x*4*W+point.y) = -1 ; // outside is -1
            getNeighbors(neighbors, &point) ; 
            concat(points, neighbors) ; 
            neighbors->length = 0 ; // lazy delete all the objects
        }
    }
    // printMatrix() ; // debug
    // printMark(mark, H, W) ; // debug
}

List * search(List * list, int label, int * mark)
{
    // search the connected black component in this 
    // list. And update the mark 
    List * whiteList = newList(sizeof(Point), NULL, NULL) ; 
    List * neighbors = newList(sizeof(Point), NULL, NULL) ; 
    while (list->length > 0)
    {
        Point p ; 
        pop(list, &p) ; 
        if (IsOnBoard(&p) == 1) continue ; // point is invalid       
        else if (*(mark+p.x*4*W+p.y) == -1) // it's an external white point
            continue ; 
        else if (matrix[p.x][p.y] == '0')  {// internal white point 
            push(whiteList, &p) ; 
        }
        else if (matrix[p.x][p.y] == '1' && *(mark+p.x*4*W+p.y) == 0 ) { // black point
            *(mark+p.x*4*W+p.y) = label ;
            getNeighbors(neighbors, &p) ; 
            concat(list, neighbors) ; // add the points to the search
            neighbors->length = 0; // lazy delete the added points.
        }
    }
    free(neighbors) ; 
    return whiteList ; 
}

void searchWhite(Point * p, int label, int * mark)
{
    List * list = newList(sizeof(Point), NULL, NULL) ; 
    List * neighbors = newList(sizeof(Point), NULL, NULL) ; 
    push(list, p) ; 
    while (list->length > 0)
    {
        Point point ; 
        pop(list, &point) ; 
        if (IsOnBoard(&point) == 1) continue ; 
        else if (matrix[point.x][point.y] != '0') continue ; 
        else if (*(mark+point.x*4*W+point.y) == label) continue ; 
        else {
            *(mark+point.x*4*W+point.y) = label ; 
            getNeighbors(neighbors, &point) ; 
            concat(list, neighbors) ;  
            neighbors->length = 0 ; 
        }
    }
    clearList(list) ; 
    clearList(neighbors) ; 
    free(list) ; 
    free(neighbors) ; 
}

int getNumHole(List * list, int label, int * mark)
{
    int num =0 ; 
    while (list->length > 0) {
        Point p ; 
        pop(list, &p) ; 
        if (*(mark+p.x*4*W+p.y) != label) {
            num += 1 ; 
            searchWhite(&p, label, mark) ; 
        }
    }
    return num ; 
}

char getChar(int num)
{
    switch (num) {
        case 1: 
            return 'A';
        case 2: 
            return 'K' ;
        case 3:
            return 'J' ;
        case 4:
            return 'S' ; 
        case 5:
            return 'D' ; 
        case 0:
            return 'W' ; 
        default:
            return 'Z' ; 
    }
}

List * sweepBlack(int * mark)
{
    // search all the black components and label them.
    int curLabel = 1 ; 
    int i,j ; 
    List * result = newList(sizeof(char), NULL, NULL) ; 
    for (i=0 ; i < H ; i++) {
        for (j=0 ; j < 4*W ; j++) {
            if (matrix[i][j] == '1' && *(mark+4*W*i+j)==0) {
                Point p ;  
                p.x = i ; p.y = j ; 
                List * blackList = newList(sizeof(Point), NULL, NULL) ; 
                push(blackList, &p) ;
                List * whiteList = search(blackList, curLabel, mark) ; 
                clearList(blackList) ; 
                free(blackList) ;

                int numHole = getNumHole(whiteList, curLabel, mark) ; 
                // printf("numHole = %d\n", numHole) ; // debug
                char c = getChar(numHole) ; 
                push(result, &c) ; 
                curLabel += 1 ;
                // TODO: We need to count how many white compoenents that
                // this white lists forms.
            }
        }
    }
    // printf("After sweep black\n") ; // debug
    // printMark(mark, H, W) ; // debug

    return result ; 
}

int charCmp(const void *c1, const void * c2)
{
    return (int)(*(char *)c1 - *(char *)c2) ; 
}

int work(int Case)
{
    if (readInput() == 1)
        return 1 ; 
    
    // use marking to indicate does the grid connect to outside
    // or which black characters it belongs to.
    int *mark = (int *)malloc(sizeof(int)*H*W*4) ;
    memset(mark, 0, H*W*4*sizeof(int)) ; 

    // printf("SweepOuterWhite:\n") ; // debug
    sweepOuterWhite(mark) ; 
    List * result = sweepBlack(mark) ;
    qsort(result->buf, result->length, result->elemSize, charCmp) ; 
    
    char end = '\0' ; 
    push(result, &end) ; 
    printf("Case %d: %s\n", Case, result->buf) ; 
    clearList(result) ; 
    free(result) ; 
    free(mark) ;
    return 0 ;
}


int main(void)
{
    // testList() ; // debug
    
    int Case = 1 ;
    while (work(Case) == 0) {
        Case += 1 ; 
    }
    return 0 ;
}




