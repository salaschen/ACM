/**
 * Quardtrees, UVa 297
 * Date: 29/Sep/2017 
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAX(a,b) ((a)>(b)? (a) : (b))

typedef struct node 
{
	char type ; // either 'p', 'f', or 'e'
	struct node * childs[4] ; 
	int pixels ; 
	int black ; 
} node ; 

node * readNode(int pixels)
{
	char type = getchar() ; 
	node * result = (node *)malloc(sizeof(node)) ; 
	result->type = type ;
	result->pixels = pixels ;
	if (type == 'p')
	{
		result->black = 0 ; 
		int i ; 
		for (i=0 ; i < 4 ; i++) {
			result->childs[i] = readNode(pixels/4) ;
			result->black += result->childs[i]->black ; 
		}
	}
	else if (type == 'e') {
		result->black = 0 ; 
	}
	else if (type== 'f') {
		result->black = result->pixels ; 	
	}
	else {
		printf("Unrecognized node type has been read.") ; 
		exit(1) ; 
	}
	return result ; 
}

void freeNode(node * root)
{
	assert(root) ; 
	if (root->type == 'p') {
		int i ; 
		for (i=0 ; i < 4 ; i++) {
			freeNode(root->childs[i]) ; 
		}
	}
	free(root) ; 
}

node * mergeNodes(node * t1, node * t2)
{
	assert(t1 && t2) ; 
	node * r = (node *)malloc(sizeof(node)) ; 
	if (t1->type == 'f' || t2->type == 'f') {
		r->type = 'f' ; 
		r->black = MAX(t1->black, t2->black) ; 
	}
	else if (t1->type == 'p' && t2->type == 'p') {
		r->type = 'p' ; 
		r->black = 0 ; 
		int i ; 
		for (i=0 ; i < 4 ; i++) {
			r->childs[i] = mergeNodes(t1->childs[i], 
									  t2->childs[i]) ; 
			r->black += r->childs[i]->black ; 
		}
	}
	else if (t1->type == 'e' || t2->type == 'e') {
		r->black = MAX(t1->black, t2->black) ; 
	}
	return r ; 
}

int work(void)
{
	int pixels = 32 * 32 ; 
	node * t1 = readNode(pixels) ; 
	getchar() ; // eat the '\n'
	node * t2 = readNode(pixels) ;
	getchar() ; // eat the '\n'

//	printf("t1 has %d black pixels\n", t1->black) ; // debug
//	printf("t2 has %d black pixels\n", t2->black) ; // debug

	node * tsum = mergeNodes(t1, t2) ; 
	printf("There are %d black pixels.\n", tsum->black) ; 
	
	freeNode(t1) ; 
	freeNode(t2) ; 
	freeNode(tsum) ; 
	return 0 ; 
}

int main(void)
{
	int i, n ; 
	scanf("%d\n", &n) ; 
	for (i=0 ; i < n ; i++) {
		work() ; 
	}
	return 0 ;
}


