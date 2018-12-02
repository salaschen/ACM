/**
 * UVa 1354a Mobile Computing, ACM/ICPC Tokyo 2005
 * Date: 02/Dec/2018
 * 
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int value ; 
    double pos ; 
    struct Node * left ; 
    struct Node * right ; 
} Node ; 

typedef struct List
{
    double * buf ;
    int num ; 
    int size ; 
} List ; 


List * CreateList(int size)
{
    List * list = (List *)malloc(sizeof(List)) ; 
    list->size = size ; 
    list->buf = (double *)malloc(sizeof(double)*list->size) ; 
    return list ;
}

void AddList(List * list, double num)
{
    if (list->num == list->size) {
        list->size += 50 ;
        list->buf = (double * )realloc(list->buf, list->size*sizeof(double)) ;
    }
    list->buf[list->num++] = num ; 
}

Node * NewNodeWithValue(int value)
{
    Node * newNode = (Node *)malloc(sizeof(Node)) ; 
    newNode->value = value ; 
    newNode->left = NULL ; 
    newNode->right = NULL ; 
    newNode->pos = 0 ; 
    return newNode ; 
}
Node * NewNodeWithNodes(Node * left, Node * right)
{
    if (left == NULL || right == NULL) 
        return NULL ; 

    Node * newNode = NewNodeWithValue(left->value+right->value) ;
    newNode->left = left ; 
    newNode->right = right ; 
    newNode->pos = 0 ; 
    return newNode ; 
}

void PrintNode(Node * node)
{
    if (node == NULL) return ; 
    printf("[node]: value=%d, pos=%lf, left=%d, right=%d\n",
            node->value, node->pos, (node->left)? node->left->value : -1, 
            (node->right)? node->right->value : -1) ; 
}
void FreeNode(Node * node)
{
    if (node == NULL) return ;
    FreeNode(node->left) ; 
    FreeNode(node->right) ; 
    free(node) ; 
}
double leftEnd(Node * node)
{
    if (node->left == NULL || node->right == NULL) {
        return node->pos ; 
    }
    else {
        // calculate the node position for the left and right
        int lw = node->left->value , rw = node->right->value ; 
        double ll = rw*1.0/(rw+lw) ;  // left length
        double rl = lw*1.0/(rw+lw) ;  // right length
        node->left->pos = node->pos - ll ; 
        node->right->pos = node->pos + rl ; 

        // recursively get the children's left end
        double llend = leftEnd(node->left) ; 
        double rlend = leftEnd(node->right) ; 
        if (llend < rlend) return llend ; 
        else return rlend ; 
    }
}

double rightEnd(Node * node)
{
    if (node->left == NULL || node->right == NULL) {
        return node->pos ; 
    }
    else {
        // calculate the node position for the left and right
        if (node->left->pos == 0 || node->right->pos == 0) {
            int lw = node->left->value , rw = node->right->value ; 
            double ll = rw*1.0/(rw+lw) ;  // left length
            double rl = lw*1.0/(rw+lw) ;  // right length
            node->left->pos = node->pos - ll ; 
            node->right->pos = node->pos + rl ; 
        }

        // recursively get the children's left end
        double llend = rightEnd(node->left) ; 
        double rlend = rightEnd(node->right) ; 
        if (llend > rlend) return llend ; 
        else return rlend ; 
    }
}

List * list ; 

void search(Node ** nodes, int numNode)
{
    if (numNode == 1) {
        Node * root = nodes[0] ; 
        root->pos = 0 ;    
        double left = leftEnd(root) ; 
        double right=  rightEnd(root) ;
        // printf("left=%lf, right=%lf, width=%.10lf\n", left, right, right-left) ; // debug
        AddList(list, (right-left)) ; 
    }
    else {
        int i, j ;   
        for (i=0 ; i < numNode ; i++) {
            for (j=0 ; j < numNode ; j++) {
                if (i == j) continue ;
                Node * compNode = NewNodeWithNodes(nodes[i], nodes[j]) ; 
                Node ** newNodes = (Node **)malloc(sizeof(Node *)*numNode) ;
                newNodes[0] = compNode ; 
                int k ; 
                int num = 1 ; 
                for (k=0 ; k < numNode ; k++) {
                    if (k != i && k != j) {
                        newNodes[num++] = nodes[k] ; 
                    }
                }
                search(newNodes, numNode-1) ;
                free(compNode) ; 
                free(newNodes) ; 
            }
        }
    }
}

int work(void)
{
    list->num = 0 ; // clear the list first
    double room  ;
    int s ; 
    scanf("%lf\n", &room) ; 
    scanf("%d\n", &s) ; 
    int i ; 

    Node ** nodes = (Node **)malloc(sizeof(Node *)*s) ; 
    for (i= 0 ; i < s ; i++) {
        int temp ;
        scanf("%d\n", &temp) ; 
        nodes[i] = NewNodeWithValue(temp) ; 
        // PrintNode(nodes[i]) ; // debug
    }

    search(nodes, s) ;
    double result = -1.0 ;
    for (i=0 ; i < list->num ; i++) {
        if (list->buf[i] > result && list->buf[i] < (room)) {
            result = list->buf[i] ; 
        }
    }   
    if (result < 0) {
        printf("-1\n") ; 
    }
    else {
        printf("%.16lf\n", result) ; 
    }
    return 0 ;
}

int solve(void)
{
    list = CreateList(100) ; 
    int n ; 
    scanf("%d\n", &n) ; 
    int i ; 
    for (i=0 ; i < n ; i++) {
        work() ; 
    }
    return 0 ;
}

int main(void)
{
    solve() ;
    return 0 ;
}
