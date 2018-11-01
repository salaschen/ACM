/**
 *  Brute-Force first
 *
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define BRANCH 0
#define LEAF 1

typedef enum {black=1, white=0, grey = 2} Color ;

// Typedefs
typedef struct Node
{
    int num ;  // base 5 number, represent the sequence number of the block.
    int tly, tlx ; // top left (x,y) // start from 1, up to n
    int bry, brx ; // bottom right (x,y) ; 
    Color color; // black = 1, white = 0, grey = 2.
} Node ; 

typedef struct NodeQueue
{
    int * buf ; 
    int bufSize ; // capacity of the queue.
    int elemSize ; // number of elements
}NodeQueue ; 


// Prototypes
void ImageToNum(int Case, int num) ; 
void NumToImage(int Case, int num) ; 
Color GetNodeColor(Node * node) ;

int 
numDigits(int num)
{
    // assume num >= 0
    int d = 1 ; 
    if (num == 0) return 1 ; 
    while (num >= 10) {
        d += 1 ; 
        num /= 10 ; 
    }
    int ten = 1 ; 
    int i ; 
    for (i=1 ; i <= d ; i++) {
        ten *= 10 ; 
    }
    return ten ; 
}

NodeQueue * 
CreateQueue(int bufSize)
{
    if (bufSize <= 0) {
        bufSize = 1 ; 
    }
    NodeQueue * queue = (NodeQueue *)malloc(sizeof(NodeQueue)) ; 
    queue->bufSize = bufSize ; 
    queue->elemSize = 0 ; 
    queue->buf = (int *)malloc(sizeof(int)*bufSize) ; 
    return queue ; 
}

void 
FreeNodeQueue(NodeQueue * queue) 
{
    if (queue != NULL) {
        free(queue->buf) ;
    }
    free(queue) ;
}

int
intCmp(const void * i1, const void *i2) 
{
    const int *ii1 = (int *)i1 ;
    const int *ii2 = (int *)i2 ; 
    return *ii1 - *ii2 ; 
}

int
BaseFiveToBaseTen(int num)
{
    if (num <= 0) return 0 ; 
    int base = 1 ; 
    int result = (num % 10) * base ; 
    num /= 10 ; 
    base *= 5 ; 
    while (num > 0) {
        result += (num % 10) * base ; 
        num /= 10 ; 
        base *= 5 ; 
    }
    return result ; 
}

int 
BaseTenToBaseFive(int num)
{
   int result = num % 5 ; 
   num /= 5 ; 
   int base = 10 ; 
   while (num > 0) {
        result += (num % 5) * base ; 
        num /= 5 ; 
        base *= 10 ; 
   }
   return result ; 
}

void
testTenToFive()
{
    int ten = 10 ;
    int five = BaseTenToBaseFive(ten) ; 
    printf("(10)%d = (5)%d\n", ten, five) ; 

    ten = 4 ;
    five = BaseTenToBaseFive(ten) ; 
    printf("(10)%d = (5)%d\n", ten, five) ; 

    ten = 25 ;
    five = BaseTenToBaseFive(ten) ; 
    printf("(10)%d = (5)%d\n", ten, five) ; 

    ten = 24 ;
    five = BaseTenToBaseFive(ten) ; 
    printf("(10)%d = (5)%d\n", ten, five) ; 

    ten = 253 ;
    five = BaseTenToBaseFive(ten) ; 
    printf("(10)%d = (5)%d\n", ten, five) ; 
}

void
AddToNodeQueue(NodeQueue * queue, int number) 
{
    // printf("queue elemSize=%d, bufSize=%d, number=%d\n", 
    //       queue->elemSize, queue->bufSize, number) ; // debug
    if (queue->bufSize == queue->elemSize) {
        queue->buf = (int *)realloc(queue->buf, sizeof(int)*2*queue->bufSize) ; 
        queue->bufSize *= 2 ;
    }
    int * pos = &(queue->buf[queue->elemSize]) ;
    int BaseTenNumber = BaseFiveToBaseTen(number) ; 
    memcpy(pos, &BaseTenNumber, sizeof(int)) ; 
    queue->elemSize += 1 ; 
}

char image[64][64] ;
int n ; 

// Helper function
void 
printNode(Node * node)
{
    //printf("num=%d, color=%d, tl(%d,%d), br(%d,%d)\n", 
    //        node->num, node->color, node->tlx,node->tly, node->brx, node->bry) ;
    int i,j ; 
    for (i=node->tly ; i <= node->bry ; i++) {
        for (j=node->tlx ; j <= node->brx ; j++) {
            printf("%c", image[i-1][j-1]) ; 
        }
        printf("\n") ; 
    }
}

void 
TranslateNode(Node *node, int num)
{
    if (num == 0) {
        // Draw the image
        int i, j ;
        for (i=node->tly ; i <=node->bry ; i++) {
            for (j=node->tlx ; j<=node->brx; j++ ) {
                image[i-1][j-1] = '*' ;
            }
        }
        return ; 
    }
    int temp = num % 10 ; 
    num /= 10 ; 
    int half = (node->brx-node->tlx+1)/2 ; 
    if (temp == 1) { // 1) NW
        node->tlx = node->tlx ; node->tly = node->tly ; 
        node->brx = node->tlx+half-1 ; node->bry = node->tly+half-1 ; 
    }
    else if (temp == 2) { // 2) NE
        node->tlx = node->tlx+half ; node->tly = node->tly ; 
        node->brx = node->brx ; node->bry = node->tly+half-1 ;
    }
    else if (temp == 3) { // 3) SW
        node->tlx = node->tlx ; node->tly = node->tly+half ; 
        node->brx = node->tlx+half-1 ; node->bry = node->bry ;
    }
    else if (temp == 4) { // 4) SE
        node->tlx = node->tlx+half ; node->tly = node->tly+half ; 
        node->brx = node->brx ; node->bry = node->bry ;
    }
    TranslateNode(node, num) ;
}

void 
printQueue(NodeQueue * queue)
{
    if (queue == NULL) return ;
    if (queue->elemSize == 0) return ; 
    qsort(queue->buf, queue->elemSize, sizeof(int), intCmp) ; 

    printf("%d", queue->buf[0]) ; 
    int i ; 
    for (i=2 ; i <= queue->elemSize ; i++) {
        if ((i-1) % 12 == 0) {
            printf("\n") ; 
        }
        else 
            printf(" ") ; 
        printf("%d", queue->buf[i-1]) ; 
    }
    printf("\n") ; 
}


void
SearchNode(Node * node, NodeQueue * queue)
{
    node->color = GetNodeColor(node) ; 
    if (node->color == black) {
        AddToNodeQueue(queue, node->num)  ;
        return ; 
    }
    else if (node->color == grey) {
        // split into four nodes.
        int half = (node->brx-node->tlx+1)/2 ; 
        // 1) NW
        Node child ; 
        child.num = 1 * numDigits(node->num) + node->num ; 
        child.tlx = node->tlx ; child.tly = node->tly ; 
        child.brx = node->tlx+half-1 ; child.bry = node->tly+half-1 ; 
        SearchNode(&child, queue) ; 

        // 2) NE
        child.num = 2 * numDigits(node->num) + node->num ; 
        child.tlx = node->tlx+half ; child.tly = node->tly ; 
        child.brx = node->brx ; child.bry = node->tly+half-1 ;
        SearchNode(&child, queue) ; 

        // 3) SW
        child.num = 3 * numDigits(node->num) + node->num ; 
        child.tlx = node->tlx ; child.tly = node->tly+half ; 
        child.brx = node->tlx+half-1 ; child.bry = node->bry ;
        SearchNode(&child, queue) ; 

        // 4) SE
        child.num = 4 * numDigits(node->num) + node->num ; 
        child.tlx = node->tlx+half ; child.tly = node->tly+half ; 
        child.brx = node->brx ; child.bry = node->bry ;
        SearchNode(&child, queue) ; 
    }
}

Color 
GetNodeColor(Node * node)
/**
 *  assume node is not null
 *  Return the color code (1=black,0=white,2=grey)
 */
{
    int x, y ; 
    Color color = (Color)(image[node->tly-1][node->tlx-1]-'0') ;     
    for (y = node-> tly ; y <= node->bry ; y++) {
        for (x = node->tlx ; x <= node->brx ; x++) {
            if ((image[y-1][x-1]-'0') != color) {
                return grey ; 
            }
        }
    }   
    return color ; 
}

void work(int Case, int num) {
    if (Case > 1) {
        printf("\n") ; 
    }
    if (num > 0) {
        n = num ; 
        ImageToNum(Case, num) ; 
    }
    else {
        n = -1*num ; 
        NumToImage(Case, -1*num) ; 
    }
}

void ImageToNum(int Case, int num)
{
    scanf("\n") ; 
    int i, j ; 
    for (i=0; i < num ; i++) {
        for (j=0 ; j < num ; j++) {
            scanf("%c", &image[i][j]) ; 
        }
        scanf("\n") ; 
        image[i][num] = '\0' ; 
        // printf("%d row is : %s\n", i, image[i]) ; // debug
    }
    
    Node node ;    
    node.num = 0 ; node.tlx = 1 ; node.tly = 1 ; node.brx = num; 
    node.bry = num; 
    node.color = GetNodeColor(&node) ; 
    NodeQueue * queue = CreateQueue(10) ; 
    // printf("queue: %d %d\n", queue->elemSize, queue->bufSize) ; // debug
    
    SearchNode(&node, queue) ; 
    
    printf("Image %d\n", Case) ;
    printQueue(queue) ; 
    printf("Total number of black nodes = %d\n", queue->elemSize) ; 
    
    // Free the queue
    FreeNodeQueue(queue) ; 
}

void NumToImage(int Case, int num) 
{
    // Initialize image
    int i, j ; 
    for (i = 0 ; i < num ; i++) {
        for (j=0 ; j < num ; j++) {
            image[i][j] = '.' ; 
        }
    }
    
    // Create Node based on the number
    while (1) {
        int temp ;  
        scanf("%d", &temp) ; 
        if (temp == -1) {
            break; 
        }
        Node node ; 
        node.num = temp ; 
        node.color=  black ;
        node.tlx = 1 ; node.tly = 1 ; 
        node.brx = num ; node.bry = num ; 
        TranslateNode(&node, BaseTenToBaseFive(temp)) ; 

    }
    Node node ; 
    node.num = 0 ; 
    node.tlx = 1 ; node.tly = 1 ; 
    node.brx = num ; node.bry = num ; 
    printf("Image %d\n", Case) ; 
    printNode(&node) ; 
}

int main(void)
{
    // testTenToFive() ;// debug

    int num ; 
    int Case = 1 ;

    scanf("%d", &num) ; 
    while (num != 0) {
        work(Case, num) ; 
        Case ++ ; 
        scanf("%d", &num) ; 
    }
    return 0  ;
}
