/**
 * Problem: Contains Duplicate - Easy
 * Author: Ruowei Chen
 * Date: 27/Dec/2021
 * Note:
 *  1)  Use hashmap and binary search tree.
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
typedef struct Node {
    long long val ;
    struct Node* left ;
    struct Node* right ;
} Node ;

typedef struct Hashmap {
    int numBucket; 
    void ** buf ;
} Hashmap ;


// Prototypes
Node * createNode(long long value) ;

// Definitions
Node * createNode(long long value) {
    Node * node = (Node *)malloc(sizeof(Node)) ;
    node->val = value ;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// return True if value is not already in the tree
// False otherwise
bool addNumber(Node * root, long long value) {
    if (root == NULL || root->val == value) {
        return true;
    }
    if (root->val < value) {
        if (root->right != NULL) {
            return addNumber(root->right, value);
        } else {
            root->right = createNode(value) ;
            return false;
        }
    } else { // root->val > value
        if (root->left != NULL) {
            return addNumber(root->left, value) ;
        } else {
            root->left = createNode(value) ;
            return false;
        }
    }
    return false;
}

Hashmap * createHashmap(int numBucket)  {
    Hashmap * map = (Hashmap *)malloc(sizeof(Hashmap)) ;
    map->numBucket = numBucket ;
    map->buf = calloc(numBucket, sizeof(void *)) ;
    return map ;
} 

#define abs(A) (((A) < 0)? (-1 * (A)) : (A))
bool addMap(Hashmap * map, long long value) {
    int index = abs(value)  % map->numBucket ;
    // printf("value=%lld, index=%d\n", value, index) ; // debug
    bool result ; 
    if (map->buf[index] == NULL) {
        map->buf[index] = createNode(value) ;
        result = false;
    } else {
        result = addNumber((Node *)map->buf[index], value) ;
    }
    // printf("adding %d, result=%d\n", value, result) ; // debug
    return result ;
}

bool containsDuplicate(int * nums, int numsSize) {
    Hashmap * map = createHashmap(17) ; 
    bool result = false;
    for (int i = 0 ; i < numsSize ; i++) {
        result = result | addMap(map, nums[i]) ;
        if (result == 1) {
            return true;
        }
    }
    return result ; 
}

// main
int main(void) {
    // int nums[] = {1,1,1,3, 3, 4,3, 2,3,4} ;
    // int nums[] = {1,2,3,1} ;
    // int nums[] = {1,2,3,4} ;
    int nums[] = {1,5,-2,-4,0} ;
    bool result = containsDuplicate(nums, sizeof(nums)/sizeof(int)) ;
    printf("reuslt=%d\n", result) ;
    return 0 ;
}
