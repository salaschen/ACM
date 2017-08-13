/**
 *	Prob: C implementation of the Solution for the UVA1594 Ducci Sequence
 *	Date: 13/Aug/2017 
 *	Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#define ABS(a) ((a) < 0? (-1*(a)) : (a))

int nextRound(int * list, int size) {
	assert(list) ; 
	int first = list[0] ; 
	int i ; 
	for (i=0 ; i < size-1 ; i++) {
		list[i] = ABS(list[i]-list[i+1]) ; 
	}
	list[size-1] = ABS(first-list[size-1]) ; 
	return 0 ; 
}

// For debug purpose
void printList(int * list, int size, char * name) {
	char * n = name ; 
	if (n == NULL) {
		n = "LIST" ; 
	}
	printf("[%s]:", n) ; 
	int i ; 
	for (i=0 ; i < size-1 ; i++) {
		printf("%d ", list[i]) ; 
	}
	printf("%d\n", list[size-1]) ; 
}

// Return 0 if same, 1 if different.
int isSameList(int *list1, int *list2, int size) {
	assert(list1 && list2) ; 
	int i ;
	for (i=0 ; i < size ; i++) {
		if (list1[i] != list2[i]) 
			return 1 ; 
	}
	return 0 ; 
}

// Return 0 if all zero, 1 if not.
int isAllZero(int *list, int size) {
	assert(list) ; 
	int i ; 
	for (i=0 ; i < size ; i++) {
		if (list[i] != 0)
			return 1 ;
	}
	return 0 ; 
}

int work() {
	int n ; 
	scanf("%d\n", &n) ; 
//	printf("%d\n", n) ; // debug
	int Tort[1000] ; 
	int Hare[1000] ; 	
	int i ; 
	for (i=0 ; i < n ; i++) {
		int temp ; 
		scanf("%d", &temp) ;
		Tort[i] = temp ; 
		Hare[i] = temp ; 
	}
	scanf("\n") ; 
	//printList(Tort, n, "Tort") ; // debug
	//nextRound(Tort, n) ; 
	//printList(Tort, n, "Tort-next") ; // debug

	int rnd = 0 ; 

	while (rnd < 1000) {
		nextRound(Tort, n) ; 
		nextRound(Hare, n) ; 
		nextRound(Hare, n) ; 
		if (isAllZero(Tort, n) == 0) {
			printf("ZERO\n") ; 
			return 0 ; 
		}
		if (isSameList(Tort, Hare, n) == 0) {
			printf("LOOP\n") ; 
			return 0 ; 
		}
		rnd ++ ; 
	}
	printf("LOOP\n") ; 

	return 0 ; 
}

int main(void) {
	int T ; 
	scanf("%d\n", &T) ; 
	int i ;
	for (i=0 ; i < T ; i++) {
		work() ; 
	}
	return 0 ; 
}
