/**
 * Prob: C implementation of the problem Throwing cards away I.
 * Date: 13/Aug/2017 
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

struct node {
	int value ; 
	struct node * next ; 
} ; 

struct node * createNode(int value) {
	struct node * n = malloc(sizeof(struct node)) ; 
	n->value = value ; 
	n->next = n ; 
	return n ; 
}

struct node * appendToNode(struct node * tail, int value) {
	struct node * n = malloc(sizeof(struct node)) ; 
	n->value = value ; 
	n->next = NULL ; 
	tail->next = n ; 
	return n ; 
}

int deleteFirst(struct node **head, struct node ** tail) {
	struct node *old_head = * head ; 
	int value = old_head->value ;
	struct node *next_head = (*head)->next ; 
	assert((*tail)->next == old_head) ; 
	free(old_head) ; 
	(*tail)->next = next_head ; 
	*head = next_head->next ; 
	*tail = next_head ; 
	return value ; 
}

void printList(struct node *head, struct node * tail) {
	printf("[LIST]: ") ; 
	struct node * current = head ; 
	while (current != tail) {
		printf("%d -> ", current->value) ; 
		current = current->next ; 
	}
	printf("%d\n", tail->value) ; 
}

void resultPrint(int * list, int size, char * name){
	printf("%s:", name) ; 	
	if (size == 1) {
		printf(" %d", list[0]) ; 
	}
	else if (size > 1) {
		int i ; 
		for (i=0 ; i < size-1 ; i++) {
			printf(" %d,", list[i]) ; 
		}
		printf(" %d", list[size-1]) ; 
	}
	printf("\n") ; 
}

int work(void) {
	int n ; 
	scanf("%d\n", &n) ; 
	if (n == 0)
		return 1 ; 
	
	struct node * head, * tail ; 
	head = createNode(1) ; 
	tail = head ; 
	int i ; 
	for (i=2 ; i <= n ; i++) {
		tail = appendToNode(tail, i) ; 
	}
	tail->next = head ; 
	
	int d_len = 0  ;
	int d[50] ; 
	while (tail != head) {
		d[d_len++] = deleteFirst(&head, &tail) ; 	
	}
	
	int r[1] ;
	r[0] = head->value ; 

	resultPrint(d, d_len, "Discarded cards") ; 
	resultPrint(r, 1, "Remaining card") ; 

	assert(head) ; 
	free(head) ; 
	return 0 ; 
}

int main(void){
	while (work() == 0) {
		 ;
	}
	return 0 ;
}
