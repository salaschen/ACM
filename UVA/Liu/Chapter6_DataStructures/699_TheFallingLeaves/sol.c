/**
 * UVa 699 - The Falling Leaves
 * Date: 27/Sep/2017 
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

typedef struct node
{
	int pos ; 
	int value ;
	struct node * left ; 
	struct node * right ; 
} node ;

int leftMost ; 
int rightMost ; 

node * readNode(int pos)
{
	
	int v ;
	scanf("%d", &v) ; 
//	printf("v=%d\n", v) ; // debug
	if (v == -1)
		return NULL ; 
	node * cur = (node *)malloc(sizeof(node)) ; 
	cur->value = v ; 
	cur->pos = pos ;
	if (cur->pos < leftMost) {
		leftMost = cur->pos ; 
	}
	if (cur->pos > rightMost) {
		rightMost = cur->pos ; 
	}
	cur->left = readNode(pos-1) ; 
	cur->right = readNode(pos+1) ; 
	return cur ; 
}

int travel(node * root, int * arr)
{
	assert(root) ; 
	if (root->left != NULL) {
		travel(root->left, arr) ; 
	}
	if (root->right != NULL) {
		travel(root->right, arr) ;
	}
	
	int setPos = root->pos - leftMost ;
	arr[setPos] += root->value ;
//	printf("setPos=%d, value=%d\n", setPos, arr[setPos]) ; // debug
	return 0 ;
}

void freeTree(node * root)
{
	if (root == NULL)
		return ; 
	if (root->left != NULL)
		freeTree(root->left) ; 
	if (root->right != NULL)
		freeTree(root->right) ; 
	free(root) ;
}

int work(int Case)
{
	leftMost = 0 ; 
	rightMost = 0 ; 
	node * root = readNode(0) ; 
	if (root == NULL)
		return 1 ; 
	scanf("\n") ;
	
	printf("Case %d:\n", Case) ; 
//	printf("rightMost=%d, leftMost=%d\n", rightMost, leftMost) ; // debug

	// calculating the pile size
	int * arr = (int *)malloc(sizeof(int)*(rightMost-leftMost+10)) ; 
	memset(arr,0, sizeof(int)*(rightMost-leftMost+10)) ; 

	travel(root, arr) ; 
	int i ; 
//	printf("finished travelling\n") ; // debug
	for (i=0 ; i <= rightMost-leftMost ; i++) 
	{
		if (i > 0)
			printf(" ") ; 
		printf("%d", arr[i]) ;
	}
	printf("\n\n") ; 

	// free the memory
	freeTree(root) ;
	free(arr) ; 

	return 0 ;
}

int main(void)
{
	int T = 1 ; 
	while (1) {
		int temp = work(T) ; 
		if (temp == 1) 
			break ; 
		else if (temp == 0) // root is not empty
		{
			T += 1 ;
		}
	}
	return 0 ;
}
