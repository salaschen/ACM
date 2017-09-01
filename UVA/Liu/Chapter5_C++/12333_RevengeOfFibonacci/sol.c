/**
 * revenge of Fibonacci, C version.
 * Date: 01/Sep/2017 
 * Author: Ruowei Chen
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define MAXLEN 21000
#define MAXN 9999

typedef struct Trie
{
	int index ; 
	struct Trie * children[10] ; 
} Trie ;

typedef struct 
{
	int a[6000] ; 
	int len ; 
} BigNum ; 


// Prototypes
void printBigNum(BigNum * b1, char * desc) ; 
Trie * genFibsBigNum(int n) ; 
void bigAdd(BigNum * b1, BigNum * b2, BigNum * c) ; 
BigNum * bigNum(int value)  ;
void outputBigNum(BigNum * b1, char * output, int digits) ; 

Trie * newTrie(void) ; 
void addToRoot(Trie * root, char * fib, int index)  ;
void addToTrie(Trie * trie, char * fib, int index, int pos, int fibLen) ; 
int findRoot(Trie * root, char * query) ; 
int findTrie(Trie * trie, char * query, int pos, int qLen) ; 

int work(void) ;
// END of prototypes

// Functions for BigNumbers
BigNum * bigNum(int value) 
{
	// accept value: 0 <= value <= 9999
	BigNum * big = (BigNum *) malloc(sizeof(BigNum)) ; 
	big->a[0] = value ; 
	big->len = 1 ; 
	return big; 
}

void printBigNum(BigNum * b1, char * desc)
{
	char out[MAXLEN] ; 
	outputBigNum(b1, out, 45) ; 
	printf("%s: %s\n", desc, out) ; 
}

void outputBigNum(BigNum * b1, char * output, int digits)
{
	// convert the Bignum into a string representation and store in output
	assert(b1 && output) ;
	int i;
	int num = 0 ; 
	char * dest = output ; 
	sprintf(dest, "%04d", b1->a[b1->len-1]) ; 
	dest += 4 ; 
	num += 4 ; 
	for (i=b1->len-2 ; i >= 0 && num < digits; i--) {
		sprintf(dest, "%04d", b1->a[i]) ; 
		dest += 4 ; 
		num += 4 ; 
	}
	dest[0] = '\0' ; 

	int leftShift = 0 ; 
	int copyLen = strlen(output) +1; 
	i = 0 ;
	while (output[i] == '0') {
		i++ ; 
		leftShift ++ ; 
		copyLen -- ; 
	}
	memmove(output, output+leftShift, copyLen) ; 
}



// store the result into c
void bigAdd(BigNum * b1, BigNum * b2, BigNum* c)
{
	assert(b1 && b2 && c); 
	int big = b1->len > b2->len? b1->len : b2->len ; 
	int i ;
	int carry = 0 ;
	for (i=0 ; i < big ; i++) {
		c->a[i] = b1->a[i] + b2->a[i] + carry ; 
		carry = 0 ;
		if (c->a[i] > MAXN) {
			carry = 1 ; 
			c->a[i] -= (MAXN+1) ; 
		}
	}
	if (carry != 0) {
		c->len = big+1 ; 
		c->a[c->len-1] = 1 ; 
	}
	else
		c->len = big ; 
}

// end of functions for BigNumbers

// functions for Trie
Trie * newTrie(void)
{
	Trie * t = (Trie *) malloc(sizeof(Trie)) ; 
	int i ; 
	for (i=0 ; i < 10 ; i++) {
		t->children[i] = NULL ; 
	}
	t->index = -1 ; 
	return t ;
}

void addToRoot(Trie * root, char * fib, int index)
{
	assert(root && fib) ; 
	int b = fib[0] - '0' ;
	if (root->children[b] == NULL) {
		root->children[b] = newTrie() ; 
	}
	int fibLen = strlen(fib) ; 
	addToTrie(root->children[b], fib, index, 1, fibLen) ; 
}

void addToTrie(Trie * trie, char * fib, int index, int pos, int fibLen)
{
	if (fibLen == pos || pos >= 41) {
		if (trie->index == -1) {
			trie->index = index ; 
		}
	}
	else {
		int b = fib[pos] - '0' ; 
		if (trie->children[b] == NULL) {
			trie->children[b] = newTrie() ; 
		}
		addToTrie(trie->children[b], fib, index, pos+1, fibLen) ; 
		if (trie->index == -1 || trie->index > index) {
			trie->index = index ;
		}
	}
}

int findRoot(Trie * root, char * query)
{
	int b = query[0] - '0' ; 
	int qLen = strlen(query) ; 
	if (root->children[b] == NULL)
		return -1 ; 
	else
		return findTrie(root->children[b], query, 1, qLen) ; 
	return 0 ; 
}

int findTrie(Trie * trie, char * query, int pos, int qLen)
{
	int b = query[pos] - '0' ; 
	if (qLen == pos) {
		return trie->index ; 
	}
	else {
		if (trie->children[b] == NULL) 
			return -1 ; 
		else 
			return findTrie(trie->children[b], query, pos+1, qLen) ; 
	}
	return 0 ; 
}

// end functions for Trie

// Working functions
Trie * genFibsBigNum(int n)
{
	BigNum * fib0 = bigNum(1) ; 
	BigNum * fib1 = bigNum(1) ; 
	BigNum * fib2 = bigNum(0) ;
	BigNum * temp ;
	Trie * root = newTrie() ; 
	char output[MAXLEN] ; 
	int index = 0 ; 
	while (index <= n)
	{
		outputBigNum(fib0, output, 45) ; 
		addToRoot(root, output, index)  ;

		bigAdd(fib0, fib1, fib2) ; 

		// debug
		//printf("fib(%d)", index) ; 
		//printBigNum(fib0, "") ; 
		
		index += 1 ; 
		temp = fib0 ;
		fib0 = fib1 ; 
		fib1 = fib2; 
		fib2 = temp ; 
		
	}
	// outputBigNum(fib0, output) ; 
	// printBigNum(fib0, "final") ; // debug
	return root ; 
}

int work(void)
{
	Trie * root = genFibsBigNum(99999) ; 
	int n ; 
	scanf("%d\n", &n) ; 
	int i ; 
	char query[50] ;
	for (i = 0 ; i < n ; i++) {
		scanf("%s\n", query) ; 
		int result = findRoot(root, query) ; 
		printf("Case #%d: %d\n", i+1, result) ; 
	}
	return 0 ;
}

int main(void)
{
	work() ; 
//	genFibsBigNum(100000) ; // debug
	return 0 ;
}
