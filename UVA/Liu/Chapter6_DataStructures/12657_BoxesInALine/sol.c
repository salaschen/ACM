/**
 * UVa 12657 - Boxes in a line
 * Date: 19/Sep/2017
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int inv ; 

void link(int L, int R, int * left, int *right)
{
	right[L] = R ; 
	left[R] = L ; 
}

// deprecated
void reverse(int * left, int * right,  int n)
{
	// Tested - Seems OK
	int i ;
	for (i=1 ; i <= n ; i++) 
	{
		int temp = left[i] ; 
		left[i] = right[i] ; 
		right[i] = temp ; 
	}
	// treat the special head and tail cases
	int oldHead = right[0] ; 
	int oldTail = left[n+1] ;
	right[oldHead] = n+1 ; 
	left[oldTail] = 0 ; 
	right[0] = oldTail ; 
	left[n+1] = oldHead ; 
}	

void analyze(int * left, int * right, int n)
{
	int i  ; 
//	printf("inv=%d\n", inv) ; // debug
	for (i=0 ; i <= n+1 ; i++) {
		printf("[%d]: left:%d, right:%d\n", i, left[i], right[i]) ; 
	}
}

// TODO: Change the way to print when inverse
void printArray(int * left, int * right, int n) 
{
	// analyze(left, right, n) ; // debug
	int * temp = left ; 
	int start = 0 ; 
	if (inv == 1) {
		left = right ; 
		right = temp ; 
		start = n+1 ; 
	}
	int cur = right[start] ; 
	int i ;
	printf("(inv=%d): ", inv) ; 
	for (i=1 ; i <= n ; i++) 
	{
		printf("%d ", cur) ; 
		cur = right[cur] ; 
	}
	printf("\n") ; 
}

// TODO: Treat the first and last (dummy) nodes as normal
void move(int * left, int * right, int n, int c, int X, int Y) 
{
	if (inv == 1) {
		c = (c == 1)? 2 : 1 ; 
	}
	if (c == 1 && left[Y] != X) // Move box X to the left to Y
	{
		link(left[X], right[X], left, right) ; 	
		link(left[Y], X, left, right) ; 
		link(X, Y, left, right) ; 
	}
	else if (c == 2 && right[Y] != X) // Move box X to the right of Y
	{
		link(left[X], right[X], left, right) ; 
		link(X, right[Y], left, right) ;
		link(Y, X, left, right) ; 
	}
}

void swapValue(int * buf, int X, int Y)
{
	int temp = buf[X] ;
	buf[X] = buf[Y] ;
	buf[Y] = temp ; 
}

int isAdjacent(int * left, int * right, int X, int Y)
{
	// return 0 if True, 1 if False.
	if (left[X] == Y || right[X] == Y)
		return 0 ;
	else
		return 1 ; 
}

// DONE: treat the first and last (dummy) node as normal
void swap(int * left, int * right, int n, int X, int Y)
{

	// swap when X and Y are NOT adjacent
	if (isAdjacent(left, right, X, Y) != 0)
	{
		right[left[X]] = Y ; 
		left[right[X]] = Y ; 

		right[left[Y]] = X ; 
		left[right[Y]] = X ; 

		swapValue(left, X, Y) ; 
		swapValue(right, X, Y) ; 
	}
	else // when X and Y are adjacent
	{
		// make X on the left and Y on the right
		if (left[X] == Y) {
			int temp = Y ; 
			Y = X ; 
			X = temp ; 
		}
		int lx = left[X] ; 
		int ry = right[Y] ; 
		left[ry] = X ; 
		right[lx] = Y ; 

		right[X] = ry ; 
		left[X] = Y ; 
		right[Y] = X ;
		left[Y] = lx ; 
	}

}

int left[100010] ;
int right[100010] ;

// DONE: treat the first and last dummy node as normal
long long calculate(int * left, int * right, int n)
{
	long long result = 0 ; 
	int start = 0 ;
	int * temp = left ; 
   	if (inv == 1)
	{
		left = right ; 
		right = temp ; 
		start = n+1 ;
	}	
	int cur = right[start] ; 
	int i ;
	for (i=1 ; i <= n ; i++)
	{
		if (i % 2 == 1)
		{
			result += cur ; 
		}
		cur = right[cur] ; 
	}
	return result ; 
}

int work(int Case)
{
	int n, m ; 
	inv = 0 ; // at start it's not inverse
	if (scanf("%d %d\n", &n, &m) == EOF)
		return 1 ; 
	
	int i ; 
	for (i=1 ; i <= n ; i++)
	{
		left[i] = i-1 ; 
		right[i] = i+1 ; 
	}
	left[n+1] = n ; 
	right[n+1] = -1 ;
	left[0] = -1 ; 
	right[0] = 1 ;

#ifdef DEBUG
	printf("Initial: ") ; // debug
	printArray(left, right, n) ; // debug
#endif

	// process commands.
	for (i=0 ; i < m ; i++) {
		int c, X, Y ;
		scanf("%d", &c) ;
		if (c == 4) {
			// reverse(left, right, n) ; 
		
			inv = (inv + 1) % 2 ; 
			/**
			int oldHead = right[0] ; 
			int oldTail = left[n+1] ; 
			right[0] = oldTail ; 
			left[n+1] = oldHead ; 
			if (inv == 0) {
				right[oldHead] = n+1 ; 
				left[oldTail] = 0 ; 
			}
			else {
				left[oldHead] = n+1 ; 
				right[oldTail] = 0 ; 
			}
			*/
#ifdef DEBUG
			printf("cmd: %d\n", c) ; // debug
#endif
		}
		else {
			scanf("%d %d\n", &X, &Y) ; 
#ifdef DEBUG
			printf("cmd: %d %d %d\n", c, X, Y) ; // debug
#endif
			switch(c) {
				case 1:
				case 2:
					move(left, right, n, c, X, Y) ; 
					break ; 
				case 3:
					swap(left, right, n, X, Y) ; 	
					break ;
			} ; 
		}
#ifdef DEBUG
		printArray(left, right, n) ; // debug
#endif
	}

#ifdef DEBUG	
	printf("final: ") ; // debug
	printArray(left, right, n) ; // debug
#endif 

	long long result = calculate(left, right, n) ; 
	printf("Case %d: %lld\n", Case, result) ; 

	return 0 ;
}

int main(void)
{
	int Case = 1 ; 
	while (work(Case) == 0)
	{
		Case ++ ;
	}
	return 0 ;
}
