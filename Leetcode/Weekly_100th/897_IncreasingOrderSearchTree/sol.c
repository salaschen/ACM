#include <stdlib.h>

struct TreeNode {
    int val ; 
    struct TreeNode * left ; 
    struct TreeNode * right ; 
} ; 


struct TreeNode * rightMostNode(struct TreeNode * root)
{
    struct TreeNode * cur = root ; 
    while (cur->right != NULL) {
        cur = cur->right ; 
    }
    return cur ; 
}

struct TreeNode * increasingBST(struct TreeNode * root)
{
    if (root == NULL) 
        return NULL ; 
    
    struct TreeNode * left = increasingBST(root->left) ; 
    struct TreeNode * right = increasingBST(root->right) ; 
    root->right = right ; 
    root->left = NULL ; 
    if (left != NULL) {
        struct TreeNode * lchild = rightMostNode(left) ; 
        lchild->right = root ; 
        return left ; 
    }
    else {
        return root ; 
    }
}

