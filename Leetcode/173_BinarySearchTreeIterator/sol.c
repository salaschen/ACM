/**
 * Prob: 173. Binary Search Tree Iterator
 * Author: Ruowei Chen
 * Lang: C
 * Date: 21/Jun/2019
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <time.h>

typedef enum bool {true, false} bool ;

/**
 * Definition for a binary tree node.
 */
struct TreeNode 
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct {
    int stackSize ; 
    int num ; 
    struct TreeNode * stack ; 
} BSTIterator;

int pushStack(BSTIterator * iterator, struct TreeNode * node) 
{
    if (iterator == NULL || node == NULL) {
        return 1 ; 
    }

    // enlarge the stack if space is not enough
    if (iterator->num == iterator->stackSize) {
        int newStackSize = 2 * iterator->stackSize + 1; 
        iterator-> stack = (struct TreeNode *)realloc(iterator->stack,\
                newStackSize*sizeof(struct TreeNode)) ; 
    }
    
    // do the copy
    char * dest = (char *)&iterator->stack[iterator->num] ; 
    memcpy(dest, node, sizeof(struct TreeNode)) ; 
    iterator->num += 1 ; 
    return 0 ; 
}

void popStack(BSTIterator * iterator, struct TreeNode * buf) {
    // store the popped content into the buf
    if (iterator->num == 0 || buf == NULL) {
        return ; 
    }
    
    char * pos = (char *)iterator->stack + sizeof(struct TreeNode)*(iterator->num-1) ; 
    memcpy(buf, pos, sizeof(struct TreeNode)) ; 
    iterator->num -= 1 ; 
}

BSTIterator* bSTIteratorCreate(struct TreeNode* root) 
{
    BSTIterator * iterator = (BSTIterator *)malloc(sizeof(BSTIterator)) ;    
    iterator->num = 0 ; 
    iterator->stackSize = 200 ; 
    iterator->stack = (struct TreeNode *)malloc(sizeof(struct TreeNode)*iterator->stackSize) ;
    assert(iterator->stack != NULL) ; 

    struct TreeNode * node = root ; 
    while (node != NULL) {
        pushStack(iterator, node) ;    
        node = node->left ; 
    }
    return iterator ; 
}

/** @return the next smallest number */
int bSTIteratorNext(BSTIterator* obj) 
{
    if (obj->num == 0) return 0;

    struct TreeNode buf ;
    popStack(obj, &buf) ; 
    int result = buf.val ; 

    struct TreeNode * node = buf.right ; 
    while (node != NULL) {
        pushStack(obj, node) ; 
        node = node->left ; 
    }

    return result;
}

/** @return whether we have a next smallest number */
bool bSTIteratorHasNext(BSTIterator* obj) {
    if (obj->num > 0) {
        return true ;
    }
    else {
        return false ; 
    }
}

void bSTIteratorFree(BSTIterator* obj) 
{
    free(obj->stack) ; 
    free(obj) ; 
    return ;
}

/**
 * Your BSTIterator struct will be instantiated and called as such:
 * BSTIterator* obj = bSTIteratorCreate(root);
 * int param_1 = bSTIteratorNext(obj);

 * bool param_2 = bSTIteratorHasNext(obj);

 * bSTIteratorFree(obj);
*/

// Test functions
struct TreeNode * createNode(int val)
{
    struct TreeNode * result = (struct TreeNode *)malloc(sizeof(struct TreeNode)) ;
    result->left = NULL ; 
    result->right = NULL ; 
    result->val = val ; 
    return result ; 
}

void addToTree(struct TreeNode *root, int num) 
{
    if (root->val >= num) {
        if (root->left == NULL) {
               root->left = createNode(num) ;
        }
        else {
            addToTree(root->left, num) ;
        }
    }
    else {
        if (root->right == NULL) {
            root->right = createNode(num) ; 
        }
        else {
            addToTree(root->right, num) ; 
        }
    }
}

struct TreeNode * buildTree(int * nums, int numSize)
{
    if (numSize == 0) return NULL ; 
    struct TreeNode * root = createNode(nums[0]) ;
    int i; 
    for (i=1 ; i < numSize ; i++) {
        addToTree(root, nums[i]) ; 
    }
    return root ; 
}

void printTree(struct TreeNode * root)
{
    if (root == NULL) return ;      
    printf("[node]: %d,left:", root->val) ; 

    if (root->left != NULL) {
        printf("%d,right:", root->left->val) ;
    }
    else {
        printf("NULL, right:") ; 
    }
    if (root->right != NULL) {
        printf("%d\n", root->right->val) ; 
    }
    else {
        printf("NULL\n") ; 
    }

    printTree(root->left) ; 
    printTree(root->right) ; 
}

int intCmp(const void *i1, const void *i2) { return *(int *)i1 - *(int *)i2 ; }

void randomTest(void)
{
    srandom(time(NULL)) ; 
    int size = 1000 ; 
    int * numbers = (int *)malloc(sizeof(int) * size) ; 
    int i ; 
    for (i=0 ; i < size ; i++) {
        numbers[i] = (int) random() ; 
    }
    qsort(numbers, size, sizeof(int), intCmp) ; 

    struct TreeNode * root = buildTree(numbers, size) ; 
    BSTIterator * iterator = bSTIteratorCreate(root) ; 
    int count = 0 ; 
    
    while (bSTIteratorHasNext(iterator) == true) {
        int cur = bSTIteratorNext(iterator) ; 
        // printf("cur=%d, numbers=%d\n", cur, numbers[count]) ; // debug
        if (cur != numbers[count]) {
            printf("Failed: iterator obtained the wrong number\n") ; 
            return ;
        }
        count ++ ; 
    }
    if (count < size) {
        printf("Failed: iterator doesn't return all the numbers.\n") ; 
    }
    else {
        printf("Passed\n") ; 
    }
}

int main(void)
{
    int nums[5] = {7,3,15,9,20} ;
    int numSize = 5 ;
    struct TreeNode * root = buildTree(nums, numSize) ; 
    printTree(root) ; 

    BSTIterator * iterator = bSTIteratorCreate(root) ; 
    while (bSTIteratorHasNext(iterator) == true) {
        printf("%d\n", bSTIteratorNext(iterator)) ; 
    }

    int i ;
    for (i=0 ; i < 10 ; i++) {
        printf("test[%d]:", i+1) ; 
        randomTest() ;
    }
    return 0;
}
