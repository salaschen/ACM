/**
 * Not so Mobile, UVa 839.
 * Date: 27/Sep/2017
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct node
{
	int weight ; 
	int wl, dl, wr, dr ; 
	struct node * left ; 
	struct node * right ; 
} node ; 

node * readNode(void)
{
	node * cur = (node *)malloc(sizeof(node)) ; 
	cur->left = NULL ; 
	cur->right= NULL ; 
	scanf("%d %d %d %d\n", &cur->wl, &cur->dl, &cur->wr, &cur->dr) ; 
	if (cur->wl == 0) {
		cur->left = readNode() ; 
		cur->wl = cur->left->weight ; 
	}
	if (cur->wr == 0) {
		cur->right = readNode() ; 
		cur->wr = cur->right->weight ; 
	}
	cur->weight = cur->wl + cur->wr ;
	return cur ; 
}

int freeNode(node * root)
{
	if (root->left != NULL) {
		freeNode(root->left) ; 
	}
	if (root->right != NULL) {
		freeNode(root->right) ; 
	}
	free(root) ; 
	return 0 ;
}

void printTree(node * root)
{
	assert(root) ;
	if (root->left != NULL) {
		printTree(root->left) ; 
	}
	if (root->right != NULL) {
		printTree(root->right) ; 
	}
	printf("weight: %d, left: %d * %d | right: %d * %d\n", 
			root->weight, root->wl, root->dl, root->wr, root->dr) ; 
}

int isBalanced(node * root)
{
	assert(root) ; 
	if (root->left != NULL && isBalanced(root->left) != 0)
		return 1 ; 
	if (root->right != NULL && isBalanced(root->right) != 0)
		return 1 ;
	if (root->wl * root->dl == root->wr * root->dr)
		return 0 ; 
	else
		return 1 ; 
}

int work(int Case)
{
	scanf("\n") ; // read the first blank line
	node * root = readNode() ; 
	if (Case >= 1) 
		printf("\n") ; 
	if (isBalanced(root) == 0){
		printf("YES\n") ; 
	}
	else {
		printf("NO\n") ; 
	}
//	printTree(root) ; // debug
	freeNode(root) ;
	return 0 ;
}

int main(void)
{
	int i, n ; 
	scanf("%d\n", &n) ; 
	for (i=0 ; i < n ; i++) {
		work(i) ;
	}
	return 0 ;
}
